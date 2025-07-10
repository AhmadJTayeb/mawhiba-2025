## 📊 Day 3 Notes: Data Analysis with Pandas

### 🎯 Objectives

By the end of this lesson, you should be able to:

* Understand what Pandas is and why it's useful
* Load and explore structured data from CSV files
* Select, filter, and sort data in a DataFrame
* Handle missing values and clean data effectively
* Perform aggregation and grouping for summaries
* Prepare data for visualization or deeper analysis

---

### 📦 1. What is Pandas?

Pandas is a powerful Python library for handling structured/tabular data. It makes data cleaning, analysis, and transformation easy.

#### Key Data Structures:
- `Series`: A one-dimensional labeled array (like a column)
- `DataFrame`: A two-dimensional table (like a spreadsheet)

#### What You Can Do With Pandas:
- Read/write data from CSV, Excel, JSON, SQL
- Clean and transform messy data
- Perform fast calculations and aggregations
- Prepare data for charts or machine learning

---

### 📥 2. Reading and Inspecting Data

#### Sample CSV (`products.csv`):
```
name,category,price,stock
Apple,Fruit,1.2,100
Banana,Fruit,0.8,150
Carrot,Vegetable,0.6,200
Milk,Beverage,1.5,80
Water,Drink,1.0,120
Chips,Snack,1.3,90
Notebook,Stationery,2.5,60
Pen,Stationery,,110
Juice,Beverage,1.8,70
Cheese,Dairy,2.0,50
```

```python
import pandas as pd

# Load data from CSV
df = pd.read_csv("products.csv")
```

#### Previewing Data
```python
print(df.head())        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.shape)         # Rows and columns
print(df.columns)       # Column names
print(df.dtypes)        # Data types
print(df.info())        # Summary
print(df.describe())    # Numeric summary
```

---

### 🔍 3. Selecting and Filtering Data

#### Select Columns:
```python
df["price"]
df[["name", "price"]]
```

#### Select Rows:
```python
df.loc[0]               # First row
df.iloc[0:5]            # First 5 rows
```

#### Filter Rows:
```python
df[df["price"] > 1.0]
df[df["name"] == "Apple"]
```

#### Combine Conditions:
```python
df[(df["price"] > 1) & (df["price"] < 3)]
df[(df["category"] == "Fruit") | (df["category"] == "Vegetable")]
```

---

### 🧹 4. Cleaning Data

#### Identify Missing Values:
```python
df.isnull()
df.isnull().sum()
```

#### Handle Missing Values:
```python
df.dropna()                # Remove rows with missing values
df.fillna(0)               # Fill with 0
df.fillna("Unknown")      # Fill with text
```

#### Rename Columns:
```python
df.rename(columns={"price": "cost"}, inplace=True)
```

#### Convert Data Types:
```python
df["price"] = df["price"].astype(float)
```

#### Strip Whitespace:
```python
df["name"] = df["name"].str.strip()
```

---

### 📊 5. Sorting and Aggregating

#### Sorting:
```python
df.sort_values(by="price", ascending=False)
df.sort_values(by=["category", "price"])
```

#### Summary Statistics:
```python
df["price"].mean()
df["price"].max()
df["price"].min()
df["price"].sum()
df["price"].std()
```

#### Group By:
```python
df.groupby("category")["price"].mean()
df.groupby("category")["price"].agg(["mean", "max", "min"])
```

#### Value Counts:
```python
df["category"].value_counts()
```

---

### 🧠 6. Example Case Study

#### Dataset (`market_data.csv`):
```
name,category,price,stock
PS5 Console,Console,499.99,15
DualSense Controller,Accessory,69.99,35
Charging Station,Accessory,29.99,40
Headset,Accessory,89.99,20
PS5 Camera,Accessory,59.99,10
Spider-Man: Miles Morales,Game,49.99,50
Horizon Forbidden West,Game,59.99,45
Elden Ring,Game,59.99,30
FIFA 24,Game,69.99,60
Storage Expansion 1TB,Accessory,129.99,8
Gran Turismo 7,Game,54.99,35
Ratchet & Clank: Rift Apart,Game,49.99,25
Sackboy: A Big Adventure,Game,39.99,30
Vertical Stand,Accessory,24.99,20
HDMI 2.1 Cable,Accessory,19.99,50
Game Voucher Card,Accessory,20.00,75
The Last of Us Part I,Game,69.99,40
PlayStation Plus 12-Month,Subscription,59.99,200
Gift Card $50,Gift,50.00,100
Gift Card $100,Gift,100.00,70
```


