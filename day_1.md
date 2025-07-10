## 📚 Day 1 Notes: Python & Data Basics

### 🐍 **What is Python?**

Python is a versatile, high-level programming language known for readability and simplicity. It's widely used in:

* Web Development
* Data Science and Analytics
* Machine Learning and AI
* Automation and Scripting

### 🛠️ **Python Fundamentals**

#### **Variables & Data Types**

* **Variables:** Containers for storing data values.
* **Integers:** Whole numbers, e.g., `age = 25`
* **Floats:** Decimal numbers, e.g., `price = 9.99`
* **Strings:** Text values, e.g., `name = "Ahmad"`
* **Booleans:** True or False, e.g., `is_student = True`

#### **Type Conversion Functions**

* `int()` - Convert to integer

  ```python
  age = int("25")
  ```
* `float()` - Convert to float

  ```python
  price = float("9.99")
  ```
* `str()` - Convert to string

  ```python
  number = str(123)
  ```

#### **Operators**

* Arithmetic: `+`, `-`, `*`, `/`, `%` (modulo)
* Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`

#### **Input & Output**

* `input()`: Get user input
* `print()`: Display output

```python
name = input("What's your name? ")
print("Hello, " + name)
```

### 📝 **String Formatting Methods**

Python offers multiple ways to format strings:

#### **f-strings (Recommended - Python 3.6+)**

```python
name = "Ahmad"
age = 25
print(f"Hello, {name}. You are {age} years old.")
print(f"Next year you'll be {age + 1} years old.")
```

#### **.format() Method**

```python
name = "Ahmad"
age = 25
print("Hello, {}. You are {} years old.".format(name, age))
print("Hello, {n}. You are {a} years old.".format(n=name, a=age))
```

#### **% Formatting (Older Style)**

```python
name = "Ahmad"
age = 25
print("Hello, %s. You are %d years old." % (name, age))
```

### 📂 **Python Data Structures**

#### **Lists (mutable)**

Lists are collections of items that can be changed.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
```

#### **List Comprehensions**

A powerful way to create lists:

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i**2)

# List comprehension
squares = [i**2 for i in range(10)]

# With condition
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

#### **Tuples (immutable)**

Tuples are collections of items that cannot be changed.

```python
colors = ("red", "green", "blue")
```

#### **Dictionaries**

Dictionaries store data as key-value pairs.

```python
student = {"name": "Ahmad", "age": 15, "grade": "10th"}
print(student["age"])  # Output: 15
```

#### **Sets**

Sets are collections of unique items (no duplicates).

```python
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'} - duplicates removed

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))      # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
```

### 🔄 **Control Flow**

#### **Conditionals (`if`, `elif`, `else`)**

Conditionals allow decisions based on certain conditions.

```python
score = 85
if score > 90:
    print("Excellent")
elif score > 70:
    print("Good job")
else:
    print("Needs improvement")
```

#### **Loops**

Loops repeat actions multiple times.

* **For Loop:**

```python
for fruit in fruits:
    print(fruit)
```

* **While Loop:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 🛡️ **Error Handling (Try/Except)**

Error handling helps your program continue running even when errors occur.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 📁 **File Handling Basics**

#### **Reading Files**

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra whitespace
```

#### **Writing Files**

```python
# Write to file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nNew line added")
```

### 📅 **Basic Date/Time Handling**

```python
from datetime import datetime, date

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 14:30:25.123456

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-01-15 14:30:25

# Working with dates
today = date.today()
print(today)  # 2024-01-15
```

### ⚙️ **Functions and Modules**

#### **Functions**

Reusable blocks of code.

```python
def greet(name):
    return "Hello, " + name

print(greet("Maria"))
```

#### **Comments and Documentation**

```python
# Single line comment

