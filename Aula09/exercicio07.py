primos_depois_100 = []
primos_antes_100 = [2, 3, 5, 7, 11]

for i in range(100, 1000):
    if len(primos_depois_100) == 10:
        break
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
        primos_depois_100.append(i)

print(primos_depois_100)
