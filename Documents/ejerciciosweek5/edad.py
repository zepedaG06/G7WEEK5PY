edad = int(input("Ingrese su edad: "))
if(edad >= 0 and edad <= 12 ):
    print("Usted es un niño")
elif(edad >= 13 and edad <= 18):
    print("Usted es un adolescente")
elif(edad >= 19 and edad <= 59):
    print("Usted es un adulto")
elif(edad >= 60 and edad <= 100):
    print("Usted es un anciano")
elif(edad >= 101 and edad <= 130):
    print("Usted es un Centenario")
else:
    print("Edad Invalida")
    