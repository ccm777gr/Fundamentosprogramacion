dinero = float(input("Dime el dinero a invertir: "))
interes = float(input("Dime el interes simple: "))
ajnos = int(input("Dime el numero de años a invertir: "))

suminteres = dinero*(interes/100)

for i in range(1, ajnos + 1):
    inversion = dinero + suminteres
    print(f"Capital en el año {i}: {inversion} €")