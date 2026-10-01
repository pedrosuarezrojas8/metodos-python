
from clases.mago import Mago

merlin = Mago("Merlin" , ["Bola de fuego", "Rayo"])
Gandalf = Mago("Gandalf", ["Bola de fuego", "Invisibilidad"])

print(merlin)
print(len(merlin))

print(Gandalf)
print(len(Gandalf))

print (merlin == Gandalf)