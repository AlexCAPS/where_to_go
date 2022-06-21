from django.apps import AppConfig

from where_to_go.settings import env


class ArtmapAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artmap_app'

    # set max place objects viewed on map page
    top_slice = env.int('TOP_SLICE', 1000)
