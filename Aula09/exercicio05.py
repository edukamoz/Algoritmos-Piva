from random import randint
sorteios = []

for i in range(6000):
    sorteios.append(randint(1, 6))

for i in range(6):
    print(f'{i+1} : {sorteios.count(i+1)}')
