from django.urls import path
from .views import cursoevento

urlpatterns = [
    path("", cursoevento.cursoeventos_list, name="cursoeventos_list"),
    path("add", cursoevento.cursoevento_add, name="cursoevento_add"),
    path("edit/<int:pk>", cursoevento.cursoevento_edit, name="cursoevento_edit"),
    path("delete/<int:pk>", cursoevento.cursoevento_delete, name="cursoevento_delete"),
    path("registers/<int:evento>", cursoevento.register_list, name="register_list"),
    path("registers/<int:evento>/add", cursoevento.registers_add, name="registers_add"),
    path("alumnos", cursoevento.alumnos_list, name="alumnos_list"),
]
