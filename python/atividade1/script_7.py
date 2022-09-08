print("Esse programa recebe as notas de um aluno e retorna a média calculada./n")

# Declarando variáveis
falta_notas = True
nota_total = 0
contador = 0
media = 0

# Recebe notas e verifica se ainda falta notas para receber
while falta_notas == True:
    nota = int(input("Nota recebida: "))
    nota_total = nota_total + nota
    contador += 1

    # verifica se ainda é necessário adicionar mais notas
    if input("Ainda falta nota? s/n\n") == 'n':
        falta_notas = False
    else:
        falta_notas  = True

# Calcula média e a imprime
media = nota_total/contador
print("A média das notas é: %.2f" %media)
