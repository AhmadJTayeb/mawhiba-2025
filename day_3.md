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

### ✅ Summary

* Pandas makes it easy to load, inspect, filter, and clean data
* Grouping and aggregation are essential for summarizing data
* Always inspect your dataset before analysis
* Practice transforming and querying data to build strong data skills