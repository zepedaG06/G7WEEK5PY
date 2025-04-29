calificacion = int(input("Ingrese su calificación numérica: "))
if(calificacion >= 0 and calificacion <= 69):
    print("REPROBADO")
elif(calificacion >= 70 and calificacion <= 79):
    print("REGULAR")
elif(calificacion >= 80 and calificacion <= 89):
    print("BUENO")
elif(calificacion >= 90 and calificacion <= 99):
    print("MUY BUENO")
elif(calificacion == 100):
    print("EXCELENTE")
else:
    print("NOTA INVALIDA")