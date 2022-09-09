# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Salario: "))
# aumento = 1.15
# print(salario * aumento)
# 
# Resultado = 114.99999999999999
# 
# Computador armazena números decimais em binários, mas alguns numeros se tornam dízimas periódicas em binário
# Ao tentar armazenar numeros com agarísmos infinitos em uma quantidade finita de dados, alguns valores são perdidos
# Esses valores se acumulam e podem resultar em perda ou ganho de dados
# Efeito pode ser reproduzido também com 0.1 + 0.2 = 0.30000000000000004
# Mais informações https://news.ycombinator.com/item?id=3361083

aumento = 0.15 # (float(input("Aumento: "))/100)
print(salario + (salario * aumento))