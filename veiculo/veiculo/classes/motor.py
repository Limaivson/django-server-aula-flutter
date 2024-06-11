from .cambio import Cambio


class Motor:
    def __init__(self, potencia, cambio: Cambio, ligado=False, aceleracao=0):
        self.potencia = potencia
        self.cambio = cambio
        self.ligado = ligado
        self.aceleracao = aceleracao

    def ligar(self):
        if self.ligado:
            return True
        else:
            self.ligado = True
            self.aceleracao = 0
            return self.ligado

    def desligar(self):
        if not self.ligado:
            return False
        else:
            self.ligado = False
            self.aceleracao = 0
            return self.ligado

    def acelerar(self):
        if self.ligado:
            if self.aceleracao >= 200:
                return self.aceleracao
            else:
                self.aceleracao += 10
                self.cambio.atualizar_marcha(self.aceleracao)
                return self.aceleracao
        else:
            return self.aceleracao

    def reduzir(self):
        if self.ligado:
            if self.aceleracao <= -50:
                return self.aceleracao
            else:
                self.aceleracao -= 10
                self.cambio.atualizar_marcha(self.aceleracao)
                return self.aceleracao
        else:
            return self.aceleracao

    def obter_estado(self):
        return self.ligado

    def obter_aceleracao(self):
        return self.aceleracao

    def obter_marcha(self):
        return self.cambio.get_marca_atual()

    def obter_potencia(self):
        return self.potencia

    def obter_forca(self):
        return self.potencia*self.aceleracao
