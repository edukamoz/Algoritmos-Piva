data = input('Digite sua data de nascimento (dd/mm/aaaa): ')

data_formatada = data.split('/')[::-1]
data_formatada = data_formatada[0] + data_formatada[1] + data_formatada[2]

print(data_formatada)
