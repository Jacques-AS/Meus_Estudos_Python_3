'''
Desafio 045:
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
import emoji
from time import sleep
print('VAMOS JOGAR JOKENPO !!!')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print(emoji.emojize('''Escolha uma opção:
[ 0 ] - PEDRA :raised_fist: 
[ 1 ] - PAPEL :raised_hand:
[ 2 ] - TESOURA :victory_hand:'''))
jogador = int(input('Digite Qual é a sua JOGADA: '))
print('JO', end=''), sleep(1), print('KEN', end=''), sleep(1), print('PO!!!'), sleep(1)
print('=*=*'*8)
print(f'Computador jogou: {computador}')
print(f'Jogador jogou: {jogador}')
print('=*=*'*8)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(emoji.emojize('''Meus Parabéns JOGADOR
jogou "PAPEL" :raised_hand: e VENCEU'''))
    elif jogador == 2:
        print(emoji.emojize('''Computador jogou "PEDRA" :raised_fist:
e VENCEU, tente novamente !!!'''))
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print(emoji.emojize('''Computador jogou "PAPEL :raised_hand:
e VENCEU, tente novamente !!!'''))
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(emoji.emojize('''Meus Parabéns JOGADOR
jogou "TESOURA" :victory_hand: e VENCEU'''))
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print(emoji.emojize('''Meus Parabéns JOGADOR
jogou "PEDRA" :raised_fist: e VENCEU'''))
    elif jogador == 1:
        print(emoji.emojize('''Computador jogou "TESOURA" :victory_hand:
e VENCEU, tente novamente !!!'''))
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!,    Jogue novamente')
