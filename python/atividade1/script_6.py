import math

# Recebendo e calculando valores
print("Esse programa recebe um número e retorna seu dobro, triplo e sua raiz quadrada\n")
numero = int(input("Escreva um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)

# Escrevendo valores calculados
print("Dobro: %d" %dobro)
print("triplo: %d" %triplo)
print("Raiz quadrada: %5.2f" %raiz_quadrada)
