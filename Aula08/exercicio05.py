palavra = input('Digite uma palavra: ').split(" ")

palavra_invertida = palavra[::-1]
palindromo = 'É um palindromo' if palavra == palavra_invertida else "Não é um palindromo"

print(palindromo)
