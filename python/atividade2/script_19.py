import random

lista_alunos = []
for i in range (0, 4):
    lista_alunos.append(input("Nome aluno: ").capitalize())

aluno_escolhido = random.choice(lista_alunos)
print("\nO aluno escolhido é: %s" % aluno_escolhido)