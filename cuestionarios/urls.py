from django.urls import path
from .views import cuestionarios

urlpatterns = [
    path("", cuestionarios.cuestionarios_list, name="cuestionarios_list"),
    path('add',cuestionarios.cuestionario_add, name ='cuestionario_add'),
    path('preguntas/<int:cuestionario>/list',cuestionarios.preguntas_list, name ='preguntas_list'),
    path('preguntas/<int:cuestionario>/add',cuestionarios.preguntas_add, name ='preguntas_add'),
    path('respuestas/base',cuestionarios.ResponderCuestionarioBase, name ='ResponderCuestionarioBase'),
    path("cuestionariobase_done", cuestionarios.cuestionariobase_done, name="cuestionariobase_done"),
]