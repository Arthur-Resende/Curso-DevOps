nome = input("Nome: ").upper().strip()

if nome.find("SILVA") != -1:
    print("Seu nome tem Silva")
    nome_destacado = []
    for i in range(0, len(nome)):
        if i >= nome.find("SILVA") and i < nome.find("SILVA") + 5:
            nome_destacado.append(nome[i])
        else:
            nome_destacado.append(nome.lower()[i])
    print("\n" + "".join(nome_destacado) + "\n")
else:
    print("Seu nome não tem Silva")