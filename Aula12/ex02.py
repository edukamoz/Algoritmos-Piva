primos = (2, 3, 5, 7, 11)


def primo_ou_nao(numero):
    for primo in primos:
        if primo == numero:
            return True
        resultado = False if numero % primo == 0 else True
        if not resultado:
            return resultado
    return True


num = int(input('Digite um número: '))
print('É primo' if primo_ou_nao(num) else 'Não é primo')
