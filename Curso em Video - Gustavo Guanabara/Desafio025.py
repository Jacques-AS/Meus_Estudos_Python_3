'''
Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = str(input('Digite seu nome completo: \n')).upper()
nome2 = 'SILVA' in nome
print(f'O seu nome tem SILVA?\n Resposta: {nome2}.')

