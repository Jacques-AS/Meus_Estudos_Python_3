'''Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome_completo = input('Digite seu Nome Completo: ')
print(f'Seu nome completo é : {nome_completo}')
print(f'Seu nome em maiúsculas: {nome_completo.upper()}')
print(f'Seu nome em minúsculas: {nome_completo.lower()}')
nome = nome_completo.split()
print(f'Quantidade de letras no nome sem espaços é: {len("".join(nome))}')
print(f'Quantidade de letras tem o primeiro nome é: {len(nome[0])}')

'''Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

numero = input('Digite um número de 0 a 9999: ')
num = numero
extensao = len(num)
print(f'Unidade:{num[extensao-1]}')
print(f'Dezena: {num[extensao-2]}')
print(f'Centena: {num[extensao-3]}')
print(f'Milhar: {num[extensao-4]}')

'''Desafio 024
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Em que cidade você nasceu? \n')).upper()
cidade2 = 'SANTO' in cidade
print(f'A cidade começa com SANTO?\n Resposta: {cidade2}.')

'''Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Digite seu nome completo: \n')).upper()
nome2 = 'SILVA' in nome
print(f'O seu nome tem SILVA?\n Resposta: {nome2}.')

'''Desafio 026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase:\n')).upper()
print(f'Quanta vezes apareceu a letra "A" \n Resposta: {frase.count("A")} vezes')
print(f'Letra "A" aparece primeira vez na posição.\n Resposta: {frase.find("A")}')
print(f'Letra "A" aparece última vez na posição.\n Resposta: {frase.rfind("A")}')


'''Desafio 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = input('Digite seu nome completo: \n') .upper()
nome = nome.split()
print(f'O primeiro nome é {nome[0]} \nO último nome é {nome[-1]}')
