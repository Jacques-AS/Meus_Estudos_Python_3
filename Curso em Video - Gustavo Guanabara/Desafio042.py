'''
Desafio 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar o tipo de triângulo será formado:
•	Equilátero: todos os lados iguais
•	Isósceles: dois lados iguais
•	Escaleno: todos os lados diferentes
'''
t1 = float(input("Primeiro segmento: "))
t2 = float(input("Segundo segmento: "))
t3 = float(input("Terceiro segmento: "))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("Os segmentos acima podem formar um TRIÂNGULO! ")
    if t1 == t2 == t3:
        print("EQUILÁTERO")
    elif t1 != t2 != t3 != t1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima não podem formar um TRIÂNGULO! ")