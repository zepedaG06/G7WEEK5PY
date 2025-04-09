# Cálculo de área y perímetro de un rectángulo
base_rectangulo = float(input("la base del rectángulo: "))
altura_rectangulo = float(input("la altura del rectángulo: "))
área_rectángulo = base_rectangulo * altura_rectangulo
print(área_rectángulo)
base_doble = base_rectangulo * 2
altura_doble = altura_rectangulo * 2
perimetro = base_doble + altura_doble
print(perimetro)