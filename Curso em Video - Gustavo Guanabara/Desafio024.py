'''
Desafio 024
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
cidade = str(input('Em que cidade você nasceu? \n')).upper()
cidade2 = 'SANTO' in cidade
print(f'A cidade começa com SANTO?\n Resposta: {cidade2}.')