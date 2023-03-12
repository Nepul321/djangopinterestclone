from django.urls import path
from .views import (
    ImagePinsListView,
    ImagePinDetailView,
    ImagePinCreateView,
    ImagePinUpdateView
)

urlpatterns = [
    path('images/', ImagePinsListView, name="pins-list"),
    path('images/<int:id>/', ImagePinDetailView, name="pins-detail"),
    path('images/create/', ImagePinCreateView, name="pins-create"),
    path('images/<int:id>/update/', ImagePinUpdateView, name="pins-update"),
]
