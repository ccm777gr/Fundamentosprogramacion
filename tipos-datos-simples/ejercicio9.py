cantidad = float(input("Cuánto quieres invertir?: "))
interes_año = float(input("Cuál es el interés anual (en %)?: "))
num_años = float(input("A cuántos años es la inversión?: "))

capital_final = cantidad * (1 + interes_año / 100) ** num_años

print(f"El capital obtenido tras {num_años} años es de: {round(capital_final,2)}")
