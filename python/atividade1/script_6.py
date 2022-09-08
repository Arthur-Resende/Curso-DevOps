# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

# Recebendo e calculando valores
print("Esse programa recebe um número e retorna seu dobro, triplo e sua raiz quadrada\n")
numero = int(input("Escreva um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)

# Escrevendo valores calculados
print("Dobro: " + str(dobro))
print("triplo: " + str(triplo))
print("Raiz quadrada: " + str(raiz_quadrada))
