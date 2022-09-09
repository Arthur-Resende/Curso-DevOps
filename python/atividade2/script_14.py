while True:
    try:
        celsius = float(input("Temperatura em ˚C: "))
    except:
        print("Insira um valor numério")
        continue
    break

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)