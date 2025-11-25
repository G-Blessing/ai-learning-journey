# calc_v1.py
print("--- Simple Calculator v1 ---")

# 1. Get User Input
# We use float() so decimals work (e.g., 5.5 + 2.1)
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# 2. Perform Calculation
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    # Basic protection against dividing by zero
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator entered.")
