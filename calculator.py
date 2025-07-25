num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = float(num1) + float(num2)
    print(f"The sum of {num1} and {num2} is: {result}")
elif operation == "-":
    result = float(num1) - float(num2)
    print(f"The difference between {num1} and {num2} is: {result}")
elif operation == "*":
    result = float(num1) * float(num2)
    print(f"The product of {num1} and {num2} is: {result}")
elif operation == "/":
    result = float(num1) / float(num2)
    print(f"The quotient of {num1} and {num2} is: {result}")
else:
    print("Invalid operation.")