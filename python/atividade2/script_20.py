# O mesmo professor do exercício 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

lista_alunos = []
for i in range (0, 4):
    lista_alunos.append(input("Nome aluno: "))

random.shuffle(lista_alunos)
for i in range(0, len(lista_alunos)):
    print("%d˚ %s" %(i+1, lista_alunos[i]))