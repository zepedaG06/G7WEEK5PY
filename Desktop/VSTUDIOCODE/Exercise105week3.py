total_segundos = int(input("Cantidad total de segundos: "))
horas = int(total_segundos / 3600)
horas_en_segundos = horas * 3600
segundos_restantes = total_segundos - horas_en_segundos
minutos = int(segundos_restantes / 60)
minutos_segundos = minutos * 60
segundos = segundos_restantes - minutos_segundos
print(f"{horas} horas, {minutos} minutos y {segundos} segundos")