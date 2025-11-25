# calc_v2.py
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


print("--- Smart Calculator v2 ---")

while True:
    print("\nOptions: +, -, *, / or 'q' to quit")
    user_input = input("Enter operator: ")

    if user_input == 'q':
        print("Goodbye!")
        break

    if user_input in ('+', '-', '*', '/'):
        try:
            # We put this inside try/except to catch non-number inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == '+':
                print(f"Result: {add(num1, num2)}")
            elif user_input == '-':
                print(f"Result: {subtract(num1, num2)}")
            elif user_input == '*':
                print(f"Result: {multiply(num1, num2)}")
            elif user_input == '/':
                print(f"Result: {divide(num1, num2)}")

        except ValueError:
            print("Oops! That was not a valid number. Try again.")
    else:
        print("Invalid Operator. Please try again.")
