# Lesson 04 - Operators

## Objective

Learn how to perform calculations, compare values, and use operators in Python.

---

# What is an Operator?

An operator is a symbol that performs an operation on one or more values.

Example:

```python
10 + 20
```

Here:

- `10` and `20` are operands.
- `+` is the operator.

---

# Arithmetic Operators

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Power | `2 ** 5` | `32` |

---

# Example

```python
a = 20
b = 10

print(f"Addition       : {a + b}")
print(f"Subtraction    : {a - b}")
print(f"Multiplication : {a * b}")
print(f"Division       : {a / b}")
print(f"Floor Division : {a // b}")
print(f"Modulus        : {a % b}")
print(f"Power          : {a ** b}")
```

---

# Calculator Example

```python
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
power = first_number ** second_number

print()
print("=" * 40)
print("Calculator Result")
print("=" * 40)

print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")
print(f"Floor Division : {floor_division}")
print(f"Modulus        : {modulus}")
print(f"Power          : {power}")
```

---

# Important Concepts

## Division (`/`)

Always returns a floating-point value.

Example:

```python
20 / 10
```

Output:

```
2.0
```

---

## Floor Division (`//`)

Returns the integer part of the division result.

Example:

```python
15 // 2
```

Output:

```
7
```

---

## Modulus (`%`)

Returns the remainder after division.

Example:

```python
15 % 2
```

Output:

```
1
```

Common use:

```python
number = 20

print(number % 2 == 0)
```

Output:

```
True
```

Used to check whether a number is even or odd.

---

## Power (`**`)

Raises a number to the specified power.

Example:

```python
2 ** 5
```

Output:

```
32
```

---

# Operator Precedence

Python follows mathematical precedence rules.

Example:

```python
print(5 + 2 * 3)
```

Output:

```
11
```

Because multiplication happens before addition.

To change the order:

```python
print((5 + 2) * 3)
```

Output:

```
21
```

---

# C# Comparison

| Python | C# |
|---------|----|
| `+` | `+` |
| `-` | `-` |
| `*` | `*` |
| `/` | `/` |
| `//` | No direct equivalent |
| `%` | `%` |
| `**` | `Math.Pow()` |

---

# Best Practices

- Use meaningful variable names.

```python
first_number
second_number
```

instead of

```python
num1
num2
```

- Store calculations in variables if they are reused or complex.

```python
addition = first_number + second_number
```

- Use f-strings for output.

```python
print(f"Addition : {addition}")
```

---

# Common Mistakes

## Forgetting that `/` returns a float

```python
print(20 / 10)
```

Output:

```
2.0
```

---

## Division by zero

```python
print(10 / 0)
```

Raises:

```
ZeroDivisionError
```

We'll learn how to handle this in the Exception Handling lesson.

---

# Interview Questions

### 1. What is the difference between `/` and `//`?

- `/` returns the exact division result as a float.
- `//` returns the floor (rounded down) result.

---

### 2. What does `%` do?

It returns the remainder after division.

---

### 3. What is `**` used for?

It performs exponentiation (power).

---

### 4. How do you check if a number is even?

```python
number % 2 == 0
```

---

# Revision Points

- Operators perform operations on values.
- `/` always returns a float.
- `//` performs floor division.
- `%` returns the remainder.
- `**` calculates powers.
- Python follows operator precedence.
- Parentheses `()` can change evaluation order.

---

# Practice Exercises

1. Write a program to calculate the area of a rectangle.
2. Write a program to calculate the area of a circle.
3. Ask the user for two numbers and display all arithmetic operations.
4. Check whether a number is even or odd using `%`.
5. Calculate the square and cube of a number using `**`.