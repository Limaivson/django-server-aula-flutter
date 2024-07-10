class Pneu:
    def __init__(self, largura, raio):
        self.largura = largura
        self.raio = raio
        self.rotacoes = 0

    def atualiza_rotacoes(self, rotacoes):
        self.rotacoes = rotacoes
        return self.rotacoes

    def tamanho(self):
        return (self.largura*self.raio)//10
