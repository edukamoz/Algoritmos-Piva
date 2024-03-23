numero = int(input('Digite um numero menor que 1000: '))

if numero >= 1000:
    print('O valor informado é maior ou igual a 1000')
    quit()

textoC = 'centena'
textoD = 'dezena'
textoU = 'unidade'

if numero / 100 >= 1:
    centena = numero // 100
    resto = numero % 100
    if centena > 1:
        textoC = 'centenas'
    dezena = resto // 10
    resto = numero % 10
    if dezena > 1:
        textoD = 'dezenas'
    unidade = resto // 1
    if unidade > 1:
        textoU = 'unidades'
    print(f'{numero} = {centena} {textoC}, {dezena} {textoD} e {unidade} {textoU}')
elif numero / 10 >= 1:
    dezena = numero // 10
    resto = numero % 10
    if dezena > 1:
        textoD = 'dezenas'
    unidade = resto // 1
    if unidade > 1:
        textoU = 'unidades'
    print(f'{numero} = {dezena} {textoD} e {unidade} {textoU}')
elif numero / 1 >= 1:
    unidade = numero // 1
    if unidade > 1:
        textoU = 'unidades'
    print(f'{numero} = {unidade} {textoU}')
