print('\nDigite os valores dos lados de um Triângulo:')
x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))
z = float(input('Terceiro valor: '))

if (x + y) > z and (x + z) > y and (z + y) > x:
    if x == y and y == z:
        print('Triângulo Equilátero')
    elif x == y or y == z or x == z:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não são valores válidos para criar um triângulo')
