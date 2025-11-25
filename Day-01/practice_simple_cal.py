# calcultor_v1.py

print("-- simple calculator --")

1.  # Get user inpute
# using float() so decimals work (e.g., 5.5 + 2.1, etc)
num1 = float(input("Enter first number:"))
operator = input("Enter operator (+, -, /, *): ")
num2 = float(input("Enter second number:"))

# 2. perform calculation
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
    # Basic protection againt devided by zero(0)
    if num2 != 0:
        result = num1 / num2
        print("fResult: {result}")
    else:
        print("Error cannot divid by zero!")
else:
    print("invalid operator entered.")
