num1 = 1
num2 = 1
while (num1 != 10) or (num2 != 10):
    print(f"{num1} * {num2} = {num1*num2}")
    if num2 == 10:
        num1 = num1 + 1
        num2 = 0
    num2 = num2 + 1
