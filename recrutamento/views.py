import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect

from accounts.decorators.group_required import group_required
from .forms import VagaForm
from .models import Vaga, CandidatoVaga, Candidato, Recrutador
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Rota principal.")
@login_required
@group_required('recrutador')
def recrutador_vagas_home(request):
    contexto = {'vagas':Vaga.objects.filter(recrutador_id=request.user.id)}
    return render(request,'recrutador/vagas/home.html',contexto)
@login_required
@group_required('candidato')
def candidato_vagas_home(request):
    query = request.POST.get('q', '')
    vagas = Vaga.objects.none()

    if query:
        palavras = query.split()

        filtros = Q()
        for palavra in palavras:
            filtros |= Q(titulo__icontains=palavra)
            filtros |= Q(descricao__icontains=palavra)

        sem_vagas = False
        vagas = Vaga.objects.filter(filtros).distinct()
        if len(vagas)==0:
            sem_vagas = True

        return render(
            request,
            'candidato/home.html',
            {
                'vagas': vagas,
                'query': query,
                'sem_vagas': sem_vagas,
            }
        )
    return render(request,'candidato/home.html',)

def recrutador_vagas_criar(request:HttpRequest):

    contexto = {
        "form": VagaForm,
    }
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.recrutador = request.user
            vaga.save()
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


@login_required
def candidato_visualizar_vaga(request:HttpRequest,id):
    vaga = Vaga.objects.get(id=id)
    recrutador = Recrutador.objects.get(user_id=vaga.recrutador_id)
    return render(request, 'candidato/visualizar_vaga.html',{'vaga':vaga,'recrutador':recrutador})

@login_required
def efetuar_candidatura(request:HttpRequest,id):
    if request.method == 'POST':
        candidato = Candidato.objects.get(user_id=request.user.id)
        vaga = Vaga.objects.get(id=id)
        candidato_vaga = CandidatoVaga.objects.filter(
            vaga_id=vaga.id,
            candidato_id=candidato.id
        ).first()
        if not candidato_vaga:
            CandidatoVaga.objects.create(candidato_id=candidato.id,vaga_id=vaga.id,data_candidatura=datetime.datetime.now(),status='Aplicado')

        return render(request, 'candidato/home.html')

@login_required
def visualizar_vagas_aplicadas(request:HttpRequest):

    candidato_vagas = CandidatoVaga.objects.filter(candidato_id=request.user.candidato.id)

    return render(request, 'candidato/vagas_aplicadas.html',{'candidato_vagas':candidato_vagas})
@login_required
def cancelar_aplicacao(request:HttpRequest,id):
    candidato_vaga = CandidatoVaga.objects.get(id=id)
    candidato_vaga.delete()
    return redirect("recrutamento:visualizar_vagas_aplicadas")


