## 📈 Day 4 Notes: Data Visualization with Python

### 🎯 Objectives

By the end of this lesson, you should be able to:

* Understand the purpose and value of data visualization
* Create bar charts, line plots, and pie charts using Matplotlib or Plotly
* Customize visuals with labels, titles, legends, and styles
* Use color schemes and formatting for effective storytelling
* Choose appropriate chart types for different types of data
* Save and export visualizations for presentations and reports

---

### 🎨 1. Why Visualize Data?

* Helps identify trends, outliers, and patterns
* Makes data easier to understand and share
* Supports better decision-making
* Tells a compelling data story

**Example Scenario:** You have a dataset of weekly sales — instead of showing numbers in a table, a line chart quickly highlights upward or downward trends.

---

### 📊 2. Introduction to Matplotlib

Matplotlib is a widely-used Python library for creating static, high-quality visualizations.

#### 2.1 Basic Bar Chart
```python
import matplotlib.pyplot as plt

items = ['Apple', 'Banana', 'Grape']
prices = [1.2, 0.8, 2.0]

plt.bar(items, prices)
plt.title('Fruit Prices')
plt.xlabel('Fruit')
plt.ylabel('Price')
plt.show()
```

#### 2.2 Customizing Appearance
```python
plt.bar(items, prices, color='skyblue')
plt.grid(True)
plt.xticks(rotation=45)
```

#### 2.3 Line Plot
```python
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [100, 120, 80, 150, 200]

plt.plot(days, sales, marker='o')
plt.title('Daily Sales')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.show()
```

#### 2.4 Pie Chart
```python
labels = ['Apple', 'Banana', 'Grape']
quantities = [40, 35, 25]

plt.pie(quantities, labels=labels, autopct='%1.1f%%')
plt.title('Fruit Quantity Share')
plt.show()
```

#### 2.5 Histogram
```python
import numpy as np
import matplotlib.pyplot as plt

# Simulated exam scores out of 100
scores = [55, 62, 68, 71, 74, 75, 77, 78, 79, 80, 81, 85, 87, 89, 90, 91, 93, 94, 95, 98]

plt.hist(scores, bins=7, color='mediumpurple', edgecolor='black')
plt.title('Exam Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

---

### 🌈 3. Interactive Charts with Plotly

Plotly is useful for building interactive, web-based charts.

#### 3.1 Bar Chart
```python
import plotly.express as px
import pandas as pd

data = {
    "Item": ["Apple", "Banana", "Grape"],
    "Price": [1.2, 0.8, 2.0]
}

df = pd.DataFrame(data)
fig = px.bar(df, x='Item', y='Price', title='Fruit Prices')
fig.show()
```

#### 3.2 Line and Pie Charts
```python
# Line plot
df = pd.DataFrame({"Day": days, "Sales": sales})
px.line(df, x='Day', y='Sales', title='Daily Sales').show()

# Pie chart
fig = px.pie(df, values='Sales', names='Day', title='Sales Share by Day')
fig.show()
```

---

### 🧠 4. Choosing the Right Chart

| Chart Type     | Use Case                             |
|----------------|--------------------------------------|
| Bar Chart      | Comparing quantities across groups   |
| Line Chart     | Tracking changes over time           |
| Pie Chart      | Showing percentage parts of a whole  |
| Histogram      | Distribution of numerical data       |

---

### 💾 5. Saving Your Visuals

```python
# Save a Matplotlib plot to a file
plt.savefig("chart.png")
```

For Plotly, you can export interactive charts as HTML files using:
```python
fig.write_html("chart.html")
```

---

### ✏️ 7. Mini Exercises

1. Create a bar chart comparing prices of 5 market items.
2. Plot a line graph showing your weekly allowance over time.
3. Visualize the proportion of expenses using a pie chart.
4. Create a histogram of students' ages from a list.
5. Use Plotly to make an interactive version of any chart.
6. Save one of your charts as an image or HTML file.

---

### 📦 6. Project Example: Sales Dashboard

Let’s bring everything together with a practical, mid-sized example. We’ll create a mini dashboard using Matplotlib to visualize sales performance over a week for multiple items.

#### Dataset
```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
sales_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Apple": [100, 90, 80, 120, 140],
    "Banana": [60, 65, 70, 75, 80],
    "Grape": [30, 40, 50, 45, 55]
}

df = pd.DataFrame(sales_data)
```

#### Line Chart: Sales Trend
```python
plt.plot(df["Day"], df["Apple"], label="Apple", marker='o')
plt.plot(df["Day"], df["Banana"], label="Banana", marker='s')
plt.plot(df["Day"], df["Grape"], label="Grape", marker='^')

plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

#### Bar Chart: Total Sales by Product
```python
total_sales = df.drop(columns="Day").sum()
total_sales.plot(kind="bar", color=["#ff9999", "#99ff99", "#9999ff"])

plt.title("Total Weekly Sales by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
```

