# Conversión de una cantidad en dólares a distintas monedas 
Cantidad_dolares = int(input("Ingrese la cantidad de dolares: "))
tasa_euros = 0.92
tasa_libras = 0.76
tasa_yenes = 151.50
cambio_euros = Cantidad_dolares * tasa_euros
cambio_libras = Cantidad_dolares * tasa_libras
cambio_yenes = Cantidad_dolares * tasa_yenes
print(f"La cantidad de dolares: ${Cantidad_dolares:.2f}USD")
print(f"La cantidad convertida en euros: €{cambio_euros:.2f}EUR")
print(f"La cantidad convertidad en libras: £{cambio_libras:.2f}GBP")
print(F"La cantidad convertidad en yenes: ¥{cambio_yenes:.2f} JPY")