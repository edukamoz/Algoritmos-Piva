vetorA = []

for i in range(10):
    vetorA.append(int(input(f'Digite o número {i+1}: ')))

vetorB = sorted(vetorA)

print(f"""
Vetor A: {vetorA}
Vetor B: {vetorB}
""")
