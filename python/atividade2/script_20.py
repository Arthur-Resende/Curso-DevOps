import random

lista_alunos = []
for i in range (0, 4):
    lista_alunos.append(input("Nome aluno: ").capitalize())

random.shuffle(lista_alunos)
for i in range(0, len(lista_alunos)):
    print("%d˚ %s" %(i+1, lista_alunos[i]))