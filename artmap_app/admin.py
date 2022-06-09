from django.contrib import admin
from django import forms

from artmap_app.models import *


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        widgets = {
            'description_short': forms.Textarea
        }
        fields = '__all__'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
