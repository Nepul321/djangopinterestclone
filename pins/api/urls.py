from django.urls import path
from .views import (
    ImagePinsListView
)

urlpatterns = [
    path('images/', ImagePinsListView, name="pins-list"),
]
