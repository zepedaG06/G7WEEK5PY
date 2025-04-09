# Cálculo del índice de masa corporal (IMC)
peso_kg = float(input("peso en kg: "))
altura_metros = float(input("Altura en metro: "))
alt2 = altura_metros * altura_metros
IMC = peso_kg / alt2
imc2 =  IMC * 100
imc3 = imc2 / 100
if imc3 < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc3 < 25:
    clasificacion = "Peso normal"
elif 25 <= imc3 < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print(peso_kg)
print(altura_metros)
print(IMC)


