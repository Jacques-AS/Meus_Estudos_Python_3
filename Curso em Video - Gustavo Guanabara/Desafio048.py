'''
Desafio 048:
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de
três e que se encontram no intervalo de 1 até 500.
'''
s = 0
for num in range(1,500):
    if num % 3 == 0:
        s += num
print(f'Soma entre todos os números ímpares\nque são múltiplos de três e que se\nencontram no intervalo de 1 até 500\né igual a ( {s} )')
