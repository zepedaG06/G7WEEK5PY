#Crea un programa en python que permita leer el salario de un trabajador que gana por hora, calcular su salario en base a las horas trabajadas.
salario = float(input("Ingrese su salario por hora: "))
horas_trabajadas =  float(input("Cuantas horas trabaja: "))
salario_bruto = salario * horas_trabajadas
print(f"Salario a pagar {salario_bruto:.2f} ")
