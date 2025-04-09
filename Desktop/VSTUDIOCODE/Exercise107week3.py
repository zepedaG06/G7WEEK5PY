#  Cálculo del precio final de un producto con impuestos y descuentos
precio_original_producto = float(input("el precio original del producto: "))
porcentaje_descuento = float(input("el porcentaje de descuento aplicado: "))
descuento = (precio_original_producto * porcentaje_descuento) / 100
precio_con_descuento = precio_original_producto - descuento
porcentaje_iva = float(input("Ingrese el porcentaje iva: "))
iva = (precio_con_descuento * porcentaje_iva) / 100
precio_final = precio_con_descuento + iva
print(f"Precio original: ${precio_original_producto:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento}%): ${descuento:.2f}")
print(f"Precio con descuento: ${precio_con_descuento:.2f}")
print(f"IVA calculado ({porcentaje_iva}%): ${iva:.2f}")
print(f"Precio final: ${precio_final:.2f}")



