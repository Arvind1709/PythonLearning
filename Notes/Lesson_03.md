# Lesson 03 - Input and Output

## Topics Covered

- print()
- input()
- f-strings
- int()
- float()

## Example

```python
name = input("Enter your name: ")
print(f"Welcome {name}")
```

## Important

`input()` always returns a string.

Example

```python
age = input("Enter age: ")
print(type(age))
```

Output

```
<class 'str'>
```

To convert:

```python
age = int(input("Enter age: "))
```

## New Functions Learned

- print()
- input()
- int()
- float()
- str()
- type()

## Mini Project

Student Profile

## Common Mistakes

Adding an integer to a string:

```python
age = input("Age: ")
print(age + 10)
```

Correct:

```python
age = int(input("Age: "))
print(age + 10)
```