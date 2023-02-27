from django.urls import path
from .views import (
    PinsListView
)

urlpatterns = [
    path('', PinsListView, name="pins-list"),
]
