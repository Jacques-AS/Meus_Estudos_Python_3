nome = str(input('Digite seu nome: '))
if nome == 'Jacques':
    print(f'Que nome LINDO !!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print(f'Belo nome feminino.')

else:
    print(f'Seu nome é bem normal.')
print(f'Tenha um ótimo dia, {nome}.')