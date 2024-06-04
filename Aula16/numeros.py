lista = []

with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo:
        lista.append(linha.replace(',', '').split())

somaMulher = 0
somaHomem = 0
mulheres = 0
homens = 0
for i in range(0, len(lista)):
    if lista[i][1] == 'F':
        somaMulher += int(lista[i][0])
        mulheres += 1
    else:
        somaHomem += int(lista[i][0])
        homens += 1


print(f'''
Idade Média das Mulheres: {somaMulher / mulheres}
Idade Média dos Homens: {somaHomem / homens}
''')
