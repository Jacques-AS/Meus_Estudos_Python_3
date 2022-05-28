'''
Desafio 047:
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
print('Estes Números Abaixo são Pares')
for num in range(1, 51):
    res = num % 2
    if res == 0:
        print(num)

