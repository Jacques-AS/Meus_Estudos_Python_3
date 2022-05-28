#Modelo Ver. 4
print('TABUADA DE 1 A 10:')
operacao = str(input('Escolha Uma Operação Aritmética ( +  -  *  / ): '))

if operacao == '+':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} + {coluna2:2} = {coluna1+coluna2:2}')

elif operacao == '-':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} - {coluna2:2} = {coluna1-coluna2:2}')

elif operacao == '*':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} x {coluna2:2} = {coluna1*coluna2:2}')

elif operacao == '/':
    for coluna1 in range(1, 11):
        print('*' *13)
        for coluna2 in range(1, 11):
            print(f'{coluna1:2} / {coluna2:2} = {coluna1/coluna2:.2f}')
else:
    print('Operação inválida, por favor escolha uma das opções informadas')
