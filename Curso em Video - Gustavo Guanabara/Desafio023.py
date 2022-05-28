'''
Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''
numero = input('Digite um número de 0 a 9999: ')
num = numero
extensao = len(num)
print(f'Unidade:{num[extensao-1]}')
print(f'Dezena: {num[extensao-2]}')
print(f'Centena: {num[extensao-3]}')
print(f'Milhar: {num[extensao-4]}')
