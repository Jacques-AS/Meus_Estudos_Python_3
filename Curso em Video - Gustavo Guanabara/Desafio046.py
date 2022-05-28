'''
Desafio 046:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios,
indo de da até 0, com uma pausa de um segundo entre eles.
'''
import emoji
from time import sleep
for c in range (3,0, -1):
    sleep(1)
    print(c)
print('Poooooollll \U0001F386 \U0001F386 \U0001F386 \U0001F386 \U0001F386')
