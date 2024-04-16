matriz = []
coluna = []

for i in range(2):
    for j in range(2):
        coluna.append(int(input(f'{i, j}: ')))
    matriz.append(coluna)
    coluna = []

print(matriz)
