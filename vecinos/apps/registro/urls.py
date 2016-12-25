from django.conf.urls import url
from vecinos.apps.registro import views as reg_views

urlpatterns = [
    
    url(r'^$',
        reg_views.registro_vecino_views,
        name='VistaRegistro'),
]