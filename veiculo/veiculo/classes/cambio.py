class Cambio:
    def __init__(self, marcha_atual=0):
        self.marcha_atual = marcha_atual

    def atualizar_marcha(self, aceleracao):
        if aceleracao < 0:
            self.marcha_atual -= 1

        elif 0 < aceleracao <= 25:
            self.marcha_atual = 1

        elif 25 < aceleracao <= 50:
            self.marcha_atual = 2

        elif 50 < aceleracao <= 75:
            self.marcha_atual = 3

        elif 75 < aceleracao <= 100:
            self.marcha_atual = 4

        elif 100 < aceleracao <= 200:
            self.marcha_atual = 5

        return self.marcha_atual
