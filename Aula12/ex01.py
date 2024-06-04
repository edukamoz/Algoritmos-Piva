def par_ou_impar(n):
    valor = True if n % 2 == 0 else False
    return valor


num = int(input('Digite um número: '))

msg = 'Par' if par_ou_impar(num) else 'Ímpar'

print(msg)
