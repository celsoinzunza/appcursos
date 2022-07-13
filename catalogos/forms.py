from django.contrib.auth.models import User
from django import forms
from catalogos.models import Instructor, Cursos, Sedes

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('first_name', 'last_name', 'telefono', 'email','rfc','banco','cuentabancaria')


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ('name', 'description','description2','description3','categoria')


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ('name', 'domicilio','Estado','Ciudad','cp','telefono','rfc','banco','cuentabancaria','nombrecontacto')