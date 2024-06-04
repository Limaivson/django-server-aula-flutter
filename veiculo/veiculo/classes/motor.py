from .cambio import Cambio


class Motor:
    def __init__(self, potencia, cambio: Cambio, ligado=False, aceleracao=0):
        self.potencia = potencia
        self.cambio = cambio
        self.ligado = ligado
        self.aceleracao = aceleracao

    def ligar(self):
        if self.ligado:
            return 'Atenção: Motor já está ligado'
        else:
            self.ligado = True
            return self.ligado

    def desligar(self):
        if not self.ligado:
            return 'Atenção: Motor já está desligado'
        else:
            self.ligado = False
            return self.ligado

    def acelerar(self):
        if self.ligado:
            if self.aceleracao >= 200:
                return 'Atenção: Aceleração máxima atingida'
            else:
                self.aceleracao += 10
                self.cambio.atualizar_marcha(self.aceleracao)
                return self.aceleracao
        else:
            return 'Atenção: Motor desligado'

    def reduzir(self):
        if self.ligado:
            if self.aceleracao <= -50:
                return 'Atenção: Velocidade máxima da ré atingida'
            else:
                self.aceleracao -= 10
                self.cambio.atualizar_marcha(self.aceleracao)
                return self.aceleracao
        else:
            return 'Atenção: Motor desligado'

    def obter_estado(self):
        return self.ligado

    def obter_aceleracao(self):
        return self.aceleracao

    def obter_marcha(self):
        return self.cambio.marcha_atual

    def obter_potencia(self):
        return self.potencia

    def obter_forca(self):
        return self.potencia*self.aceleracao