Given a CSV file `market_data.csv` with columns `name`, `category`, `price`, `stock`:

```python
# Load data
market = pd.read_csv("market_data.csv")

# Top 3 most expensive items
market.sort_values(by="price", ascending=False).head(3)

# Average price
avg_price = market["price"].mean()
print("Average price:", avg_price)

# Group by category
market.groupby("category")["price"].mean()

# Items with missing prices
market[market["price"].isnull()]
```

---

### ✏️ Mini Exercises

Use the following tasks to reinforce your understanding of working with Pandas and analyzing real data.

1. **Read and Display Data:**
   - Load `market_data.csv` into a DataFrame.
   - Display the first 10 rows using `head()`.

2. **Basic Filtering:**
   - Show all products in the "Game" category.
   - Display only the items that cost more than $60.

3. **Column Selection and Statistics:**
   - Display only the `name`, `category`, and `price` columns.
   - Find the average price of all items.
   - Find the total stock across all products.

4. **Sorting and Ranking:**
   - Sort the products by `stock` in descending order.
   - Find the top 3 products with the highest price.

5. **Data Cleaning:**
   - Show any items with missing prices.
   - Fill missing prices with the average price of their category.

6. **GroupBy Analysis:**
   - Group products by category and show the average and max price per category.
   - Count how many items are in each category.

7. **New Calculated Columns:**
   - Add a column `total_value = price * stock`.
   - Sort and display the top 5 products with the highest total value.

8. **Challenge Task:**
   - Group by category, and for each group, show:
     - Total number of products
     - Average price
     - Total value (sum of `price * stock`)

---

### 🔍 Bonus: Creating DataFrames from Scratch

```python
data = {
    "name": ["Apple", "Banana", "Carrot"],
    "price": [1.2, 0.8, 0.6],
    "category": ["Fruit", "Fruit", "Vegetable"]
}
df = pd.DataFrame(data)
print(df)
```

---

### 🔄 7. Combining DataFrames (Merging & Concatenating)

In real projects, you often need to combine data from multiple sources.

#### Sample Data for Examples:

**customers.csv:**
```
customer_id,name,city
1,Mohammed,Riyadh
2,Fatima,Jeddah
3,Abdullah,Dammam
4,Aisha,Riyadh
```

**orders.csv:**
```
order_id,customer_id,product,amount
101,1,Laptop,2500
102,2,Phone,800
103,1,Mouse,50
104,3,Keyboard,120
105,5,Tablet,600
```

**products_info.csv:**
```
product,category,supplier
Laptop,Electronics,TechCorp
Phone,Electronics,MobilePlus
Mouse,Accessories,TechCorp
Keyboard,Accessories,InputMaster
Tablet,Electronics,TabletPro
```

#### Loading the Data:
```python
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products_info = pd.read_csv("products_info.csv")
```

#### Merging DataFrames (Like SQL JOIN):
```python
# Inner Join - only matching records
customer_orders = customers.merge(orders, on='customer_id')
print(customer_orders)

# Left Join - keep all customers, even without orders
all_customers = customers.merge(orders, on='customer_id', how='left')
print(all_customers)

# Join with different column names
orders_with_products = orders.merge(products_info, 
                                  left_on='product', 
                                  right_on='product')
```

#### Concatenating DataFrames:
```python
# Sample data for concatenation
new_customers = pd.DataFrame({
    'customer_id': [5, 6],
    'name': ['Sara', 'Ali'],
    'city': ['Mecca', 'Medina']
})

# Stack vertically (add new rows)
all_customers = pd.concat([customers, new_customers], ignore_index=True)

# Side by side (add new columns) - rarely used
# combined = pd.concat([df1, df2], axis=1)
```

---

### 🔧 8. Advanced Data Manipulation

#### Applying Custom Functions:

**Sample Sales Data:**
```python
sales_data = pd.DataFrame({
    'product': ['iPhone', 'Samsung Galaxy', 'iPad', 'MacBook'],
    'price_usd': [999, 850, 599, 1299],
    'quantity': [50, 75, 30, 20],
    'discount_percent': [5, 10, 0, 15]
})
```

