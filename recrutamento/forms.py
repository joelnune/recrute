from django import forms
from .models import Vaga

class RecrutadorForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao','salario']