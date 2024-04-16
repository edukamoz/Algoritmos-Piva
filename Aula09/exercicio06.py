from random import randint
dado1 = []
dado2 = []
somas = []

for i in range(30000):
    dado1.append(randint(1, 6))
    dado2.append(randint(1, 6))
    somas.append(dado1[i] + dado2[i])

for i in range(2, 13):
    print(f'{i}: {somas.count(i)}')
