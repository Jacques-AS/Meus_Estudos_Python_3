'''
Desafio 010:
Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere:
U$$ 1.00 = R$ 3.27
'''
n1=float(input('Dinheiro na Carteira R$ '))
dolar = n1 / 3.27
print(f'Dinheiro na carteira R$ {n1:.2f} em Dólares U$$ {dolar:.2f}')
