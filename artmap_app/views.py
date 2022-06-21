from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from artmap_app.apps import ArtmapAppConfig
from artmap_app.models import Place


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        top_slice = ArtmapAppConfig.top_slice
        places = Place.objects.order_by('-pk').all()[:top_slice]  # top new objects
        context['places'] = self._prepare_geodata(places)

        return context

    @staticmethod
    def _prepare_geodata(places):
        features = [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat],

                },
                'properties': {
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': reverse('place_api', args=[place.pk]),
                }
            }
            for place in places
        ]

        geodata = {
            "type": "FeatureCollection",
            "features": features,
        }
        return geodata


def places_view(request, pk):
    if not request.method == 'GET':
        return HttpResponseBadRequest()

    place = get_object_or_404(Place, pk=pk)
    formatted_place = place.to_dict()
    return JsonResponse(formatted_place, json_dumps_params={'ensure_ascii': False})
