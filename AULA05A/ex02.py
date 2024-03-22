nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
nota = ''
aprovacao = ''

if media < 4:
    nota = 'E'
    aprovacao = 'REPROVADO'
elif media < 6:
    nota = 'D'
    aprovacao = 'REPROVADO'
elif media < 7.5:
    nota = 'C'
    aprovacao = 'APROVADO'
elif media < 9:
    nota = 'B'
    aprovacao = 'APROVADO'
else:
    nota = 'A'
    aprovacao = 'APROVADO'

print(f'''
Primeira nota: {nota1}
Segunda nota: {nota2}

Média: {media}
Nota: {nota}

Status: {aprovacao}
''')
