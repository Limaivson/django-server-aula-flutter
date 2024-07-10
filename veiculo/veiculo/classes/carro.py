from typing import List
from .veiculo import Veiculo
from .motor import Motor
from .pneu import Pneu


class Carro(Veiculo):
    def __init__(self, modelo, cor, motor: Motor, pneus: List[Pneu]):
        super().__init__(motor, pneus)
        self.modelo = modelo
        self.cor = cor
        # self.motor = motor
        # self.pneus = pneus

    def __str__(self):
        return f'Carro {self.modelo} de cor {self.cor}'

    def acelerar(self):
        super().acelerar()

    def frear(self):
        super().frear()

    def ligar(self):
        super().ligar()

    def desligar(self):
        super().desligar()

    def obter_velocidade(self):
        return super().obter_velocidade()

    def obter_marcha(self):
        return super().obter_marcha()

    def obter_rotacao_pneu(self):
        return self.rodas[0].rotacoes


    def atualizar_rotacao_pneu(self):
        super().atualizar_rotacao_pneu()
