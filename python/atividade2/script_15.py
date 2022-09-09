# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_percorridos = float(input("Km percorridos: "))
dias_usados = float(input("Dias em uso: "))
preco = (60 * dias_usados) + (0.15 * km_percorridos)
print(preco)