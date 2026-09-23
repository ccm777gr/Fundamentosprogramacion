peso = float(input("dime tu peso en kg: "))
altura = float(input("dime tu altura en metros: "))
masacorporal = (peso/altura**2)
print(f"el indice de masa corporal es {round(masacorporal,2)}")