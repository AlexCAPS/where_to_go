from django.contrib import admin

from artmap_app.forms import PlaceAdminForm
from artmap_app.models import *


class InlineImageAdmin(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm
    inlines = [
        InlineImageAdmin,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
