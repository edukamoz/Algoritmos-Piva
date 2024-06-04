def converter_para_segundos(horas, minutos, segundos):
    segundos += (minutos * 60) + (horas * 3600)
    return segundos


print(converter_para_segundos(2, 40, 10))
