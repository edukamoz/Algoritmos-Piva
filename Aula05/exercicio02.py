idade = int(input('Digite a idade do nadador: '))

if idade > 30:
    print('Nadador Sênior!')
elif idade >= 16:
    print('Nadador Adulto!')
elif idade >= 11:
    print('Nadador Adolescente!')
elif idade >= 8:
    print('Nadador Juvenil!')
elif idade >= 5:
    print('Nadador Infantil!')
else:
    print('Nadador Inapto!')
