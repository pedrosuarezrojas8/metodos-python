
from clases.perro import Perro
from clases.gato import Gato
from clases.vaca import Vaca


def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")


perro = Perro("Firulais")
gato = Gato("Pelusa")
vaca = Vaca("Lechera")

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(gato)
hacer_sonido_de_animal(vaca)