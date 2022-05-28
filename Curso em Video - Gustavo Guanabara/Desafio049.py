'''
Desafio 049:
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
print('**** TABUADA DE MULTIPLICAÇÃO ****')
num = int(input('Digite um Número para Tabuada: '))
for tabuada in range (1, 11):
    total = tabuada * num
    print(f'{tabuada} x {num} = {total}')
print(f'PROGRAMA TABUADA ENCERRADO, Volte sempre!')
