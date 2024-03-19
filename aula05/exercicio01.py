letra = input('Digite uma letra: ').lower()

vogais = ('a', 'e', 'i', 'o', 'u')

for vogal in vogais:
    if vogal == letra:
        print(f'A letra {letra} é uma vogal.')
        break
    else:
        print(f'A letra {letra} é uma consoante.')
        break
