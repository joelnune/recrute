from django.contrib.auth.models import User
from recrutamento.models import Candidato, Recrutador

class UserService:

    @staticmethod
    def create_candidato(user, cpf, cargo,email,):

        candidato = Candidato.objects.create(
            user=user,
            cpf=cpf,
            cargo=cargo,
            email=email,
        )
        return candidato

    @staticmethod
    def create_recrutador(user,nome, cargo, nome_empresa, cnpj):

        recrutador = Recrutador.objects.create(
            user=user,
            nome=nome,
            cargo=cargo,
            nome_empresa=nome_empresa,
            cnpj=cnpj,
        )
        return recrutador
