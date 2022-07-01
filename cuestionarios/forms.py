from django import forms
from cuestionarios.models import CuestionariosPreguntas, CuestionariosRespuestas, Cuestionarios, CuestionarioBase

class CuestionariosForm(forms.ModelForm):
    class Meta:
        model = Cuestionarios
        fields = ('title', 'description','status',)

class PreguntasForm(forms.ModelForm):
    class Meta:
        model = CuestionariosPreguntas
        fields = ('pregunta',)


class RespuestasForm(forms.ModelForm):
    class Meta:
        model = CuestionariosRespuestas
        fields = ('respuesta',)

class ResponderCuestionarioBaseForm(forms.ModelForm):
    class Meta:
        model = CuestionarioBase
        fields = ('Pregunta1','Pregunta2','Pregunta3','Pregunta4','Pregunta5')