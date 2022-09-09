# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Precço: "))
desconto = 0.05 # float(input("Desconto: "))/100
print(preco - (preco * desconto))