# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

lista_alunos = []
for i in range (0, 4):
    lista_alunos.append(input("Nome aluno: "))

aluno_escolhido = random.choice(lista_alunos)
print("O aluno escolhido é: %s" % aluno_escolhido)