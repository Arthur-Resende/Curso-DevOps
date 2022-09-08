# Faça um programa que leia um númeor inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input("Digite um número para ver sua tabuada:"))
contador = 1
while contador <= 10:
    print("%d x %d = %d" % (numero, contador, numero*contador))
    contador = contador + 1
