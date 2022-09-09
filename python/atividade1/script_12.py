# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem do desconto: "))/100
preco_final = preco - (preco * desconto)
print(preco_final)