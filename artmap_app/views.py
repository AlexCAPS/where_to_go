from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from artmap_app.models import Place


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['places'] = Place.prepare_geodata()
        return context


def places_view(request, pk):
    if not request.method == 'GET':
        return HttpResponseBadRequest()

    place = get_object_or_404(Place, pk=pk)
    formatted_place = place.to_dict()
    return JsonResponse(formatted_place, json_dumps_params={'ensure_ascii': False})
