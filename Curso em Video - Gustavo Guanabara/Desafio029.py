'''
Desafio 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 cada Km acima do limite.
'''
velocidade = float(input('Digite Velocidade do Veículo: '))
if velocidade > 80:
    print('Você será MULTADO por excesso de velocidade, limite de 80Km/h.')
    multa = (velocidade - 80) * 7
    print (f'Você pagará uma MULTA no valor de R$ {multa:.2f}')

print('Dirija com SEGURANÇA ! Ótima viagem.')
