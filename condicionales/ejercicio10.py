pedido = input("¿Tu pizza sera vegetariana?(S/N): ")

if pedido.lower() == "s":
    print("Ingredientes disponibles: Pimiento(1) y Tofu(2)")
    eleccion = input("¿Que ingrediente quieres?(Pon el numero): ")
    if eleccion == "1":
        print("Detalles del pedido\nTipo de pizza: Vegetariana\nIngrediente: Mozzarela, tomate y pimiento")
    elif eleccion == "2":
        print("Detalles del pedido\nTipo de pizza: Vegetariana\nIngrediente: Mozzarela, tomate y tofu")
    else:
        print("Valor incorrecto")
elif pedido.lower() == "n":
    print("Ingredientes disponibles: Peperoni(1), Jamón(2) y Salmón(3)")
    eleccion = input("¿Que ingrediente quieres?(Pon el numero): ")
    if eleccion == "1":
        print("Detalles del pedido\nTipo de pizza: No vegetariana\nIngrediente: Mozzarela, tomate y peperoni")
    elif eleccion == "2":
        print("Detalles del pedido\nTipo de pizza: No vegetariana\nIngrediente: Mozzarela, tomate y jamón")
    elif eleccion == "3":
            print("Detalles del pedido\nTipo de pizza: No vegetariana\nIngrediente: Mozzarela, tomate y salmón")
    else:
        print("Valor incorrecto")
else:
    print("Valor incorrecto")