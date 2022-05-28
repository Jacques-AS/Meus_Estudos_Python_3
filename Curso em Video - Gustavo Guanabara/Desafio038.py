'''
Desafio 038:
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
•	O primeiro valor é maior
•	O segundo valor maior
•	Não existe valor maior, os dois são iguais
'''
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print(f'{num1}, o primeiro valor Maior.')
elif num1 < num2:
    print(f'{num2}, o segundo valor Maior.')
else:
    print('Não existe valor maior, os dois são iguais.')