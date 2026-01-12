from django import forms
from recrutamento.models import Recrutador,Candidato
from django.contrib.auth.models import User
class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'cpf', 'email','cargo' ]


class RecrutadorForm(forms.ModelForm):
    class Meta:
        model = Recrutador
        fields = ['nome','cargo','cnpj','nome_empresa']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username': 'E-mail',
        }