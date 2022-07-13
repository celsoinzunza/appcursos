#from django.conf.urls import url
from django.urls import path, re_path
from .views import catalogos

urlpatterns = [
    # -- instructores
    path('instructores/',catalogos.instructores_list, name='instructores_list'),
    re_path(r'^instructores/add/$', catalogos.instructores_add, name='instructores_add'),
    re_path(r'^instructores/edit/(?P<pk>[0-9]+)/$',
        catalogos.instructores_edit, name='instructores_edit'),
    re_path(r'^instructores/delete/(?P<pk>[0-9]+)/$',
        catalogos.instructores_delete, name='instructores_delete'),

    # -- cursos
    path('cursos/',catalogos.cursos_list, name='cursos_list'),
    re_path(r'^cursos/add/$', catalogos.cursos_add, name='cursos_add'),
    re_path(r'^cursos/edit/(?P<pk>[0-9]+)/$',
        catalogos.cursos_edit, name='cursos_edit'),
    re_path(r'^cursos/delete/(?P<pk>[0-9]+)/$',
        catalogos.cursos_delete, name='cursos_delete'),

    # -- sedes
    path('sedes/',catalogos.sedes_list, name='sedes_list'),
    re_path(r'^sedes/add/$', catalogos.sedes_add, name='sedes_add'),
    re_path(r'^sedes/edit/(?P<pk>[0-9]+)/$',
        catalogos.sedes_edit, name='sedes_edit'),
    re_path(r'^sedes/delete/(?P<pk>[0-9]+)/$',
        catalogos.sedes_delete, name='sedes_delete'),

]
