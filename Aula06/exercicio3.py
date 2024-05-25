print('Digite as dimensões do aposento em questão: ')
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
litros_tinta = float(input('\nDigite quantos litros possui o balde de tinta: '))

metros_comprimento = comprimento * 2.8
metros_largura = largura * 2.8
metros_porta = 0.8 * 2.1
metros_totais = (metros_comprimento * 2) + (metros_largura * 2) - metros_porta
metros_por_balde = litros_tinta * 3

qnt_tinta = round(metros_totais / metros_por_balde)

print(f'A quantidade de baldes de tinta necessárias para pintar um cômodo de {comprimento}m'
      f' de comprimento e {largura}m de largura são de {qnt_tinta} baldes.')
