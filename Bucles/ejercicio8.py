altura = int(input("Dime un numero entero: "))
num = ""

for i in range(1, altura):
    num = str(i) + num
    print(num)
    i = i + 1