from django.shortcuts import render
from catalogos.models import AlumnoSelfRegister
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def alumnos_add(request):
    pass

def alumnos_list(request):
    pass

def alumnos_edit(request):
    pass

# Create your views here.
def alumnos_delete(request, pk):
    alumno_obj = get_object_or_404(AlumnoSelfRegister, pk=pk)
    alumno_obj.status = False
    alumno_obj.save()
    msg = messages.success(request, 'Alumno eliminado con exito')
    return redirect('cursoevento:alumnos_list')
    #return render(request, 'cursoevento/cursoeventos_list.html', context)