nombre = input("Dime el nombre del producto: ")
valor = float(input("Dime el precio del producto(si tiene decimales separalo con punto): "))
unidades = int(input("Dime las unidades del producto: "))
costetotal = valor * unidades

print(f"{nombre}{valor:9.2f}{unidades:3d}{costetotal:11.2f}")