"""
Multi-line comment
or docstring
"""

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        float: Area of rectangle
    """
    return length * width
```

#### **Import Statements**

```python
# Import entire module
import math
print(math.sqrt(16))

# Import specific function
from math import sqrt, pi
print(sqrt(16))

# Import with alias
import pandas as pd
import matplotlib.pyplot as plt

# Import multiple items
from datetime import datetime, timedelta
```

#### **Math Module**

Common mathematical functions:

* `math.sqrt(x)` - Square root
* `math.pow(x, y)` - x raised to the power of y
* `math.ceil(x)` - Rounds up to nearest integer
* `math.floor(x)` - Rounds down to nearest integer
* `math.pi` - Mathematical constant Pi

```python
import math
print(math.sqrt(25))  # Output: 5.0
print(math.pi)        # Output: 3.141592653589793
```

### 📈 **Structured Data with Pandas**

Pandas is a Python library to analyze structured data.

#### **Basic Pandas Operations**

```python
import pandas as pd
# Reading data from a CSV file
data = pd.read_csv("data.csv")
print(data.head())  # shows the first 5 rows
print(data.describe())  # basic statistics

# Creating a CSV file from a dictionary
data_dict = {
    "Item": ["apple", "banana", "milk"],
    "Price": [1.2, 0.5, 2.5]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data_dict)

# Saving the DataFrame to a CSV file
df.to_csv("example_data.csv", index=False)
print("CSV file 'example_data.csv' created successfully.")
```

### 🎯 **Python Best Practices**

#### **Naming Conventions**

```python
# Variables and functions: lowercase_with_underscores
user_name = "Ahmad"
def calculate_total():
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
PI = 3.14159
MAX_ATTEMPTS = 3

# Classes: PascalCase
class StudentRecord:
    pass
```

#### **Code Style**

```python
# Good spacing
x = 5 + 3
if x > 0:
    print("Positive")

# Use meaningful variable names
total_price = item_price * quantity  # Good
tp = ip * q  # Bad
```

### ✏️ **Mini Exercises**

1. Create a list of five fruits. Use a loop to print each fruit with its index number.
2. Write a program that asks for two numbers from the user, converts them to integers, and then prints their sum, difference, product, and quotient.
3. Create a dictionary to store the names and scores of three students. Calculate and print the average score.
4. Use a list comprehension to create a list of even numbers from 1 to 20.
5. Write a function that takes a filename and reads the first line, handling potential file errors.
6. Create a program that formats today's date in three different ways using f-strings.

### 📌 **Summary**

* Variables store data; Python supports various data types.
* Type conversion helps manage data types effectively.
* Lists, dictionaries, and sets organize data in different ways.
* String formatting makes output more readable and flexible.
* Error handling makes programs more robust.
* File handling allows reading and writing data.
* Functions help reuse code; modules organize functions.
* Comments and documentation make code more maintainable.
* Pandas simplifies data analysis from structured sources.

### 🏠 **Homework**

Write a Python program that:

1. Asks the user how many items they want to enter.
2. Collects item names and their prices from user input.
3. Stores the data in a dictionary.
4. Calculates and prints the total and average prices.
5. Saves the data to a CSV file using `pandas`.
6. Includes proper error handling for invalid inputs.
7. Uses f-strings for all output formatting.

**Example:**

```python
import pandas as pd
from datetime import datetime

items = {}
try:
    n = int(input("How many items do you want to enter? "))
    
    for i in range(n):
        item_name = input(f"Enter name of item {i+1}: ")
        item_price = float(input(f"Enter price of {item_name}: "))
        items[item_name] = item_price

    # Display total and average
    total = sum(items.values())
    average = total / len(items)

    print(f"Total price: ${total:.2f}")
    print(f"Average price: ${average:.2f}")

    # Save to CSV
    df = pd.DataFrame(list(items.items()), columns=['Item', 'Price'])
    filename = f"market_data_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

except ValueError:
    print("Please enter valid numbers for quantity and prices.")
except Exception as e:
    print(f"An error occurred: {e}")
```
