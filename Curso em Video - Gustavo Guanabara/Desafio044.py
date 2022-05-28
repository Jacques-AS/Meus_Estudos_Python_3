'''
Desafio 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
•	À vista dinheiro/ cheque: 10% de desconto
•	À vista no cartão: 5% de desconto
•	Em até 2x no cartão: preço normal
•	3x ou mais no cartão: 20% de juros
'''
print(f'{" Black One Tec ":*^30}')
produto = float(input('Digite o Valor do Produto R$ '))
print('Digite um número correspondente a FORMA DE PAGAMENTO')
print('[ 1 ] À vista dinheiro/ cheque: 10% de desconto\n[ 2 ] À vista no cartão: 5% de desconto\n[ 3 ] Em até 2x no cartão: preço normal\n[ 4 ] 3x ou mais no cartão: 20% de juros')
opcao = int(input('Escolha sua OPÇÃO DE PAGAMENTO: '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    total_parcela = int(input('Digite em Quantas PARCELAS: '))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    total_parcela = int(input('Digite em Quantas PARCELAS: '))
    valor_parcelas = total / total_parcela
    print(f'Sua Compra foi Parcelada em {total_parcela}x, Valor para Cada Parcela R$ {valor_parcelas:.2f}')
else:
    total = 0
    print('Opção INVÁLIDA DE PAGAMENTO, tente NOVAMENTE!')

print(f'Valor da Compra R$ {produto:.2f}, Valor Total do Pagamento R$ {total:.2f}')
