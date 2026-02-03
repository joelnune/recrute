from asyncio.windows_events import NULL

from django.db import models
from django.contrib.auth.models import User

class Candidato(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    nome = models.CharField(max_length=100,null=True)
    cpf = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    curriculo = models.BinaryField(blank=True, null=True)
    cargo = models.CharField(max_length=100,null=True)

class Recrutador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nome_empresa = models.CharField(max_length=100,null=True)
    descricao_empresa = models.CharField(max_length=600,null=True)
    descricao = models.CharField(max_length=600,null=True)
    cnpj = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100,null=True)


class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400,null=True)
    responsabilidades = models.CharField(max_length=400,null=True)
    habilidades = models.CharField(max_length=400,null=True)
    salario = models.FloatField(default=0,null=True)
    remoto = models.BooleanField(default=False)
    recrutador = models.ForeignKey(User, on_delete=models.CASCADE,related_name='vagas',default=None)
    data_criacao = models.DateTimeField(auto_now_add=True)

class CandidatoVaga(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_candidatura = models.DateTimeField(auto_now_add=True)

    STATUS_OPCOES = [
        ('aplicado', 'Aplicado'),
        ('em_analise', 'Em análise'),
        ('entrevista', 'Entrevista'),
        ('reprovado', 'Reprovado'),
        ('aprovado', 'Aprovado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_OPCOES, default='aplicado')
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('candidato', 'vaga')  # impede o mesmo candidato se candidatar 2x na mesma vaga

    def __str__(self):
        return f"{self.candidato} -> {self}"