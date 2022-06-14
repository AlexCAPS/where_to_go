from django.urls import path

from artmap_app.views import IndexView, places_view

urlpatterns = [
    path('', IndexView.as_view()),
    path('places/<int:pk>/', places_view),
]