while True:
    try:
        km_percorridos = float(input("Km percorridos: "))
        dias_usados = float(input("Dias em uso: "))
    except:
        print("Insira um valor numério")
        continue
    break

preco = (60 * dias_usados) + (0.15 * km_percorridos)
print(preco)