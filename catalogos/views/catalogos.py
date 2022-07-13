from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#from core.utils import user_logs, delete_record, delete_item
from django.http import JsonResponse

from django.db.models import Count, Sum, Q, Max, F
# Create your views here.

from catalogos.models import Instructor, Cursos, Sedes

from ..forms import InstructorForm, CursoForm, SedeForm

# ------- INSTRUCTORES ------- #
def instructores_list(request):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context['instructores_list'] = Instructor.objects.filter(status=True).order_by('first_name')
    return render(request, 'catalogos/instructores/instructores_list.html', context)

def instructores_add(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST or None)
        if form.is_valid():
            instructor_obj = form.save(commit=False)
            instructor_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Instructor creado satisfactorimente')

            return redirect('catalogos:instructores_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = InstructorForm()

    context = {
        "form": form
    }

    return render(request, 'catalogos/instructores/instructores_form.html', context)

def instructores_edit(request, pk):
    instructor_obj = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor_obj)
        if form.is_valid():
            instructor_obj = form.save(commit=False)
            instructor_obj.save()

            msg = messages.success(
                request, 'Instructor modificado satisfactorimente')

            # -- User Logs (Info, Access, Error)
            # user_logs(request, None, 'I', 'Sucursal modificada satisfactorimente')

            return redirect('catalogos:instructores_list')
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = InstructorForm(instance=instructor_obj)

    context = {
        "form": form
    }

    return render(request, 'catalogos/instructores/instructores_form.html', context)

def instructores_delete(request):
    pass


# ------ CURSOS --------- #
def cursos_list(request):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context['cursos_list'] = Cursos.objects.filter(status=True)
    return render(request, 'catalogos/cursos/cursos_list.html', context)

def cursos_add(request):
    if request.method == 'POST':
        form = CursoForm(request.POST or None)
        if form.is_valid():
            cultivo_obj = form.save(commit=False)
            cultivo_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Curso creado satisfactorimente')

            return redirect('catalogos:cursos_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = CursoForm()

    context = {
        "form": form
    }

    return render(request, 'catalogos/cursos/curso_form.html', context)

def cursos_delete(request):
    pass

def cursos_edit(request, pk):
    context = {}
    context['curso_obj'] = get_object_or_404(Cursos, pk=pk)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=context['curso_obj'])
        if form.is_valid():
            curso_obj = form.save(commit=False)
            curso_obj.save()

            msg = messages.success(
                request, 'Curso modificado satisfactorimente')

            # -- User Logs (Info, Access, Error)
            # user_logs(request, None, 'I', 'Sucursal modificada satisfactorimente')

            return redirect('catalogos:cursos_list')
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = CursoForm(instance=context['curso_obj'])

    context = {
        "form": form
    }

    return render(request, 'catalogos/cursos/curso_form.html', context)


    
# ------ SEDES --------- #
def sedes_list(request):
    context = {}
    context['sedes_list'] = Sedes.objects.filter(status=True)
    return render(request, 'catalogos/sedes/sedes_list.html', context)

def sedes_add(request):
    if request.method == 'POST':
        form = SedeForm(request.POST or None)
        if form.is_valid():
            cultivo_obj = form.save(commit=False)
            cultivo_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Sede creada satisfactorimente')

            return redirect('catalogos:sedes_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = SedeForm()

    context = {
        "form": form
    }

    return render(request, 'catalogos/sedes/sede_form.html', context)

def sedes_delete(request):
    pass

def sedes_edit(request, pk):
    context = {}
    context['sede_obj'] = get_object_or_404(Sedes, pk=pk)

    if request.method == 'POST':
        form = SedeForm(request.POST, instance=context['sede_obj'])
        if form.is_valid():
            context['sede_obj'] = form.save(commit=False)
            context['sede_obj'].save()

            msg = messages.success(
                request, 'Sede modificado satisfactorimente')

            # -- User Logs (Info, Access, Error)
            # user_logs(request, None, 'I', 'Sede modificada satisfactorimente')

            return redirect('catalogos:sedes_list')
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = SedeForm(instance=context['sede_obj'])

    context = {
        "form": form
    }

    return render(request, 'catalogos/sedes/sede_form.html', context)