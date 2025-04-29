edad_usuario = int(input("Ingrese su edad: "))
if(edad_usuario >= 0 and edad_usuario <= 12):
    print("No tiene edad para ver esta película")
elif(edad_usuario >= 13 and edad_usuario <= 17):
    print("Puede ver la película")
elif(edad_usuario > 18):
    print("Puede ver la película")
else:
    print("Puede ver la película")