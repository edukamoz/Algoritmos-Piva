palavras = []

for i in range(20):
    palavras.append(input(f'Digite a {i+1}ºPalavra: '))

for palavra in palavras:
    print(palavra[::-1])
