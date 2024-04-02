frase = input('Digite uma frase: ')
a = 0

for i in frase:
    if i.lower() in 'aeiouáàãéêíóu':
        a += 1

print(f'Existem {a} vogais na frase')
