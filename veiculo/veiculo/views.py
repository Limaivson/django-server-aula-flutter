from django.http import HttpResponse
from .carro_pb import Carro, Motor, Pneu
from .instance import c, m, p, ca

carro = Carro()
motor = Motor()
pneu = Pneu()


def acelerar(request):
    velocidade = str(ca.acelerar())
    motor.velocidade = velocidade
    return HttpResponse(bytes(motor))


def reduzir(request):
    velocidade = str(ca.frear())
    motor.velocidade = velocidade
    return HttpResponse(bytes(motor))


def ligar(request):
    enginicao = ca.ligar()
    motor.ligado = enginicao
    return HttpResponse(bytes(motor))


def desligar(request):
    enginicao = ca.desligar()
    motor.ligado = enginicao
    return HttpResponse(bytes(motor))


def obter_velocidade(request):
    velocidade = str(ca.obter_velocidade())
    motor.velocidade = velocidade
    return HttpResponse(bytes(motor))


def obter_marcha(request):
    marcha = ca.obter_marcha()
    motor.marcha = marcha
    return HttpResponse(bytes(motor))


def obter_estado(request):
    enginicao = ca.motor.obter_estado()
    motor.ligado = enginicao
    return HttpResponse(bytes(motor))


def obter_rotacao_pneu(request):
    rotacao = ca.obter_rotacao_pneu()
    pneu.rotacao = rotacao
    return HttpResponse(pneu.SerializeToString)

def obter_modelo(request):
    modelo = ca.modelo
    carro.modelo = modelo
    return HttpResponse(carro.SerializeToString)

def obter_cor(request):
    cor = ca.cor
    carro.cor = cor
    return HttpResponse(carro.SerializeToString)
