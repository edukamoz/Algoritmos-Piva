nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
nota = ''
aprovacao = ''

if media < 4:
    nota = 'E'
elif media < 6:
    nota = 'D'
elif media < 7.5:
    nota = 'C'
elif media < 9:
    nota = 'B'
else:
    nota = 'A'

aprovacao = 'APROVADO' if media >= 6 else 'REPROVADO'

print(f'''
Primeira nota: {nota1}
Segunda nota: {nota2}

Média: {media}
Nota: {nota}

Status: {aprovacao}
''')
