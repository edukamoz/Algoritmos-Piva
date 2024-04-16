lista = []

for i in range(5):
    lista.append(int(input(f'Digite o número {i+1}: ')))

maior_valor = max(lista)

print(f"""
Maior valor: {maior_valor}
Índice: {lista.index(maior_valor)}
""")
