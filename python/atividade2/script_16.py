import math

while True:
    try:
        num_real = float(input("Número real: "))
    except:
        print("Insira um valor numério")
        continue
    break

num_inteiro = math.trunc(num_real)
print(num_inteiro)