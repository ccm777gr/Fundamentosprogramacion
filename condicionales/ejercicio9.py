print("Menores de 4: Gratis \nEntre 4 y 18: 5€ \nMayor de 18: 10€")
edad = int(input("Dime tu edad: "))

if edad < 4:
    print("Gratis")
elif edad >= 4 and edad <= 18:
    print("5€")
elif edad > 18:
    print("10€")
else:
    print("Valor no valido")