from django.conf.urls import url
from vecinos.apps.registro import views as reg_views

urlpatterns = [
    url(r'^$',
    	reg_views.index_views,
    	name='VistaIndex'),
    url(r'^registro/vecinos$',
        reg_views.registro_vecino_views,
        name='VistaRegistro'),
    url(r'^registro/calles$',
    	reg_views.registro_calle_views,
    	name='VistaCalles'),
    url(r'^listado/calles$',
    	reg_views.listado_calles_views,
    	name='VistaListadoCalles'),
    url(r'^listado/vecinos$',
    	reg_views.listado_vecinos_views,
    	name='VistaListadoVecinos'),
]