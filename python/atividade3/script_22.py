nome_completo = input("Nome completo: ")
nome_partes = nome_completo.split()
nome_sem_espacos = "".join(nome_partes)

print("\nnome maiúsculo: " + nome_completo.upper())
print("nome minúsculo: " + nome_completo.lower())
print("Quantidade de letras total: %d" %len(nome_sem_espacos))
print("Quantidade de letras do primeiro nome: %d" %len(nome_partes[0]))