def ano_bissexto(aaaa):
    if aaaa % 400 == 0 and aaaa % 100 == 0:
        return 1
    elif aaaa % 100 == 0:
        return 0
    elif aaaa % 4 == 0:
        return 1


ano = int(input('Digite um ano: '))
print('É bissexto' if ano_bissexto(ano) == 1 else 'Não é bissexto')
