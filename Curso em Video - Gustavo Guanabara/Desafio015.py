'''
Desafio 015:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.
'''
km_percorrido = float(input('Informe o Km percorrido '))
quant_dias = int(input('Informe a quantidade de dias da locação '))
preco = 60
km = 0.15
preco_dia = preco * quant_dias
preco_kmpercorrido = km_percorrido * km
valor_pagar = preco_dia + preco_kmpercorrido
print('*'*50)
print(f'Veículo percorreu {km_percorrido:.0f} Km\nLocação por {quant_dias} dias\nValor diária de R$ {preco:.2f}\nValor por Km R$ {km}\nCusto total da locação R$ {valor_pagar:.2f}')
print('*'*50)
