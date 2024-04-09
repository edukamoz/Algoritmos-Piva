frase = input('Digite uma frase qualquer: ').lower()
palavra = input('Digite a palavra que você quer saber quantas vezes repete: ').lower()

num_repeticoes = frase.count(palavra)

print(f'A palavra "{palavra}" repetiu {num_repeticoes} vezes na frase que você digitou.')
