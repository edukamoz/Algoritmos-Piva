numero = int(input('Digite um número inteiro maior que 1: '))
qnt = 0
contador = 1

if numero < 1:
    print('Número menor que 1')
    quit()

# Comando for
for i in range(2, numero+1):
    if numero % i == 0 and numero % 1 == 0:
        qnt += 1

# Comando while
while contador <= numero:
    if numero % (contador + 1) == 0 and numero % 1 == 0:
        qnt += 1
        contador += 1
    else:
        contador += 1

if qnt > 1:
    print(f'O {numero} não é um número primo')
else:
    print(f'O {numero} é um número primo')