#### Using Apply for Calculations:
```python
# Calculate price in SAR (1 USD = 3.75 SAR)
sales_data['price_sar'] = sales_data['price_usd'].apply(lambda x: x * 3.75)

# Calculate total revenue per product (Using apply with axis=1)
# axis=1 means apply the function to each ROW (across columns)
# axis=0 would mean apply to each COLUMN (down rows)
sales_data['revenue'] = sales_data.apply(
    lambda row: row['price_usd'] * row['quantity'] * (1 - row['discount_percent']/100),
    axis=1
)

# Alternative methods to calculate revenue:

# Method 1: Vectorized operations (FASTEST - recommended)
sales_data['revenue_v1'] = sales_data['price_usd'] * sales_data['quantity'] * (1 - sales_data['discount_percent']/100)

# Method 2: Using eval (good for complex expressions)
sales_data['revenue_v2'] = sales_data.eval('price_usd * quantity * (1 - discount_percent/100)')

# Method 3: Using a loop (SLOWEST - avoid for large datasets)
revenue_list = []
for index, row in sales_data.iterrows():
    revenue = row['price_usd'] * row['quantity'] * (1 - row['discount_percent']/100)
    revenue_list.append(revenue)
sales_data['revenue_v3'] = revenue_list

# Performance comparison:
# Vectorized (Method 1) > eval (Method 2) > apply (original) > loop (Method 3)
# For large datasets, always prefer vectorized operations!

# Categorize products by price
def price_category(price):
    if price < 600:
        return 'Budget'
    elif price < 1000:
        return 'Mid-range'
    else:
        return 'Premium'

sales_data['category'] = sales_data['price_usd'].apply(price_category)
```

#### String Operations:
```python
# Sample customer data with messy names
messy_customers = pd.DataFrame({
    'name': ['  MOHAMMED BIN SALMAN  ', 'fatima abdullah', 'KHALID-IBRAHIM', 'aisha_mohammed'],
    'email': ['mohammed@email.com', 'FATIMA@EMAIL.COM', 'khalid@email.com', 'aisha@email.com']
})

# Clean and standardize
messy_customers['name_clean'] = messy_customers['name'].str.strip().str.title()
messy_customers['email_clean'] = messy_customers['email'].str.lower()
messy_customers['first_name'] = messy_customers['name_clean'].str.split().str[0]

# Check for specific patterns
messy_customers['has_underscore'] = messy_customers['name'].str.contains('_')
```

#### Map Values for Quick Transformations:
```python
# Convert categories to codes
category_mapping = {'Budget': 'B', 'Mid-range': 'M', 'Premium': 'P'}
sales_data['category_code'] = sales_data['category'].map(category_mapping)
```

---

### 🧹 9. Data Quality & Validation

#### Handling Duplicates:

**Sample Data with Duplicates:**
```python
student_grades = pd.DataFrame({
    'student_id': [1, 2, 3, 2, 4, 3, 5],
    'name': ['Abdullah', 'Fatima', 'Khalid', 'Fatima', 'Aisha', 'Khalid', 'Sara'],
    'subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Math', 'Science'],
    'grade': [85, 92, 78, 92, 88, 78, 95]
})
```

#### Finding and Removing Duplicates:
```python
# Check for duplicates
print("Duplicate rows:")
print(student_grades.duplicated())

# Count duplicates
print(f"Number of duplicates: {student_grades.duplicated().sum()}")

# Remove exact duplicates
clean_grades = student_grades.drop_duplicates()

# Remove duplicates based on specific columns
unique_students = student_grades.drop_duplicates(subset=['student_id', 'subject'])

# Keep last occurrence instead of first
latest_grades = student_grades.drop_duplicates(subset=['student_id', 'subject'], 
                                             keep='last')
```

#### Data Validation:
```python
# Check data quality
print("Data Overview:")
print(f"Shape: {student_grades.shape}")
print(f"Missing values: {student_grades.isnull().sum()}")
print(f"Unique students: {student_grades['student_id'].nunique()}")

# Validate grade ranges
valid_grades = student_grades['grade'].between(0, 100).all()
print(f"All grades valid (0-100): {valid_grades}")

# Find outliers
grade_stats = student_grades['grade'].describe()
print("Grade statistics:")
print(grade_stats)
```

---

### 💾 10. Saving Your Work

#### Export to Different Formats:
```python
# Save to CSV (most common)
student_grades.to_csv('student_grades_clean.csv', index=False)

# Save to Excel with multiple sheets
with pd.ExcelWriter('school_data.xlsx') as writer:
    student_grades.to_excel(writer, sheet_name='Grades', index=False)
    sales_data.to_excel(writer, sheet_name='Sales', index=False)

# Save to JSON
student_grades.to_json('grades.json', orient='records', indent=2)

# Save only specific columns
student_grades[['name', 'subject', 'grade']].to_csv('summary.csv', index=False)

# Save with custom settings
student_grades.to_csv('grades_formatted.csv', 
                     index=False, 
                     sep=';',  # Use semicolon separator
                     encoding='utf-8')
```

