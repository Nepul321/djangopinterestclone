from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('pins.urls')),
    path('api/', include('base.api.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('authentication.urls')),
    path('api/pins/', include('pins.api.urls')),
]
