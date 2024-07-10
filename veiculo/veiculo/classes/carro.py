from abc import ABC
from typing import List
from .veiculo import Veiculo
from .motor import Motor
from .pneu import Pneu


class Carro(Veiculo, ABC):
    def __init__(self, modelo, cor, motor: Motor, pneus: List[Pneu]):
        super().__init__(motor, pneus)
        self.modelo = modelo
        self.cor = cor
        self.motor = motor
        self.pneus = pneus

    def __str__(self):
        return f'Carro {self.modelo} de cor {self.cor}'

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.reduzir()

    def ligar(self):
        return self.motor.ligar()

    def desligar(self):
        return self.motor.desligar()

    def obter_velocidade(self):
        return self.motor.obter_aceleracao()

    def obter_marcha(self):
        return self.motor.obter_marcha()

    def obter_rotacao_pneu(self):
        return self.pneus[0].rotacoes

    def atualizar_rotacao_pneu(self):
        super().atualizar_rotacao_pneu()
