choose = input("choose one for calculation (+, -, *, /, ): ")

if (choose == "+"):
    num1 = int(input("enter a num1: "))
    num2 = int(input("enter a num2: "))
    cal = num1 + num2
elif (choose == "-"):
    num1 = int(input("enter a num1: "))
    num2 = int(input("enter a num2: "))
    cal = num1 - num2
elif (choose == "*"):
    num1 = int(input("enter a num1: "))
    num2 = int(input("enter a num2: "))
    cal = num1 * num2
elif (choose == "/"):
    num1 = int(input("enter a num1: "))
    num2 = int(input("enter a num2: "))
    cal = num1 / num2
else :
    print("value is not valid")

print(cal)




