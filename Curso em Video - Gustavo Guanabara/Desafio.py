'''DESAFIO 001
nome = input('Digite seu nome: ')
print(f'Olá \033[97:46m{nome}\033[m prazer em te conhecer, seja bem vindo.')

DESAFIO 002
dia = int(input('Digite o DIA em que você NASCEU: '))
mes = str(input('Digite o MÊS em que você NASCEU: '))
ano = int(input('Digite o ANO em que você NASCEU: '))
print(f'Você nasceu no dia {dia} de {mes} do ano de {ano}')

DESAFIO 003
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
soma = num1 + num2
print('*'*25)
print(f'{num1} + {num2} = {soma}')

DESAFIO 004
algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: ', type(algo))
print(f'Só tem espaços? {algo.isspace()}')
print(f'É númerico? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em letras maiúsculas? {algo.isupper()}')
print(f'Está em letras minúsculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')

DESAFIO 005
numero = float(input('Digite um valor: '))
antecessor = numero - 1
sucessor = numero + 1
print(f"O número: {numero:.0f}\nSeu antecessor é: {antecessor:.0f} \nSeu sucessor é: {sucessor:.0f}")

DESAFIO 006
numero = float(input('Digite um valor: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print(f'O número: {numero:.0f}\nDobro: {dobro:.0f}\nTriplo: {triplo:.0f}\nRaiz Quadrada: {raiz_quadrada:.0f}')

DESAFIO 007
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
media = (nota1 + nota2) / 2
print(f'Nota1: {nota1} Nota2: {nota2}, sua Média foi: {media}')

DESAFIO 008
metro = float(input('Digite um valor em metros: '))
centimetro = metro * 100
milimetro = metro * 1000
print(f'{metro:.0f} Metro é igual a {centimetro:.0f} Centímetro, que é igual a {milimetro:.0f} Milímetro')

DESAFIO 009
numero = int(input('Digite um número para Tabuada de Multiplicação: '))
print (f'{numero} x {0:2} = {numero*0:2}')
print (f'{numero} x {1:2} = {numero*1:2}')
print (f'{numero} x {2:2} = {numero*2:2}')
print (f'{numero} x {3:2} = {numero*3:2}')
print (f'{numero} x {4:2} = {numero*4:2}')
print (f'{numero} x {5:2} = {numero*5:2}')
print (f'{numero} x {6:2} = {numero*6:2}')
print (f'{numero} x {7:2} = {numero*7:2}')
print (f'{numero} x {8:2} = {numero*8:2}')
print (f'{numero} x {9:2} = {numero*9:2}')
print (f'{numero} x {10:2} = {numero*10:2}')

DESAFIO 010
reais = float(input('Digite quanto você tem em R$: '))
dolar = reais / 3.27
print(f'Você tem R$ {reais:.2f} e em Dólar U$$ {dolar:.2f}')

DESAFIO 011'''
















