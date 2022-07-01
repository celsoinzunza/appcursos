from django import forms
from catalogos.models import Alumnos
from cursoevento.models import CursoEvento

class CursoEventoForm(forms.ModelForm):
    class Meta:
        model = CursoEvento
        fields = ('descripcion', 'curso', 'fechayhora_inicio','fechayhora_final','duracion_hrs','instructor','lugar','status')


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('first_name','last_name','email','phone','empresa','status')
