num1 = float(input("enter a number: "))
opr = input("enter an operator: ")
num2 = float(input("enter another number: "))

if opr == '+':
    print(num1 + num2)

elif opr == '-':
    print(num1 - num2)

elif opr == '*':
    print(num1 * num2)

elif opr == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1 / num2)

elif opr == '%':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1 % num2)

elif opr == '**':
    print(num1 ** num2)

elif opr == '//':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1 // num2)

else:
    print("Error: Invalid operator")