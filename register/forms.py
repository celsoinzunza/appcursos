from django import forms
from catalogos.models import AlumnoSelfRegister
from cursoevento.models import CursoEvento

class AlumnoSelfRegisterForm(forms.ModelForm):
    class Meta:
        model = AlumnoSelfRegister
        fields = ('first_name','last_name','email','phone','empresa')

class CursoEventoForm(forms.ModelForm):
    class Meta:
        model = CursoEvento
        fields = ('descripcion', 'curso', 'fechayhora_inicio','fechayhora_final','duracion_hrs','instructor','lugar','status')