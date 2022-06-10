from django.views.generic import TemplateView

from artmap_app.models import Place


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['places'] = Place.prepare_geodata()
        return context
