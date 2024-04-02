numero = int(input('Digite um número: '))
fatorial = 1
qnt = 1

# Comando for

if numero < 0:
    print('Não existe fatorial para número negativo!')
elif numero == 0:
    print('O fatorial para o número 0 é sempre 1')
else:
    for i in range(1, numero + 1):
        fatorial *= i

# Comando while

if numero < 0:
    print('Não existe fatorial para número negativo!')
elif numero == 0:
    print('O fatorial para o número 0 é sempre 1')
else:
    while qnt <= numero:
        fatorial *= qnt
        qnt += 1

print(f'{numero}! = {fatorial}')
