from django.urls import path
from .views import alumnos

urlpatterns = [
    path("", alumnos.alumnos_list, name="alumnos_list"),
    path('add',alumnos.alumnos_add, name ='alumnos_add'),
    path('edit/<int:pk>',alumnos.alumnos_edit, name ='alumnos_edit'),
    path('delete/<int:pk>',alumnos.alumnos_delete, name ='alumnos_delete'),

]