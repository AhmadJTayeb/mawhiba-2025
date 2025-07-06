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
* **Strings:** Text values, e.g., `name = "Alex"`
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

### 📂 **Python Data Structures**

#### **Lists (mutable)**

Lists are collections of items that can be changed.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
```

#### **Tuples (immutable)**

Tuples are collections of items that cannot be changed.

```python
colors = ("red", "green", "blue")
```

#### **Dictionaries**

Dictionaries store data as key-value pairs.

```python
student = {"name": "Alex", "age": 15, "grade": "10th"}
print(student["age"])  # Output: 15
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

### ⚙️ **Functions and Modules**

#### **Functions**

Reusable blocks of code.

```python
def greet(name):
    return "Hello, " + name

print(greet("Maria"))
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

### ✏️ **Mini Exercises**

1. Create a list of five fruits. Use a loop to print each fruit with its index number.
2. Write a program that asks for two numbers from the user, converts them to integers, and then prints their sum, difference, product, and quotient.
3. Create a dictionary to store the names and scores of three students. Calculate and print the average score.

### 📌 **Summary**

* Variables store data; Python supports various data types.
* Type conversion helps manage data types effectively.
* Lists and dictionaries organize data.
* Functions help reuse code; modules organize functions.
* Pandas simplifies data analysis from structured sources.

### 🏠 **Homework**

Write a Python program that:

1. Asks the user how many items they want to enter.
2. Collects item names and their prices from user input.
3. Stores the data in a dictionary.
4. Calculates and prints the total and average prices.
5. Saves the data to a CSV file using `pandas`.

**Example:**

```python
import pandas as pd

items = {}
n = int(input("How many items do you want to enter? "))

for i in range(n):
    item_name = input(f"Enter name of item {i+1}: ")
    item_price = float(input(f"Enter price of {item_name}: "))
    items[item_name] = item_price

# Display total and average
total = sum(items.values())
average = total / len(items)

print("Total price:", total)
print("Average price:", average)

# Save to CSV
df = pd.DataFrame(list(items.items()), columns=['Item', 'Price'])
df.to_csv("my_market_data.csv", index=False)
print("Data saved to my_market_data.csv")
```
