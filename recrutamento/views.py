from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect


from .forms import VagaForm
from . models import Vaga,CandidatoVaga,Candidato
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Rota principal.")
@login_required

def recrutador_vagas_home(request):
    contexto = {'vagas':Vaga.objects.filter(recrutador_id=request.user.id)}
    return render(request,'recrutador/vagas/home.html',contexto)
@login_required

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
def candidato_buscar_vagas(request):
    return None


