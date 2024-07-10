from motor import Motor
from pneu import Pneu
from cambio import Cambio
from carro import Carro


if __name__ == '__main__':
    cambio = Cambio()
    motor = Motor(200, cambio)
    lista_pneus = [Pneu(205, 55) for _ in range(4)]
    carro = Carro('Fusca', 'Azul', motor, lista_pneus)
    print(carro.ligar())
    print(carro.acelerar())
    print(carro.acelerar())
    print(carro.acelerar())
    print(f'Rotações: {carro.obter_rotacao_pneu()}')
    print(carro.obter_velocidade())
    print(carro.obter_marcha())
    print(carro.frear())
    print(carro.desligar())
    print(carro)
