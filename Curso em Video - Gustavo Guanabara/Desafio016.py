'''
Desafio 016
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6
'''
import math
n = float(input('Digite um número: '))
porcao_inteira = math.trunc(n)
print(f'Número inteiro {n} e sua porção inteira do número é: {porcao_inteira}')
