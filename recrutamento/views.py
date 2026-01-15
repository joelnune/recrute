from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect

from accounts.decorators.permissions import recrutador_required, candidato_required
from .forms import VagaForm
from . models import Vaga,CandidatoVaga,Candidato
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Rota principal.")
@login_required

def recrutador_vagas_home(request):
    contexto = {'vagas':Vaga.objects.all()}
    return render(request,'recrutador/vagas/home.html',contexto)
@login_required

def candidato_vagas_home(request):
    contexto = {'vagas':Vaga.objects.all()}
    return render(request,'candidato/home.html',contexto)

def recrutador_vagas_criar(request:HttpRequest):

    contexto = {
        "form": VagaForm,
    }
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recrutamento:recrutador_vagas_home")


    return render(request,'recrutador/vagas/criar.html',contexto)

def recrutador_vagas_remover(request:HttpRequest,id):
    vaga = Vaga.objects.get(id=id)
    vaga.delete()
    return redirect("recrutamento:recrutador_vagas_home")

def recrutador_vagas_editar(request:HttpRequest,id):
    vaga = Vaga.objects.get(id=id)
    formulario = VagaForm(instance=vaga)
    if request.method == 'POST':
        formulario = VagaForm(request.POST, instance=vaga)
        if formulario.is_valid():
            formulario.save()
            return redirect("recrutamento:recrutador_vagas_home")

    context = {'formulario':formulario}
    return render(request, 'recrutador/vagas/editar.html',context)

