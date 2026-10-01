#Data input
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть дію (+, -, /, *, mod, pow, div): ")

#True when 2nd number is zero
b_is_zero = (b == 0)
#Calculation conditions
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b_is_zero == True:
        print("Division by 0!")
    else:
        print(a / b)
elif operation == "mod":
    if b_is_zero == True:
        print("Division by 0!")
    else:
        print(a % b)
elif operation == "div":
    if b_is_zero == True:
        print("Division by 0!")
    else:
        print(a // b)
elif operation == "pow":
    print(a ** b)
else:
    print("Невідома дія")
