'''
Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'Hipotenusa é {hipotenusa}')
'''
#Modo com a biblioteca Math
import math
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'Hipotenusa é {hipotenusa}')
