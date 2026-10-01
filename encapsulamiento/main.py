from clases.cuenta_bancaria import CuentaBancaria

#creamos instancia
cuenta = CuentaBancaria("Pedro", 1000)

cuenta.__titular = "Ricardo"
cuenta.__saldo = 10000


#obtener saldo inicial
print(cuenta.obtener_saldo())

#depositar 500 y mostrar saldo parcial
cuenta.depositar(500)
print(cuenta.obtener_saldo())

#retirar 750 y mostrar saldo parcial
cuenta.retirar(750)
print(cuenta.obtener_saldo())