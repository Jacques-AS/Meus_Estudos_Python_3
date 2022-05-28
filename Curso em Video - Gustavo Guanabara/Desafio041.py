'''
Desafio 041:
A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
•	Até 9 anos: MIRIM
•	Até 14 anos: INFANTIL
•	Até 19 anos: JUNIOR
•	Até 20 anos: SÊNIOR
•	Acima: MASTER
'''
from datetime import date
ano = date.today().year
ano_nasc_atleta = int(input("Digite o ANO DE NASCIMENTO: "))
classif = ano - ano_nasc_atleta
if classif <= 9:
    print(f'Atleta tem {classif} anos de idade, sua Categoria é MIRIM !')
elif classif <= 14:
    print(f'Atleta tem {classif} anos de idade, sua Categoria é INFANTIL !')
elif classif <= 19:
    print(f'Atleta tem {classif} anos de idade, sua Categoria é JÚNIOR !')
elif classif <= 20:
    print(f'Atleta tem {classif} anos de idade, sua Categoria é SÊNIOR !')
else:
    print(f'Atleta tem {classif} anos de idade, sua Categoria é MASTER !')
