# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. (utilize o método math.trunc() para realizar este exercício).
import math

num_real = float(input("Número real: "))
num_inteiro = math.trunc(num_real)
print(num_inteiro)