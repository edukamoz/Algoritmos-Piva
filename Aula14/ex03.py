num = input("Digite seu RA: ")
soma = 0
mult = 1

for dig in num:
    soma += int(dig)
    mult *= int(dig)

print(f'''
RA: {num}
Multiplicação: {mult}
Soma: {soma}
''')
