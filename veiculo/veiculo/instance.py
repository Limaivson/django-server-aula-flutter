from .classes.motor import Motor
from .classes.carro import Carro
from .classes.cambio import Cambio
from .classes.pneu import Pneu

c = Cambio()
m = Motor(200, c)
p = [Pneu(205, 55) for _ in range(4)]
ca = Carro('fusca', 'azul', m, p)
