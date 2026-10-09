renta = int(input("Dime tu renta anual: "))

if renta < 10000:
    print("5%")
elif (renta >= 10000 and renta < 20000):
    print("15%")
elif (renta >= 20000 and renta < 35000):
    print("20%")
elif (renta >= 35000 and renta < 60000):
    print("30%")
elif renta >= 60000:
    print("45%")
else:
    print("ERROR")