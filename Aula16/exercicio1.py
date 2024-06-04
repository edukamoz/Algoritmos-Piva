lista = []

with open('exercicio1.txt', 'r') as arquivo:
    for linha in arquivo:
        lista.append(linha.split())

print(f'''
ACME Inc.               Uso do espaço em disco pelos usuários
---------------------------------------------------------------------
Nr.     Usuário     Espaço utilizado        % do uso
''')

x = 0
soma = 0
for i in range(0, len(lista)):
    soma += int(lista[i][1])

soma /= (1024 * 1024) * 100
for pessoa in lista:
    pessoa[1] = (int(pessoa[1]) / 1024 / 1024)
    x += 1
    print(f'{x:2d}     {pessoa[0]:15s}     {pessoa[1]:.2f} MB      {pessoa[1]/soma:.2f}')
