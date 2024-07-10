from abc import ABC, abstractmethod
from typing import List
from .pneu import Pneu
from .motor import Motor


class Veiculo(ABC):
    def __init__(self, motor: Motor, rodas: List[Pneu]):
        self.motor = motor
        self.rodas = rodas

    @abstractmethod
    def acelerar(self):
        self.motor.acelerar()
        self.atualizar_rotacao_pneu()

    @abstractmethod
    def frear(self):
        self.motor.reduzir()
        self.atualizar_rotacao_pneu()

    @abstractmethod
    def ligar(self):
        self.motor.ligar()

    @abstractmethod
    def desligar(self):
        self.motor.desligar()

    @abstractmethod
    def obter_velocidade(self):
        return self.motor.obter_aceleracao()//100

    @abstractmethod
    def obter_marcha(self):
        return self.motor.obter_marcha()

    @abstractmethod
    def atualizar_rotacao_pneu(self):
        for pneu in self.rodas:
            pneu.atualiza_rotacoes(self.motor.obter_forca()*self.motor.obter_marcha()*200)/pneu.tamanho

    @abstractmethod
    def __str__(self):
        pass
