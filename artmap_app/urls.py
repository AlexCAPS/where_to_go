from django.urls import path

from artmap_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]