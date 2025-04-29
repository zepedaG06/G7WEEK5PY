num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
operacion = input("Escoger un operador (+,-,*,/): ")
if(operacion == "+"):
    suma = num1 + num2
    print(suma)
elif(operacion == "-"):
    resta = num1 - num2
    print(resta)
elif(operacion == "*"):
    multiplicacion = num1 * num2
    print(multiplicacion)
elif(operacion == "/"):
    division = num1 / num2
    print(division)
else:
    print("Operador no válido")