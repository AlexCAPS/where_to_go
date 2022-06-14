from django import forms

from artmap_app.models import Place


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        widgets = {
            'description_short': forms.Textarea
        }
        fields = '__all__'
