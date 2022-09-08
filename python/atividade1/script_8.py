# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print("Esse programa recebe valores em metro e retorna o valor em centímetros e milímetros calculados.\n")
metros = int(input("Escreva um valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(str(metros) + " metros é igual a:\n" + str(centimetros) + "cm\n" + str(milimetros) + "mm")
