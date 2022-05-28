'''
Desafio 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''
from time import sleep
print('-='*20)
print('\033[33mANÁLISE DE APROVAÇÃO DE EMPRÉSTIMOS\033[m')
print('-='*20)
nome = str(input('Digite seu NOME: '))
emprestimo = float(input('Digite o valor da CASA para o EMPRÉSTIMO R$ '))
salario = float(input('Digite seu SALÁRIO bruto R$ '))
anos = int(input('Em quantos anos deseja o FINANCIAMENTO: '))
prestacao = emprestimo / (anos * 12)
meses = anos * 12
minsal = salario * 30 / 100
print()
print('\033[33mPROCESSANDO SOLICITAÇÃO........\033[m')
print()
sleep(3)
print('*'*65)
if prestacao <= minsal:
    print(f'PARABÉNS, Empréstimo \033[1:32mAPROVADO \033[m!!!')
    print(f'Boa sorte e aproveite seu novo IMÓVEL Sr. {nome}.')
else:
    print(f'Sr. {nome} infelizmente o seu financiamento foi, \033[1:31mNEGADO \033[m!!!\n'
          f'O valor da parcela ultrapassa o limite máximo de 30% sobre o seu salário')
sleep(3)
print('*'*65)
print()
print('\033[33m*** ANALISE DA PROPOSTA ***\033[m')
print()
print(f'Para pagar um Empréstimo R$ {emprestimo:.2f} em {anos} Ano(s)\nSua Prestação MENSAL ficaria em R$ {prestacao:.2f} de {meses} PARCELAS\nSeu Salário R$ {salario:.2f}\nSeu Salário Equivalante a 30% R$ {minsal:.2f}')
