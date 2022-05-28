'''
Desafio 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = int(input('Digite um ângulo: '))
print('=*='*13)
print(f'O ângulo de {angulo} é:')
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print(f'Seno = {seno:.2f}\nCosseno = {cosseno:.2f}\nTangente = {tangente:.2f}')
print('=*='*13)
