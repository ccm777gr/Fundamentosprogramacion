dinero = float(input("Dame el precio del producto con dos decimales: "))
dinerotext = str(dinero)
dineroarray = dinerotext.split(".")
print(f"El precio es {dineroarray[0]} euros con {dineroarray[1]} centimos")