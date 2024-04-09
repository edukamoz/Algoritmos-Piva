frase = input('Digite uma frase qualquer: ').lower()

vogais = ('a', 'e', 'i', 'o', 'u', 'à', 'á', 'õ', 'ã', 'ó', 'é', 'í')
num_vogais = 0

for vogal in vogais:
    num_vogais += frase.count(vogal)

print(num_vogais)
