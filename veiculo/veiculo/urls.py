from django.urls import path
from .views import *

urlpatterns = [
    path('acelerar/', acelerar),
    path('reduzir/', reduzir),
    path('ligar/', ligar),
    path('desligar/', desligar),
    path('obter_velocidade/', obter_velocidade),
    path('obter_marcha/', obter_marcha),
    path('obter_estado/', obter_estado),
    path('obter_rotacao_pneu/', obter_rotacao_pneu),
]
