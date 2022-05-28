'''
Desafio 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores R$ 1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Salário do Funcionário R$ '))
if salario <= 1250:
    salario_superior = salario + (salario * 15 / 100)
    print(f'Seu salário R$ {salario:.2f} teve um reajuste de 15% para R$ {salario_superior:.2f}')
else:
    salario_inferior = salario + (salario * 10 /100)
    print(f'Seu salário R$ {salario:.2f} teve um reajuste de 10% para R$ {salario_inferior:.2f}')
