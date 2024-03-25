numero = int(input('Digite um número: '))

if numero % 5 == 0 and numero % 3 == 0:
    print(f'O número {numero} é divisível por 5 e 3 ao mesmo tempo')
else:
    print('O número que você digitou não é divisível por 5 e 3 ao mesmo tempo')
