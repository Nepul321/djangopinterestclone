from django.urls import path
from .views import (
    ImagePinsListView,
    ImagePinDetailView
)

urlpatterns = [
    path('images/', ImagePinsListView, name="pins-list"),
    path('images/<int:id>/', ImagePinDetailView, name="pins-detail"),
]
