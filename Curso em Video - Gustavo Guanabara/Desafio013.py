'''
Desafio 013:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
n1 = float(input('Salário do Funcionário: R$ '))
aumento = n1 * 0.15
salario = n1 + aumento
print(f'Salário do funcionário: R$ {n1:.2f}\nAumento de 15% salário: R$ {aumento:.2f} \nSalário Ajustado: R$ {salario:.2f}')
