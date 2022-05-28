'''
Desafio 039:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
•	Se ele ainda vai se alistar ao serviço militar.
•	Se é a hora de se alistar
•	Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
atual = date.today().year
nome = str(input('Digite seu Nome: '))
ano_nasc = int(input('Digite o ANO que você nasceu: '))
idade = atual - ano_nasc
alistar = atual - ano_nasc
alistar1 = 18 - alistar
alistar2 = ano_nasc + 18
if alistar < 18:
    saldo = 18 - alistar
    print(f'Sr. {nome} você tem {idade} anos de idade\n'
          f'ainda falta/m {alistar1} anos, estamos em {atual},\npara se alistar ao serviço militar'
          f' é em {alistar2}.\nfalta {saldo} anos.')
elif alistar == 18:
    print(f'Sr. {nome} você tem {idade} anos de idade\n'
          f' está na hora de se alistar ao serviço militar IMEDIATAMENTE')

elif alistar > 18:
    saldo = alistar -18
    print(f'Sr. {nome} já passou do tempo do alistamento,\n seu alistamento era em {alistar2},\n '
          f'por favor procure serviço militar,\n se passaram {saldo} anos.')