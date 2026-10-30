altura = int(input("Dime un numero entero: "))
if ( altura%2 == 0 ):
    altura = altura - 1

num = ""

for i in range(1, altura + 1):
    if ( i%2 == 1 ):
        num = str(i) + num
        print(num)