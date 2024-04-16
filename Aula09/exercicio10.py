matriz = []
coluna = []
maior = 0

for i in range(2):
    for j in range(2):
        coluna.append(int(input(f'{i, j}: ')))
    matriz.append(coluna)
    if max(coluna) > maior:
        maior = max(coluna)
    coluna = []

print(matriz * maior)
