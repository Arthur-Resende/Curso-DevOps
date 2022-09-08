print("Esse programa recebe as notas de um aluno e retorna a média calculada./n")

# Declarando variáveis
falta_notas = True
nota_total = 0
quantidade_notas = 0
media = 0

# Recebe notas e verifica se ainda falta notas para receber
while falta_notas == True:
    nota = int(input("Nota recebida: "))
    nota_total = nota_total + nota
    quantidade_notas = quantidade_notas + 1
    falta_notas = input("Ainda falta nota? s/n\n")
    if falta_notas == "n":
        falta_notas = False
    else:
        falta_notas  = True

# Calcula média e a imprime
media = nota_total/quantidade_notas
print("A média das notas é: " + str(media))
