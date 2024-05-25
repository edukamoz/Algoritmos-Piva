valor_hora = float(input('Digite o valor da sua hora: '))
horas_trabalhadas = int(input('Digite quantas horas você trabalha por mês: '))

salario_bruto = valor_hora * horas_trabalhadas

ir = float
inss = 0.1 * salario_bruto
fgts = 0.11 * salario_bruto

if salario_bruto > 2500:
    ir = 0.2
elif salario_bruto > 1500:
    ir = 0.1
elif salario_bruto > 900:
    ir = 0.05
else:
    ir = 0

ir_valor = ir * salario_bruto

salario_liquido = salario_bruto - ir_valor - inss

print(f"""
Salário Bruto:         R$ {salario_bruto:.2f}
(-) IR ({(ir * 100):.0f}%):           R$ {ir_valor:.2f}
(-) INSS (10%):        R$ {inss:.2f}
FGTS (11%):            R$ {fgts:.2f}
Total de descontos:    R$ {(inss + ir_valor):.2f}
Salário líquido:       R$ {salario_liquido:.2f}
""")
