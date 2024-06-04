import math

print('Digite os valores para uma equação do segundo grau: ')
a = float(input('Valor de A: '))

if a == 0:
    print('Se A for igual a zero não é uma equação de segundo grau!')
    quit()

b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

delta = math.pow(b, 2) - 4 * a * c

if delta < 0:
    print('A equação não possui raízes reais!')
    quit()
elif delta == 0:
    raiz = (-b) / (2 * a)
    print(f'A equação possui apenas uma raíz: {raiz}')
else:
    raiz1 = ((-b) + math.sqrt(delta)) / (2 * a)
    raiz2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f'''A equação possui duas raízes:
Raiz 1: {raiz1}
Raiz 2: {raiz2}
''')
    