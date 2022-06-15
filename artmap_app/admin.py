from django.contrib import admin
from django.utils.html import format_html

from artmap_app.forms import PlaceAdminForm
from artmap_app.models import *


class InlineImageAdmin(admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']

    @staticmethod
    def image_preview(img_obj: Image):
        return format_html('<img style="height:200px;width:auto;" src="{}" />', img_obj.pict.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm
    inlines = [
        InlineImageAdmin,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
