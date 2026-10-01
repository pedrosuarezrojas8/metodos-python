
from clases.villano import Villano
from clases.heroe import Heroe

superman = Heroe("Superman", 100, "volar")
joker = Villano("Joker", 80, "engañar")

superman.saludar()
superman.mostrar_salud()
superman.mostrar_poder()

joker.saludar()
joker.mostrar_salud()
joker.mostrar_poder()


