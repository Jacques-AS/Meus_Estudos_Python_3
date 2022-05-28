'''
Desafio 012:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
n1 = int(input('Preço do Produto: R$ '))
desc = n1 * 0.05
prod = n1 - desc
print(f'Preço do Produto R$ {n1:.2f} \n 5% de desconto R$ {desc:.2f} \n Valor do Produto com Desconto R$ {prod:.2f}')


