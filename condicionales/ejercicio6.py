nombre = input("dame nombres: ")
sexo = input("Dime el sexo: ")

sexoup = sexo[:1].upper()
first = nombre[:1].upper()

if (sexoup == "M" and first > "N") or (sexoup == "F" and first < "M"):
    print("Group A")
else:
    print("Group B")