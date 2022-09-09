# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
lista_alunos = []
continua = True
while continua == True:
    lista_alunos.append(input("Nome aluno: "))
    falta_aluno = input("falta aluno? s/n: ")
    if falta_aluno == 's':
        continue
    elif falta_aluno == 'n':
        break