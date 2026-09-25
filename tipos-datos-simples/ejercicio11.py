dinero = float(input("Con cuanto dinero desea calcular el interes?: "))
interes = int(4)

ganancias1anho = dinero*(1 + ((interes/100))*1)
ganancias2anho = dinero*(1 + ((interes/100))*2)
ganancias3anho = dinero*(1 + ((interes/100))*3)

print(f"En los tres años tienes {round(ganancias1anho,2)}, {round(ganancias2anho,2)} y {round(ganancias3anho,2)}")