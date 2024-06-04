from .classes.motor import Motor
from .classes.pneu import Pneu
from .classes.cambio import Cambio
from .classes.carro import Carro
from django.http import HttpResponse

cambio = Cambio()
motor = Motor(200, cambio)
lista_pneus = [Pneu(205, 55) for _ in range(4)]
carro = Carro('Fusca', 'Azul', motor, lista_pneus)


def acelerar(request):
    velocidade = carro.acelerar()
    return HttpResponse(velocidade)


def reduzir(request):
    velocidade = carro.frear()
    return HttpResponse(velocidade)


def ligar(request):
    enginicao = carro.ligar()
    return HttpResponse('ligado' if enginicao else 'desligado')


def desligar(request):
    enginicao = carro.desligar()
    return HttpResponse(enginicao)


def obter_velocidade(request):
    velocidade = carro.obter_velocidade()
    return HttpResponse(velocidade)


def obter_marcha(request):
    marcha = carro.obter_marcha()
    return HttpResponse(marcha)


def obter_estado(request):
    enginicao = carro.motor.obter_estado()
    print(enginicao)
    return HttpResponse('ligado' if enginicao else 'desligado')


def obter_rotacao_pneu(request):
    rotacao = carro.obter_rotacao_pneu()
    return HttpResponse(rotacao)
