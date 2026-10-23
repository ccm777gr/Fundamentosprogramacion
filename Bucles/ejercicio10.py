num = int(input("dime un numero entero: "))
primo = False
for i in range(2, num-1):
    if (num%i) == 0:
        primo = True

if primo == True:
    print("El numero no es primo")
else:
    print("El numero es primo")