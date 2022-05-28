#Modelo Ver. 3
while True:
    num = int(input('Digite um número para  ver a sua tabuada: '))
    if num < 0:
        break
    for contador in range(1, 11):
        print(f'{num:2} x {contador:2} = {num* contador:2}')
print(f'PROGRAMA TABUADA ENCERRADO, Volte sempre!')
