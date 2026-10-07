productos = input("Dime los productos de tu cesta separados por comas: ")
vect = productos.split(",")
for i in range(0, len(vect)):
    print(f"Producto {i+1}: {vect[i].strip()}")