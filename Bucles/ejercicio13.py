palabra = input("Dime algo(salir = salir del bucle): ")
comprobacion = palabra.lower()

while comprobacion != "salir":
    print(palabra)
    palabra = input("Dime algo(salir = salir del bucle): ")
    comprobacion = palabra.lower()
