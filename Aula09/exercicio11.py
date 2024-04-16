matriz = []
coluna = []
soma = 0

for i in range(4):
    for j in range(4):
        coluna.append(float(input(f'({i}, {j})')))
        if i == j:
            soma += coluna[i]
    matriz.append(coluna)
    coluna = []

print(matriz)
print(soma)
