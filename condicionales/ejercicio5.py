edad = int(input("Dime tu edad: "))
ingresos = int(input("Dime tus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Debes tributar")
else:
    print("No puedes tributar")