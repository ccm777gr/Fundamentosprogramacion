puntuacion = float(input("Dime tu puntuación: "))
if puntuacion == 0.0:
    dineroextra = puntuacion * 2400
    print(f"Nivel: Inaceptable\nDinero extra: {dineroextra}")
elif puntuacion == 0.4:
    dineroextra = puntuacion * 2400
    print(f"Nivel: Aceptable\nDinero extra: {dineroextra}")
elif puntuacion >= 0.6:
    dineroextra = puntuacion * 2400
    print(f"Nivel: Meritorio\nDinero extra: {dineroextra}")
else:
    print("valor invalido")