# Cálculo del volumen de un cilindro y su área superficial 
radio_cilindro = float(input("Ingrese el radio del cilindro: "))
altura_cilindro = float(input("Ingrese la altura del cilindro: "))
area_base = 3.1416 * (radio_cilindro * radio_cilindro)
volumen_cilindro = area_base * altura_cilindro
area_lateral = 2 * (3.1416 * (radio_cilindro * altura_cilindro))
area_superficial = area_lateral + 2 * area_base
print(f"el radio ingresado es: {radio_cilindro:.2f}")
print(f"altura ingresada: {altura_cilindro:.2f}")
print(f"El volumen calculado es: {volumen_cilindro:.2f}")
print(f"El area superficial es: {area_superficial:.2f}")