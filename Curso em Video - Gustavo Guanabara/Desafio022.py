'''
Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome_completo = input('Digite seu Nome Completo: ')
print(f'Seu nome completo é : {nome_completo}')
print(f'Seu nome em maiúsculas: {nome_completo.upper()}')
print(f'Seu nome em minúsculas: {nome_completo.lower()}')
nome = nome_completo.split()
print(f'Quantidade de letras no nome sem espaços é: {len("".join(nome))}')
print(f'Quantidade de letras tem o primeiro nome é: {len(nome[0])}')