lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))
if(lado1 == lado2 == lado3):
    print("Triángulo equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")