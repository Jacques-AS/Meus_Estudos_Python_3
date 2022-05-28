'''
Desafio 009:
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
#ModeloVer. 01
num = int(input('Digite um número para tabuada de Multiplicação: '))
print(f'{num} x {0:2} = {num*0:2}')
print(f'{num} x {1:2} = {num*1:2}')
print(f'{num} x {2:2} = {num*2:2}')
print(f'{num} x {3:2} = {num*3:2}')
print(f'{num} x {4:2} = {num*4:2}')
print(f'{num} x {5:2} = {num*5:2}')
print(f'{num} x {6:2} = {num*6:2}')
print(f'{num} x {7:2} = {num*7:2}')
print(f'{num} x {8:2} = {num*8:2}')
print(f'{num} x {9:2} = {num*9:2}')
print(f'{num} x {10:2} = {num*10:2}')


#Modelo Ver. 2
num = int(input('Digite um número para  ver a sua tabuada: '))
for contador in range(1, 11):
    print(f'{num:2} x {contador:2} = {num* contador:2}')

#Modelo Ver. 3
while True:
    num = int(input('Digite um número para  ver a sua tabuada: '))
    if num < 0:
        break
for contador in range(1, 11):
    print(f'{num:2} x {contador:2} = {num* contador:2}')
print(f'PROGRAMA TABUADA ENCERRADO, Volte sempre!')


#Modelo Ver. 4
print('TABUADA DE 1 A 10:')
operacao = str(input('Escolha Uma Operação Aritmética ( +  -  *  / ): '))

if operacao == '+':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} + {coluna2:2} = {coluna1+coluna2:2}')

elif operacao == '-':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} - {coluna2:2} = {coluna1-coluna2:2}')

elif operacao == '*':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} x {coluna2:2} = {coluna1*coluna2:2}')

elif operacao == '/':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} / {coluna2:2} = {coluna1/coluna2:.2f}')
else:
    print('Operação inválida, por favor escolha uma das opções informadas')

