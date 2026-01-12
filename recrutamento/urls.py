from django.urls import path

from . import views

app_name = 'recrutamento'
urlpatterns = [
    path("", views.index, name="recrutador_vagas_home"),
    path("recrutador/vagas/", views.recrutador_vagas_home, name="recrutador_vagas_home"),
    path("recrutador/criar/", views.recrutador_vagas_criar, name="recrutador_vagas_criar"),

    path("recrutador/remover/<int:id>", views.recrutador_vagas_remover, name="recrutador_vagas_remover"),

    path("recrutador/editar/<int:id>", views.recrutador_vagas_editar, name="recrutador_vagas_editar"),


]
