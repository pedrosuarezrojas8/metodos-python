class Mago:
    #metodo especial CONSTRUCTOR
    def __init__(self, nombre, hechizos = None):
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else []

    #metodo especial TO STRING

    def __str__(self):
        return f"Hola mi nombre es {self.nombre}, el mago"

    def __len__(self):
        return len(self.hechizos)

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos