from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from ..forms import CuestionariosForm, PreguntasForm, RespuestasForm, ResponderCuestionarioBaseForm
from cuestionarios.models import (
    Cuestionarios,
    CuestionariosPreguntas,
    CuestionariosRespuestas,
    CuestionarioBase,
)

def cuestionarios_list(request):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context["list"] = Cuestionarios.objects.all()
    context["respuestas"] = CuestionarioBase.objects.all()
    return render(request, "cuestionarios/cuestionarios_list.html", context)

def cuestionario_add(request):
    if request.method == 'POST':
        form = CuestionariosForm(request.POST or None)
        if form.is_valid():
            cuestionario_obj = form.save(commit=False)
            cuestionario_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Cuestionario creado satisfactorimente')

            return redirect('cuestionarios:cuestionarios_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = CuestionariosForm()

    context = {
        "form": form
    }

    return render(request, 'cuestionarios/cuestionario_form.html', context)    


def preguntas_list(request, cuestionario):
    context = {}
    # context['cultivos_list'] = Cultivo.objects.filter(status=True).order_by('name')
    context["list"] = CuestionariosPreguntas.objects.filter(cuestionario = cuestionario)
    return render(request, "cuestionarios/preguntas_list.html", context)


def preguntas_add(request, cuestionario):
    if request.method == 'POST':
        form = PreguntasForm(request.POST or None)
        if form.is_valid():
            pregunta_obj = form.save(commit=False)
            pregunta_obj.cuestionario_id = cuestionario
            pregunta_obj.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Pregunta creado satisfactorimente')

            return redirect('cuestionarios:cuestionarios_list')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = PreguntasForm()

    context = {
        "form": form
    }

    return render(request, 'cuestionarios/preguntas_form.html', context) 


def ResponderCuestionarioBase(request):
    if request.method == 'POST':
        form = ResponderCuestionarioBaseForm(request.POST or None)
        if form.is_valid():
            ojb_cuestionario = form.save(commit=False)
            ojb_cuestionario.save()

            # -- Message to beneficiary
            msg = messages.success(request, 'Se recibieron tus respuestas correctamente.')

            return redirect('cuestionarios:cuestionariobase_done')
        else:
            msg = messages.error(request, 'Hubo un error.')
    else:
        form = ResponderCuestionarioBaseForm()

    context = {
        "form": form
    }

    return render(request, 'cuestionarios/responder_cuestionario_base.html', context)  


def cuestionariobase_done (request):
    context = {}
    return render(request, "cuestionarios/cuestionario_done.html", context)    