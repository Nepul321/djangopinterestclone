from .views import (
    AllPinsView
)

from django.urls import path

urlpatterns = [
    path('global/', AllPinsView, name="global-pins"),
]
