combustivel = input('Digite o código do combustivel (A-álcool, G-gasolina): ').lower()
litros_vendidos = int(input('Digite quantos litros foram vendidos: '))

valor_total = float

match combustivel:
    case 'a':
        valor_bruto = litros_vendidos * 1.9
        if litros_vendidos <= 20:
            desconto = valor_bruto * 0.03
            valor_total = litros_vendidos - desconto
        else:
            desconto = valor_bruto * 0.05
            valor_total = litros_vendidos - desconto
    case 'b':
        valor_bruto = litros_vendidos * 2.5
        if litros_vendidos <= 20:
            desconto = valor_bruto * 0.04
            valor_total = litros_vendidos - desconto
        else:
            desconto = valor_bruto * 0.06
            valor_total = litros_vendidos - desconto

print(valor_total)
