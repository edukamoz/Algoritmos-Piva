nome = input('Digite seu primeiro nome: ').title()
nome_do_meio = input('Digite seu nome do meio: ').title()
sobrenome = input('Digite seu sobrenome: ').title()

nome_completo = [nome, nome_do_meio, sobrenome]
nome_completo = " ".join(nome_completo)

print(f"\nMuito prazer, {nome_completo}!")
