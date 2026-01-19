from django import forms
from .models import Vaga,Candidato

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao','salario','remoto']
