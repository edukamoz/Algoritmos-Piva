valor_compra = float(input('Digite o valor da compra: '))
valor_final = float

if valor_compra < 1000.99:
    valor_final = valor_compra * 0.9
elif valor_compra < 5000:
    valor_final = valor_compra * 0.8
else:
    valor_final = valor_compra * 0.7

print(f'Valor total da compra:   R$ {valor_final:.2f}')
