from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

path('cadastro/', views.cadastro, name='cadastro'),

    path('cadastrar/candidato/', views.cadastrar_candidato, name='cadastrar_candidato'),
    path('cadastrar/recrutador/', views.cadastrar_recrutador, name='cadastrar_recrutador'),
]
