from django.conf.urls import url
from vecinos.apps.registro import views as reg_views
from django.views.generic import ListView, DetailView
from vecinos.apps.registro.models import Calle

urlpatterns = [
    url(r'^createCalle/$', reg_views.create_calle, name='createCalles'),
    url(r'^listCalles/$', ListView.as_view(model=Calle,), name='listaCalles'),
    url(r'^calle/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Calle,)),
    url(r'^calle/(?P<slug>[-\w]+)/update/$', reg_views.update_calle,
        name="update"),
    url(r'^listCasa/$', reg_views.list_casa, name='casa_list'),
    url(r'^createCasa/$', reg_views.create_casa, name='casa_new'),
    url(r'^edit/(?P<id>[-\w]+)/$', reg_views.update_casa, name='casa_edit'),
    url(r'^delete/(?P<id>[-\w]+)/$', reg_views.delete_casa,
        name='casa_delete'),
    url(r'^calles/$', reg_views.calles, name='calles'),
    url(r'^like_calles/$', reg_views.like_calles, name='like_calles'),
]
