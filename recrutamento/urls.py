from django.urls import path

from . import views

app_name = 'recrutamento'
urlpatterns = [
    path("", views.index, name="recrutador_vagas_home"),
    path("recrutador/vagas/", views.recrutador_vagas_home, name="recrutador_vagas_home"),
    path("recrutador/criar/", views.recrutador_vagas_criar, name="recrutador_vagas_criar"),
    path("recrutador/remover/<int:id>", views.recrutador_vagas_remover, name="recrutador_vagas_remover"),
    path("recrutador/editar/<int:id>", views.recrutador_vagas_editar, name="recrutador_vagas_editar"),


    path("candidato/vagas/", views.candidato_vagas_home, name="candidato_vagas_home"),
    path("candidato/vagas/<int:id>", views.candidato_visualizar_vaga, name="candidato_visualizar_vaga"),
    path("candidato/vagas/efetuar_candidatura/<int:id>", views.efetuar_candidatura, name="efetuar_candidatura"),
    path("candidato/vagas_aplicadas", views.visualizar_vagas_aplicadas, name="visualizar_vagas_aplicadas"),
path("candidato/vagas_aplicadas/cancelar/<int:id>", views.cancelar_aplicacao, name="cancelar_aplicacao"),

]
