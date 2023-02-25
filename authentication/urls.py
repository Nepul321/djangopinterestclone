from django.urls import path
from .views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('login/', LoginView, name="login-view"),
    path('logout/', LogoutView, name="logout-view"),
]
