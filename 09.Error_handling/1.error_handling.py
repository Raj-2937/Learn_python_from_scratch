# Basic Error Handling in Python

## Definition

**Error handling** in Python is the process of detecting and handling errors so that the program continues running without crashing. Python uses `try`, `except`, `else`, and `finally` blocks to manage errors.

## Syntax

```python
try:
    # Code that may cause an error
except:
    # Handle the error
```

## Example 1: ZeroDivisionError

```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Output

```
You cannot divide by zero.
```

---

## Example 2: ValueError

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a valid number.")
```

### Example Output

```
Enter your age: abc
Please enter a valid number.
```

---

## Example 3: else Block

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)
```

### Example Output

```
Enter a number: 25
You entered: 25
```

---

## Example 4: finally Block

```python
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program finished.")
```

### Output

```
File not found.
Program finished.
```

## Advantages of Error Handling

- Prevents the program from crashing.
- Makes programs more reliable.
- Helps identify and fix errors.
- Improves user experience.
- Makes code easier to maintain.
