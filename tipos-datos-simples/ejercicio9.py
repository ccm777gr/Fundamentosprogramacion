cantidad = float(input("Cuánto quieres invertir?: "))
interes-año = float(input("Cuál es el interés anual (en %)?: "))
num-años = float(input("A cuántos años es la inversión?: "))

capital-final = cantidad * (1 + interes-año / 100) ** num-años

print(f"El capital obtenido tras {num-años} años es de: {round(capital-final,2)}")
