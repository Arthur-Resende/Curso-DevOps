while True:
    try:
        preco = float(input("Preço: "))
    except:
        print("Insira um valor numério")
        continue
    break

desconto = 0.05 # float(input("Desconto: "))/100
print(preco - (preco * desconto))