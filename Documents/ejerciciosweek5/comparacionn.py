numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

if(numero1 == numero2 == numero3):
    print("Son iguales")
elif(numero1 >= numero2 and numero1 >= numero3):
    print("Numero mayor ",numero1)
    if(numero2 <= numero3):
        print("Numero menor ",numero2)
    else:
        print("El numero menor ",numero3)
elif(numero2 >= numero1 and numero2 >= numero3):
    print("Numero mayor ",numero2)
    if(numero1 <= numero3):
        print("Numero menor ",numero1)
    else:
        print("Numero menor ",numero3)
elif(numero3 >= numero1 and numero3 >= numero2):
    print("Numero mayor ",numero3)
    if(numero1 <= numero2):
        print("Numero menor ",numero1)
    else:
        print("Numero menor ",numero2)
