'''
Desafio 019
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''
import random
a1 = input('Nome do 1° aluno: ')
a2 = input('Nome do 2° aluno: ')
a3 = input('Nome do 3° aluno: ')
a4 = input('Nome do 4° aluno: ')
alunos = a1,a2,a3,a4
escolhido = random.choices(alunos)
print(f'O nome dos quatro alunos sorteados foram: {a1}, {a2}, {a3} e {a4}.\nE o sorteado é:{escolhido}')
