class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular #Usando __ hacemos privado el atributo
        self.__saldo = saldo_inicial


#SETTER (EDITOR CONFIGURADOR)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de ${cantidad} pesos")
        else:
            print("La cantidad a depositar debe ser mayor a Zero")


    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado $ {cantidad} exitosamente")
        else:
            print("Fondos insuficientes")
            
#GETTER (OBTENER INFORMACION PRIVADA A TRAVES DE UN METODO PUBLICO) 

    def obtener_saldo(self):
        return f"El saldo actual de la cuenta es $ {self.__saldo}"