def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:

    choice = input("Choose + - * / or q to quit: ")

    if choice == "q":
        break

    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    if choice == "+":
        print(add(num1, num2))

    elif choice == "-":
        print(subtract(num1, num2))

    elif choice == "*":
        print(multiply(num1, num2))

    elif choice == "/":
        print(divide(num1, num2))

    else:
        print("Invalid choice")