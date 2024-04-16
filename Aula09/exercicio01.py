lista = []

for i in range(10):
    lista.append(int(input(f'Digite o número {i+1}: ')))

print(lista[::-1])
