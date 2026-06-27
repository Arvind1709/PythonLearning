# # Take inputs from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Print an empty line for spacing
# print()

# # Perform calculations and print results with formatting
# print(f"Addition       : {num1 + num2}")
# print(f"Subtraction    : {num1 - num2}")
# print(f"Multiplication : {num1 * num2}")
# print(f"Division       : {num1 / num2}")
# print(f"Floor Division : {num1 // num2}")
# print(f"Modulus        : {num1 % num2}")
# print(f"Power          : {num1 ** num2}")

# ==========================================
# File: calculator.py
# Lesson 04 - Arithmetic Operators
# ==========================================

# Read input from the user
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Perform calculations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
power = first_number ** second_number

# Display results
print()
print("=" * 40)
print("        Calculator Result")
print("=" * 40)

print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")
print(f"Floor Division : {floor_division}")
print(f"Modulus        : {modulus}")
print(f"Power          : {power}")

print("=" * 40)