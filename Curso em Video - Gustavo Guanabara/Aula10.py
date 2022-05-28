'''Desafio 028:
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

rom random import randint
maquina = randint(0,10) #faz o computador "PENSAR"
print ('*'*60)
print ('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print ('.'*60)
jogador = int(input('Em que número eu pensei???')) #Jogador tentar advinhar
if jogador == maquina:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print(f'GANHEI! Eu pensei no número {maquina} e não {jogador}')

'''Desafio 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$ 7.00 cada Km acima do limite.'''

velocidade = float(input('Digite Velocidade do Veículo: '))
if velocidade > 80:
    print('Você será MULTADO por excesso de velocidade, limite de 80Km/h.')
    multa = (velocidade - 80) * 7
    print (f'Você pagará uma MULTA no valor de R$ {multa:.2f}')

print('Dirija com SEGURANÇA ! Ótima viagem.')

'''Desafio 030:
Crie um programa que leia um número inteiro e mostre na tela se
é PAR ou ÍMPAR.'''

num = int(input('Digite um número: '))
res = num % 2
if res == 0:
    print(f'O número {num} que você digitou é PAR.')
else:
    print(f'O número {num} que você digitou é ÍMPAR.')

'''Desafio 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens
até 200 Km e R$ 0.45 para viagens mais longas.'''

distancia = float(input('Qual a distância você irá viajar em Km ? '))
valor1 = distancia * 0.50
valor2 = distancia * 0.45
if distancia <= 200:
    print(f'Em uma viagem de {distancia} Km\nO valor da viagem será de R$ 0.50 por Km\nTotal a pagar pela viagem R$ {valor1:.2f}')

else:
    print(f'Em uma viagem de {distancia} Km\nO valor da viagem será de R$ 0.45 por Km\nTotal a pagar pela viagem R$ {valor2:.2f}')

print('*'*40)
print('Muito obrigado, tenha uma ÓTIMA viagem.')
print('*'*40)


'''Desafio 032:
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para o ano ATUAL: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')

else:
    print(f'O ano de {ano} NÃO É BISSEXTO')

'''Desafio 033:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

valor1 = int(input('Digite PRIMEIRO valor: '))
valor2 = int(input('Digite SEGUNDO valor: '))
valor3 = int(input('Digite TERCEIRO valor: '))

menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2

if valor3 < valor1 and valor3 < valor2:
    menor = valor3

maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2

if valor3 > valor1 and valor3 > valor2:
    maior = valor3

print('*'*30)
print(f'O MENOR valor digitado fo {menor}')
print(f'O MAIOR valor digitado fo {maior}')
print('*'*30)

'''Desafio 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento.
Para salários superiores R$ 1.250,00 calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Salário do Funcionário R$ '))
if salario <= 1250:
    salario_superior = salario + (salario * 15 / 100)
    print(f'Seu salário R$ {salario:.2f} teve um reajuste de 15% para R$ {salario_superior:.2f}')
else:
    salario_inferior = salario + (salario * 10 /100)
    print(f'Seu salário R$ {salario:.2f} teve um reajuste de 10% para R$ {salario_inferior:.2f}')


'''Desafio 035:
Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('tercerio segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segumentos acima PODEM FORMAR triângulo')

else:
    print('Os segumentos acima NÃO PODEM FORMAR triângulo')