'''
Desafio 033:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
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
