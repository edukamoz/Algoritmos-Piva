numero = int(input('Digite um número: '))
E = 0
qnt = 1

if numero <= 0:
    print('O número digitado é inválido')
    quit()

# Comando for

for i in range(1, numero+1):
    E += 2 ** i

print(E)

# Comando While

while qnt <= numero:
    E += 2 ** qnt
    qnt += 1

print(E)
