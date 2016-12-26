from django.views.static import serve
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('vecinos.apps.registro.urls')),
    url(r'^admin/', admin.site.urls),
]
