import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from catalogos.models import AlumnoSelfRegister
from register.forms import AlumnoSelfRegisterForm
from cursoevento.models import CursoEvento



def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello theres, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def register_self(request, evento):
    if request.method == "POST":
        form = AlumnoSelfRegisterForm(request.POST or None)
        if form.is_valid():
            alumno_obj = form.save(commit=False)
            alumno_obj.save()

    # -- Message to beneficiary
            msg = messages.success(request, 'Registro al curso satisfactorimente')
            #return redirect('register:register_self_done')
            return redirect('/register/register_self_done/' + str(evento))
        else:
            msg = messages.error(request, 'Hubo un error')
    else:
        form = AlumnoSelfRegisterForm()

    context = {
        "form": form,
        "evento" : get_object_or_404(CursoEvento, pk=evento)
    }
    return render(request, "register/register_self_form.html", context)

def register_self_done(request, evento):
    context = {}
    context["evento"] = get_object_or_404(CursoEvento, pk=evento)
    return render(request, "register/register_done.html", context)

