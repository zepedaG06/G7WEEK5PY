#Cálculo del salario neto de un empleado
Salario_bruto = float(input("Salario bruto del empleado: "))
Impuesto_renta = Salario_bruto * 0.1
seguro_social = Salario_bruto * 0.05
fondo_pensiones = Salario_bruto * 0.03
descuentos_totales = Impuesto_renta + seguro_social + fondo_pensiones
salario_neto = Salario_bruto - descuentos_totales
print(Salario_bruto)
print(descuentos_totales)
print(salario_neto)
