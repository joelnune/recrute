from django.db import models

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    salario = models.FloatField(default=0)


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

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
        return f"{self.candidato} -> {self.vaga}"