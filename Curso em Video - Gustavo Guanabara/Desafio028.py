'''
Desafio 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
maquina = randint(0,10) #faz o computador "PENSAR"
'''
print ('*'*60)
print ('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print ('.'*60)
jogador = int(input('Em que número eu pensei???')) #Jogador tentar advinhar
if jogador == maquina:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print(f'GANHEI! Eu pensei no número {maquina} e não {jogador}')
