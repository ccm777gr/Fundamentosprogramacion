palabra = input("Dime una palabra: ")
letra = input("Dime una letra: ")
cant = 0
vect = list(palabra)

for i in range(0, len(palabra)):
    if vect[i] == letra:
        cant = cant + 1

print(f"En la palabra {palabra} hay {cant} {letra.upper()}")