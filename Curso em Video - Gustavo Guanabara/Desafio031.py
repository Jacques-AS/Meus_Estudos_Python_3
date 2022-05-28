'''
Desafio 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200 Km e R$ 0.45 para viagens mais longas.
'''
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
