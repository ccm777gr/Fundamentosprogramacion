pan_dia = float(3.49)
desc_nodia = float(0.6)
barras_vend_nodia = int(input("Cuantas barras de pan se han vendido que no son de este dia?: "))

pan_desc = pan_dia-(pan_dia*desc_nodia)

print(f"La barra de pan esta a {pan_dia}, con el descuento cuesta {round(pan_desc,2)} y el precio total de todas las barras vendidad es {round(pan_desc*barras_vend_nodia,2)}")