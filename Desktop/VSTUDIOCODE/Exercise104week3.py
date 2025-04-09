primer_tramo = float(input("Duración del primer tramo del vuelo: "))
primera_escala = float(input("Duración de la primera escala: "))
segundo_tramo = float(input("Duración del segundo tramo del vuelo: "))
segunda_escala = float(input("Duración de la segunda escala: "))
tercera_tramo = float(input("Duración del tercer tramo del vuelo: "))
sum1 = primer_tramo + primera_escala
sum2 = sum1 + segundo_tramo
sum3 = sum2 + segunda_escala
sum4 = sum3 + tercera_tramo
print(sum4)