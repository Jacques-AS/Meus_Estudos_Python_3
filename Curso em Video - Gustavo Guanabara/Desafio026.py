'''
Desafio 026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase:\n')).upper()
print(f'Quanta vezes apareceu a letra "A" \n Resposta: {frase.count("A")} vezes')
print(f'Letra "A" aparece primeira vez na posição.\n Resposta: {frase.find("A")}')
print(f'Letra "A" aparece última vez na posição.\n Resposta: {frase.rfind("A")}')
