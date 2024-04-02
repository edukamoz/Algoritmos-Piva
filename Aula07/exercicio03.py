peso_total = 0
altura_total = 0
qnt = 1
IMCs = []

# Comando for

# for i in range(1, 6):
#     peso = float(input(f'Digite o peso em kg da pessoa {i}: '))
#     altura = float(input(f'Digite a altura em m da pessoa {i}: '))
#     peso_total += peso
#     altura_total += altura
#     IMCs.append(peso / (altura ** 2))

# Comando while

while qnt <= 5:
    peso = float(input(f'Digite o peso em kg da pessoa {qnt}: '))
    altura = float(input(f'Digite a altura em m da pessoa {qnt}: '))
    peso_total += peso
    altura_total += altura
    IMCs.append(peso / (altura ** 2))
    qnt += 1

peso_medio = peso_total / 5
altura_media = altura_total / 5

print(f'Peso médio: {peso_medio:.2f}kg')
print(f'Altura média: {altura_media:.2f}m')
print(f'Maior IMC: {max(IMCs)}')
print(f'Menor IMC: {min(IMCs)}')