---

### 🔍 11. Advanced Filtering & Querying

#### Using Query Method (SQL-like):
```python
# Sample inventory data
inventory = pd.DataFrame({
    'item': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Tablet', 'Phone'],
    'price': [2500, 50, 120, 800, 600, 1200],
    'stock': [15, 100, 45, 25, 30, 60],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Electronics'],
    'supplier': ['TechCorp', 'TechCorp', 'InputMaster', 'DisplayPro', 'TabletPro', 'MobilePlus']
})

# Query examples
expensive_items = inventory.query('price > 500 and stock > 20')
tech_accessories = inventory.query('category == "Accessories" and supplier == "TechCorp"')

# Using isin for multiple values
electronics = inventory[inventory['supplier'].isin(['TechCorp', 'MobilePlus'])]

# Combine with string operations
cheap_electronics = inventory.query('price < 1000 and category == "Electronics"')
```

---

### 📅 12. Working with Dates

#### Sample Sales Data with Dates:
```python
sales_timeline = pd.DataFrame({
    'date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-01-25', '2024-02-14'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Mouse', 'Keyboard'],
    'amount': [2500, 1200, 600, 50, 120],
    'customer': ['Mohammed', 'Fatima', 'Abdullah', 'Aisha', 'Sara']
})

# Convert to datetime
sales_timeline['date'] = pd.to_datetime(sales_timeline['date'])

# Extract date components
sales_timeline['year'] = sales_timeline['date'].dt.year
sales_timeline['month'] = sales_timeline['date'].dt.month
sales_timeline['day_name'] = sales_timeline['date'].dt.day_name()

# Filter by date ranges
jan_sales = sales_timeline[sales_timeline['date'].dt.month == 1]
recent_sales = sales_timeline[sales_timeline['date'] >= '2024-02-01']

# Group by month
monthly_sales = sales_timeline.groupby(sales_timeline['date'].dt.month)['amount'].sum()
```

---

### 🚨 13. Error Handling & Best Practices

#### Common Error Prevention:
```python
# Check if file exists before reading
import os
if os.path.exists('data.csv'):
    df = pd.read_csv('data.csv')
else:
    print("File not found!")

# Check if column exists before using
if 'price' in inventory.columns:
    avg_price = inventory['price'].mean()
    print(f"Average price: {avg_price}")
else:
    print("Price column not found!")

# Handle division by zero
def safe_profit_margin(price, cost):
    if cost == 0:
        return 0
    return (price - cost) / price * 100

# Memory usage check for large datasets
print("Memory usage:")
print(inventory.memory_usage(deep=True))
```

#### Performance Tips:
```python
# Use vectorized operations instead of loops
# BAD: slow loop
# for i in range(len(df)):
#     df.loc[i, 'new_col'] = df.loc[i, 'price'] * 1.1

# GOOD: vectorized operation
inventory['price_with_tax'] = inventory['price'] * 1.1

# Use query for complex filtering (often faster)
result = inventory.query('price > 500 and stock < 50')
```

---

### ✏️ Advanced Mini Exercises

**Complete these exercises using the sample data provided above:**

1. **Data Combination:**
   - Merge customers with orders to show customer names with their order amounts
   - Find customers who haven't placed any orders (hint: use left join)

2. **String Manipulation:**
   - Clean the messy customer names and extract first names
   - Create email usernames from email addresses (part before @)

3. **Duplicate Management:**
   - Find students who have duplicate grades in the same subject
   - Keep only the highest grade for each student-subject combination

4. **Advanced Filtering:**
   - Use query to find electronics under 1000 SAR with stock above 20
   - Find all products from suppliers containing "Tech" in the name

5. **Date Analysis:**
   - Calculate total sales per month from the sales timeline
   - Find the day of the week with highest sales

6. **Data Export Challenge:**
   - Create an Excel file with 3 sheets: Customers, Orders, and Summary
   - Export only profitable products (price > 100) to a CSV

7. **Custom Functions:**
   - Create a function to categorize stock levels (Low: <20, Medium: 20-50, High: >50)
   - Apply it to create a new stock_level column

8. **Data Validation:**
   - Check if all prices are positive numbers
   - Identify any products with suspicious data (price = 0 or negative stock)

---

### ✅ Summary

* Pandas makes it easy to load, inspect, filter, and clean data
* Grouping and aggregation are essential for summarizing data
* Always inspect your dataset before analysis
* Practice transforming and querying data to build strong data skills