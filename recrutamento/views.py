from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect
from .forms import RecrutadorForm
from . models import Vaga,CandidatoVaga

def index(request):
    return HttpResponse("Rota principal.")
def recrutador_vagas_home(request):
    contexto = {'vagas':Vaga.objects.all()}
    return render(request,'recrutador/vagas/home.html',contexto)

def recrutador_vagas_criar(request:HttpRequest):

    contexto = {
        "form": RecrutadorForm,
    }
    if request.method == 'POST':
        form = RecrutadorForm(request.POST)
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
    formulario = RecrutadorForm(instance=vaga)
    if request.method == 'POST':
        formulario = RecrutadorForm(request.POST, instance=vaga)
        if formulario.is_valid():
            formulario.save()
            return redirect("recrutamento:recrutador_vagas_home")

    context = {'formulario':formulario}
    return render(request, 'recrutador/vagas/editar.html',context)

def criar_usuario(request:HttpRequest):
    return None

def candidato_buscar_vaga(request:HttpRequest,nome):
    return None

def candidato_home(request):
    contexto = {'vagas_do_candidato' :CandidatoVaga.objects.get(candidato_id=1)}
    return render(request,'candidato/home.html',contexto)