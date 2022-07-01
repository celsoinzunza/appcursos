from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from ..forms import CursoEventoForm, AlumnoForm
from catalogos.models import AlumnoSelfRegister,  Alumnos
from cursoevento.models import CursoEvento, RegistroEventos

def cursoeventos_list(request):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context['cursoeventos_list'] = CursoEvento.objects.filter(status=True)
    return render(request, 'cursoevento/cursoeventos_list.html', context)


def cursoevento_add(request):
    if request.method == 'POST':
        form = CursoEventoForm(request.POST or None)
        if form.is_valid():
            cursoevento_obj = form.save(commit=False)
            cursoevento_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Curso creado satisfactorimente')

            return redirect('cursoevento:cursoeventos_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = CursoEventoForm()

    context = {
        "form": form
    }
    return render(request, 'cursoevento/cursoevento_form.html', context)

def cursoevento_delete(request):
    pass

def cursoevento_edit(request, pk):
    context = {}
    context['cursoevento_obj'] = get_object_or_404(CursoEvento, pk=pk)

    if request.method == 'POST':
        form = CursoEventoForm(request.POST, instance=context['cursoevento_obj'])
        if form.is_valid():
            cursoevento_obj = form.save(commit=False)
            cursoevento_obj.save()

            msg = messages.success(
                request, 'Curso Evento modificado satisfactorimente')

            # -- User Logs (Info, Access, Error)
            # user_logs(request, None, 'I', 'Sucursal modificada satisfactorimente')

            return redirect('cursoevento:cursoeventos_list')
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = CursoEventoForm(instance=context['cursoevento_obj'])

    context = {
        "form": form
    }

    return render(request, 'cursoevento/cursoevento_form.html', context)

def register_list(request, pk):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context["evento"] = get_object_or_404(CursoEvento, pk=pk)
    context["register_list"] = RegistroEventos.objects.filter(status=True, evento=pk)
    return render(request, "cursoevento/register_list.html", context)

def alumnos_list(request):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context["list_self"] = AlumnoSelfRegister.objects.filter(status=True)
    context["list"] = Alumnos.objects.filter(status=True)
    return render(request, "cursoevento/registrocursos_alumnos.html", context)

def registers_add(request, evento):
    if request.method == "POST":
        form = AlumnoForm(request.POST or None)
        if form.is_valid():
            alumno_obj = form.save(commit=False)
            alumno_obj.save()

    # -- Message to beneficiary
            msg = messages.success(request, 'Sucursal creado satisfactorimente')
            #return redirect('cursoevento:registers')
            return redirect('/cursoevento/alumnos')
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = AlumnoForm()

    context = {
        "form": form,
        "evento" : get_object_or_404(CursoEvento, pk=evento)
    }
    return render(request, "cursoevento/register_form.html", context)