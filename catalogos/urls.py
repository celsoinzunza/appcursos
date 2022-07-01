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


    path('cursos/',catalogos.cursos_list, name='cursos_list'),
    re_path(r'^cursos/add/$', catalogos.cursos_add, name='cursos_add'),
    re_path(r'^cursos/edit/(?P<pk>[0-9]+)/$',
        catalogos.cursos_edit, name='cursos_edit'),
    re_path(r'^cursos/delete/(?P<pk>[0-9]+)/$',
        catalogos.cursos_delete, name='cursos_delete'),

]
