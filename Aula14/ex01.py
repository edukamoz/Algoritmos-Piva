def total_animais(t_cab, t_pes):
    pes_a_mais = t_cab * 4 - t_pes
    t_pes -= pes_a_mais
    t_coelhos = t_pes // 4
    t_patos = t_cab - t_coelhos
    return [t_patos, t_coelhos]


cabecas = int(input('Total de cabeças: '))
pes = int(input('Total de pés: '))
animais = total_animais(cabecas, pes)

print(f'''
Total de patos: {animais[0]}
Total de coelhos: {animais[1]}
''')