#### Pie Chart: Sales Share
```python
plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", colors=["#ff9999", "#99ff99", "#9999ff"])
plt.title("Sales Share by Product")
plt.show()
```

This project gives students practice with:
- Realistic multi-variable data
- Multiple chart types
- Storytelling with visuals
- Color and layout customization
- Combining Matplotlib techniques

---

### 📦 7. Comparison Project Example: Two Markets Price Comparison

Now let's compare prices for the same products from two different markets and visualize the differences.

#### Dataset
```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample product price data from two markets
price_data = {
    "Item": ["Apple", "Banana", "Grape", "Orange", "Mango"],
    "Market A": [1.2, 0.75, 2.0, 1.1, 2.5],
    "Market B": [1.0, 0.85, 2.2, 1.05, 2.8]
}

df_prices = pd.DataFrame(price_data)
```

#### Grouped Bar Chart: Price Comparison
```python
x = range(len(df_prices))

plt.bar([i - 0.2 for i in x], df_prices["Market A"], width=0.4, label="Market A", align='center')
plt.bar([i + 0.2 for i in x], df_prices["Market B"], width=0.4, label="Market B", align='center')
plt.xticks(x, df_prices["Item"])
plt.ylabel("Price")
plt.title("Market Price Comparison")
plt.legend()
plt.tight_layout()
plt.grid(axis='y')
plt.show()
```

#### Line Plot
```python
plt.plot(df_prices["Item"], df_prices["Market A"], marker='o', label='Market A')
plt.plot(df_prices["Item"], df_prices["Market B"], marker='s', label='Market B')
plt.title("Market Prices Over Products")
plt.xlabel("Item")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

This example allows students to:
- Practice with comparative analysis
- Use grouped bars and line plots
- Draw real insights from pricing data between sellers

---

### ✏️ More Practice Tasks

Use the following tasks to practice your data visualization skills. Each includes real-world-style data and uses either Matplotlib or Plotly.

#### 🟩 Basic Visualization

**1. Bar Chart: Fruit Prices**
```python
items = ["Apple", "Banana", "Orange", "Grapes", "Peach", "Watermelon", "Pineapple", "Strawberry", "Blueberry", "Kiwi"]
prices = [1.2, 0.8, 1.5, 2.0, 1.8, 3.0, 2.5, 2.8, 3.2, 1.6]

plt.bar(items, prices)
plt.title("Market Fruit Prices")
plt.xlabel("Fruit")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
```

**2. Line Chart: Weekly Spending**
```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon2", "Tue2", "Wed2", "Thu2", "Fri2", "Sat2", "Sun2"]
spending = [5, 7, 6, 8, 10, 12, 9, 6, 11, 13, 8, 7, 9, 14]

plt.plot(days, spending, marker='o')
plt.title("2-Week Spending Trend")
plt.xlabel("Day")
plt.ylabel("Amount Spent")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**3. Pie Chart: Daily Activity Split**
```python
labels = ["School", "Homework", "Free Time", "Chores", "Sleep"]
hours = [6, 2, 5, 2, 9]

plt.pie(hours, labels=labels, autopct='%1.1f%%')
plt.title("How I Spend My Day")
plt.show()
```

**4. Histogram: Exam Scores**
```python
scores = [65, 70, 75, 80, 85, 90, 70, 72, 74, 78, 82, 88, 91, 93, 95, 68, 76, 81, 87, 89, 92, 96, 97, 99, 100]
plt.hist(scores, bins=7, color='skyblue', edgecolor='black')
plt.title("Exam Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

#### 🧩 Plotly Extensions

**5. Convert a Bar Chart to Plotly**
```python
import plotly.express as px
import pandas as pd

items = ["Apple", "Banana", "Orange", "Grapes", "Peach", "Watermelon", "Pineapple", "Strawberry", "Blueberry", "Kiwi"]
prices = [1.2, 0.8, 1.5, 2.0, 1.8, 3.0, 2.5, 2.8, 3.2, 1.6]

data = {"Fruit": items, "Price": prices}
df = pd.DataFrame(data)
fig = px.bar(df, x="Fruit", y="Price", title="Interactive Fruit Prices")
fig.show()
```

**6. Create an Interactive Line Plot**
```python
import plotly.express as px
import pandas as pd

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon2", "Tue2", "Wed2", "Thu2", "Fri2", "Sat2", "Sun2"]
spending = [5, 7, 6, 8, 10, 12, 9, 6, 11, 13, 8, 7, 9, 14]

df_spend = pd.DataFrame({"Day": days, "Spending": spending})
fig = px.line(df_spend, x="Day", y="Spending", title="2-Week Spending Trend")
fig.show()
```

---

### ✅ Summary

* Visualization enhances understanding and communication
* Matplotlib is great for static charts; Plotly for interactive ones
* Customize titles, labels, and colors for clarity and appeal
* Choose the right chart for the story your data tells
* Save charts to share them in reports or presentations
