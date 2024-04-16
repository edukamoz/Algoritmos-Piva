lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
n = 0

for i in range(1, 10, 2):
    lista.insert(i, lista2[n])
    n += 1

print(lista)
