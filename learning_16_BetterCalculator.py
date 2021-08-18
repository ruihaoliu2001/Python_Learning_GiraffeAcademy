
num1 = float(input("Enter first num: "))
op = input("Enter operator: ")
num2 = float(input("Enter second num: "))

def calculator():
    if op == "+":
        num3 = num1 + num2
        print(num3)
    elif op == "-":
        num3 = num1 - num2
        print(num3)
    elif op == "*":
        num3 = num1 * num2
        print(num3)
    elif op == "/":
        num3 = num1 / num2
        print(num3)
    else:
        print("Invalid Operator")


calculator()