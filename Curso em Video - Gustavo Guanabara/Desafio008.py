'''
Desafio 008:
Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
'''
n = float(input('Digite um valor em metro: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f'O valor escolhido é {n}m, equivale a: \n{km} quilômetro (km)\n{hm} hectômetro (hm)\n{dam} decâmetro (dam)\n{dm} decímetro (dm)\n{cm} centímetro (cm)\n{mm} milímetro (mm).')

#OUTRO MODELO
metro=int(input('Digite quantidade de metros: '))
centimetro = metro * 100
milimetro = metro * 1000
#print('Quant. de Metro {} é igual a {}  Centímetros e igual {} Milímetros'. format(metro, centimetro, milimetro))
print(f'Quant. de Metro {metro} é igual a {centimetro}  Centímetros e igual {milimetro} Milímetros')
