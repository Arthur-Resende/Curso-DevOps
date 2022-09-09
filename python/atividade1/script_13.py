# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Salario: "))
aumento = 0.15 # (float(input("Aumento: "))/100)
print(salario + (salario * aumento))