# Cálculo del tiempo total de una película con comerciales 
duracion_minutos = float(input("Ingrese la duración de la pelicula en minutos: "))
duracion_comerciales_previos = float(input("Ingrese la duración de los comerciales previos: "))
pausas_comerciales = float(input("Ingrese la cantidad de pausas comerciales: "))
cada_comercial = float(input("Ingres la duración de cada pausa comercial: "))
total_comerciales = pausas_comerciales * cada_comercial
subtotal = duracion_minutos + duracion_comerciales_previos
duracion_total = subtotal + total_comerciales
print(f"La duración original de la película: {duracion_minutos:.3f} minutos")
print(f"Duración total de los cormeciales: {duracion_comerciales_previos + total_comerciales:.2f} minutos")
print(f"El tiempo total de la proyección: {duracion_total:.2f} minutos")