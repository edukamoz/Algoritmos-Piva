preco_liquido = float(input('Digite o valor líquido do produto: '))
codigo_origem = int(input('Digite o código de origem do produto: '))

codigos = {
    1: 0.11,
    2: 0.13,
    3: 0.09,
    4: 0.12,
    5: 0.18
}

if codigo_origem > 5:
    print('Código de origem inválido ou não cadastrado')
