from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('juntagrico.urls')),
    path(r'impersonate/', include('impersonate.urls')),
]
