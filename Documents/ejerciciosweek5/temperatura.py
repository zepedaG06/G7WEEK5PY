temperatura = float(input("Ingrese la temperatura en grados celsius: "))
if(temperatura >= 0 and temperatura <= 15):
    print("Frío")
elif(temperatura >= 16 and temperatura <= 25):
    print("Templado")
elif(temperatura >= 26 and temperatura <= 35):
    print("Cálido")
else:
    print("Muy caluroso")