numero = int(input("Digite um número para ver sua tabuada:"))
for i in range(0, 10):
    print("%d x %d = %d" %(numero, (i+1), numero*(i+1)))
