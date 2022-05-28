'''
Desafio 011:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''
larg = int(input('Largura da Parede: '))
alt = int(input('Altura da Parede: '))
dimensao = larg * alt
tinta = dimensao / 2
print(f'Sua parede tem uma dimensão {larg}x{alt}. A sua área da parede é: {dimensao} m², será utilizado {tinta} latas de tintas para demanda exigida.')
