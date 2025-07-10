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

### 📊 8. Scatter Plots - Showing Relationships

Scatter plots are essential for discovering relationships between two variables.

#### Sample Student Performance Data:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Saudi students' study data
student_data = pd.DataFrame({
    'name': ['Mohammed', 'Fatima', 'Abdullah', 'Aisha', 'Khalid', 'Sara', 'Omar', 'Maryam', 'Ahmed', 'Noura'],
    'study_hours': [2, 8, 5, 7, 3, 6, 4, 9, 1, 7],
    'exam_score': [65, 95, 78, 88, 70, 85, 75, 98, 60, 90],
    'city': ['Riyadh', 'Jeddah', 'Riyadh', 'Mecca', 'Dammam', 'Jeddah', 'Riyadh', 'Mecca', 'Dammam', 'Jeddah']
})
```

#### Basic Scatter Plot:
```python
plt.scatter(student_data['study_hours'], student_data['exam_score'])
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Performance')
plt.grid(True, alpha=0.3)
plt.show()
```

#### Colored by Category:
```python
cities = student_data['city'].unique()
colors = ['red', 'blue', 'green', 'orange']

for i, city in enumerate(cities):
    city_data = student_data[student_data['city'] == city]
    plt.scatter(city_data['study_hours'], city_data['exam_score'], 
                label=city, color=colors[i], s=60)

plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Performance by City')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

### 🎯 9. Subplots - Multiple Charts in One Figure

Essential for creating dashboards and comparing multiple datasets.

#### Sample Sales Data for Multiple Stores:
```python
# Sales data for different Saudi cities
sales_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'riyadh': [120, 135, 145, 160, 175, 180],
    'jeddah': [100, 110, 125, 140, 155, 165],
    'dammam': [80, 90, 95, 105, 115, 125],
    'mecca': [90, 100, 110, 120, 130, 140]
})
```

#### 2x2 Subplot Layout:
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Riyadh
axes[0, 0].plot(sales_data['month'], sales_data['riyadh'], 'o-', color='blue')
axes[0, 0].set_title('Riyadh Sales')
axes[0, 0].grid(True)

# Top-right: Jeddah
axes[0, 1].plot(sales_data['month'], sales_data['jeddah'], 's-', color='red')
axes[0, 1].set_title('Jeddah Sales')
axes[0, 1].grid(True)

# Bottom-left: Dammam
axes[1, 0].plot(sales_data['month'], sales_data['dammam'], '^-', color='green')
axes[1, 0].set_title('Dammam Sales')
axes[1, 0].grid(True)

# Bottom-right: Mecca
axes[1, 1].plot(sales_data['month'], sales_data['mecca'], 'd-', color='orange')
axes[1, 1].set_title('Mecca Sales')
axes[1, 1].grid(True)

plt.tight_layout()
plt.suptitle('Sales Performance Across Saudi Cities', y=1.02, fontsize=16)
plt.show()
```

#### Subplot with Different Chart Types:
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Bar chart
axes[0, 0].bar(sales_data['month'], sales_data['riyadh'])
axes[0, 0].set_title('Riyadh - Bar Chart')

# Line chart
axes[0, 1].plot(sales_data['month'], sales_data['jeddah'], marker='o')
axes[0, 1].set_title('Jeddah - Line Chart')

# Pie chart (using June data)
june_sales = [sales_data['riyadh'].iloc[-1], sales_data['jeddah'].iloc[-1], 
              sales_data['dammam'].iloc[-1], sales_data['mecca'].iloc[-1]]
axes[1, 0].pie(june_sales, labels=['Riyadh', 'Jeddah', 'Dammam', 'Mecca'], autopct='%1.1f%%')
axes[1, 0].set_title('June Sales Distribution')

# Area chart
axes[1, 1].fill_between(sales_data['month'], sales_data['riyadh'], alpha=0.5)
axes[1, 1].set_title('Riyadh - Area Chart')

plt.tight_layout()
plt.show()
```

#### Subplot with different chart types for all cities:
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

cities = ['riyadh', 'jeddah', 'dammam', 'mecca']
colors = ['skyblue', 'orange', 'lightgreen', 'lightcoral']

# Bar chart - All cities
x = range(len(sales_data['month']))
width = 0.2
for i, city in enumerate(cities):
    axes[0, 0].bar([pos + width*i for pos in x], sales_data[city], 
                   width, label=city.title(), color=colors[i])
axes[0, 0].set_title('All Cities - Bar Chart')
axes[0, 0].set_xticks([pos + width*1.5 for pos in x])
axes[0, 0].set_xticklabels(sales_data['month'])
axes[0, 0].legend()

# Line chart - All cities
for i, city in enumerate(cities):
    axes[0, 1].plot(sales_data['month'], sales_data[city], 
                    marker='o', label=city.title(), color=colors[i])
axes[0, 1].set_title('All Cities - Line Chart')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Pie chart (using latest month data)
latest_sales = [sales_data[city].iloc[-1] for city in cities]
axes[1, 0].pie(latest_sales, labels=[city.title() for city in cities], 
               autopct='%1.1f%%', colors=colors)
axes[1, 0].set_title(f'{sales_data["month"].iloc[-1]} Sales Distribution')

# Stacked area chart
axes[1, 1].stackplot(sales_data['month'], 
                     sales_data['riyadh'], sales_data['jeddah'], 
                     sales_data['dammam'], sales_data['mecca'],
                     labels=['Riyadh', 'Jeddah', 'Dammam', 'Mecca'],
                     colors=colors, alpha=0.7)
axes[1, 1].set_title('All Cities - Stacked Area Chart')
axes[1, 1].legend(loc='upper left')

plt.tight_layout()
plt.show()
```

---

### 📦 10. Box Plots - Statistical Distribution Analysis

Box plots show quartiles, median, and outliers - essential for statistical analysis.

#### Sample Test Scores Data:
```python
# Test scores for different subjects
scores_data = {
    'Math': [78, 85, 90, 76, 88, 92, 85, 79, 86, 91, 77, 89, 83, 87, 94, 82, 88, 90, 85, 86],
    'Science': [82, 79, 85, 88, 84, 86, 90, 83, 87, 89, 81, 85, 88, 86, 91, 84, 87, 89, 85, 88],
    'Arabic': [75, 80, 85, 78, 83, 88, 81, 76, 84, 87, 79, 82, 86, 80, 89, 77, 83, 85, 81, 84],
    'English': [70, 75, 80, 73, 78, 83, 76, 72, 79, 82, 74, 77, 81, 75, 84, 73, 78, 80, 76, 79]
}

# Convert to list format for box plot
score_values = [scores_data['Math'], scores_data['Science'], scores_data['Arabic'], scores_data['English']]
```

#### Basic Box Plot:
```python
plt.boxplot(score_values, tick_labels=['Math', 'Science', 'Arabic', 'English'])
plt.title('Test Score Distribution by Subject')
plt.ylabel('Score')
plt.xlabel('Subject')
plt.grid(True, alpha=0.3)
plt.show()
```

#### Horizontal Box Plot:
```python
plt.boxplot(score_values, tick_labels=['Math', 'Science', 'Arabic', 'English'], vert=False)
plt.title('Test Score Distribution by Subject (Horizontal)')
plt.xlabel('Score')
plt.ylabel('Subject')
plt.grid(True, alpha=0.3)
plt.show()
```

---

### 🔥 11. Heatmaps - Correlation and 2D Data

Heatmaps are perfect for showing correlations and relationships in 2D data.

#### Sample Correlation Data:
```python
import numpy as np
import seaborn as sns

# Create sample correlation matrix
subjects = ['Math', 'Science', 'Arabic', 'English', 'History']
np.random.seed(42)  # For reproducible results

# Generate correlation matrix (values between -1 and 1)
correlation_matrix = np.array([
    [1.00, 0.85, 0.45, 0.65, 0.30],
    [0.85, 1.00, 0.40, 0.70, 0.35],
    [0.45, 0.40, 1.00, 0.60, 0.75],
    [0.65, 0.70, 0.60, 1.00, 0.55],
    [0.30, 0.35, 0.75, 0.55, 1.00]
])

correlation_df = pd.DataFrame(correlation_matrix, 
                            index=subjects, 
                            columns=subjects)
```

#### Basic Heatmap:
```python
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_df, annot=True, cmap='coolwarm', center=0,
            square=True, cbar_kws={'label': 'Correlation'})
plt.title('Subject Performance Correlation Matrix')
plt.show()
```

#### Store Sales Heatmap by Month and City:
```python
# Sample monthly sales data
monthly_sales = pd.DataFrame({
    'Riyadh': [120, 135, 145, 160, 175, 180, 190, 185, 170, 155, 140, 130],
    'Jeddah': [100, 110, 125, 140, 155, 165, 170, 160, 145, 130, 115, 105],
    'Dammam': [80, 90, 95, 105, 115, 125, 130, 125, 110, 95, 85, 80],
    'Mecca': [90, 100, 110, 120, 130, 140, 145, 140, 125, 110, 100, 95]
}, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.figure(figsize=(10, 8))
sns.heatmap(monthly_sales, annot=True, cmap='YlOrRd', fmt='d')
plt.title('Monthly Sales by City (in thousands SAR)')
plt.ylabel('Month')
plt.xlabel('City')
plt.show()
```

---

### 🐼 12. Pandas Built-in Plotting - Quick and Easy

Pandas has built-in plotting that's much more convenient than raw matplotlib.

#### Sample Restaurant Revenue Data:
```python
# Revenue data for Saudi restaurant chain
restaurant_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'riyadh_branch': [45000, 52000, 58000, 61000, 67000, 70000],
    'jeddah_branch': [38000, 44000, 48000, 52000, 56000, 59000],
    'dammam_branch': [25000, 28000, 32000, 35000, 38000, 42000]
}).set_index('month')
```

#### Quick Plots with Pandas:
```python
# Line plot
restaurant_data.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Restaurant Revenue by Branch')
plt.ylabel('Revenue (SAR)')
plt.grid(True)
plt.show()

# Bar plot
restaurant_data.plot(kind='bar', figsize=(10, 6))
plt.title('Monthly Restaurant Revenue')
plt.ylabel('Revenue (SAR)')
plt.xticks(rotation=45)
plt.show()

# Area plot
restaurant_data.plot(kind='area', figsize=(10, 6), alpha=0.7)
plt.title('Cumulative Restaurant Revenue')
plt.ylabel('Revenue (SAR)')
plt.show()
```

#### Individual Column Plots:
```python
# Histogram of Riyadh branch revenue
restaurant_data['riyadh_branch'].plot(kind='hist', bins=5, alpha=0.7)
plt.title('Riyadh Branch Revenue Distribution')
plt.xlabel('Revenue (SAR)')
plt.show()

# Box plot comparison
restaurant_data.plot(kind='box')
plt.title('Revenue Distribution by Branch')
plt.ylabel('Revenue (SAR)')
plt.show()
```

---

### 🎨 13. Professional Styling with Seaborn

Seaborn makes statistical plots easier and more beautiful.

#### Sample Employee Salary Data:
```python
# Saudi company employee data
employee_data = pd.DataFrame({
    'name': ['Mohammed', 'Fatima', 'Abdullah', 'Aisha', 'Khalid', 'Sara', 'Omar', 'Maryam', 
             'Ahmed', 'Noura', 'Fahd', 'Layla', 'Salman', 'Huda', 'Yusuf'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 
                   'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'experience_years': [2, 5, 3, 7, 1, 4, 6, 8, 3, 5, 4, 6, 9, 2, 7],
    'salary': [8000, 12000, 9500, 15000, 7000, 11000, 14000, 18000, 
               10000, 13000, 11500, 13500, 19000, 8500, 16000],
    'city': ['Riyadh', 'Jeddah', 'Riyadh', 'Riyadh', 'Dammam', 'Jeddah', 
             'Riyadh', 'Jeddah', 'Dammam', 'Riyadh', 'Jeddah', 'Dammam', 
             'Riyadh', 'Jeddah', 'Dammam']
})
```

#### Seaborn Scatter Plot:
```python
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Scatter plot with department colors
sns.scatterplot(data=employee_data, x='experience_years', y='salary', 
                hue='department', size='salary', sizes=(50, 200))
plt.title('Employee Salary vs Experience by Department')
plt.xlabel('Years of Experience')
plt.ylabel('Salary (SAR)')
plt.show()
```

#### Seaborn Box Plot by Category:
```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=employee_data, x='department', y='salary')
plt.title('Salary Distribution by Department')
plt.ylabel('Salary (SAR)')
plt.show()
```

#### Seaborn Violin Plot:
```python
plt.figure(figsize=(10, 6))
sns.violinplot(data=employee_data, x='department', y='salary')
plt.title('Salary Distribution Shape by Department')
plt.ylabel('Salary (SAR)')
plt.show()
```

---

### ✨ 14. Advanced Customization & Annotations

Adding professional touches to your visualizations.

#### Sample Sales Performance Data:
```python
quarterly_data = pd.DataFrame({
    'quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'sales': [250000, 320000, 290000, 380000],
    'target': [300000, 300000, 300000, 300000]
})
```

#### Chart with Annotations:
```python
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
bars = ax.bar(quarterly_data['quarter'], quarterly_data['sales'], 
              color=['red' if x < 300000 else 'green' for x in quarterly_data['sales']])

# Add target line
ax.axhline(y=300000, color='orange', linestyle='--', linewidth=2, label='Target')

# Annotate each bar
for i, (quarter, sales) in enumerate(zip(quarterly_data['quarter'], quarterly_data['sales'])):
    ax.annotate(f'{sales:,} SAR', 
                xy=(i, sales), 
                xytext=(0, 10),  # 10 points vertical offset
                textcoords='offset points',
                ha='center', va='bottom',
                fontweight='bold')

# Highlight best quarter
best_quarter_idx = quarterly_data['sales'].idxmax()
ax.annotate('Best Performance!', 
            xy=(best_quarter_idx, quarterly_data['sales'].max()),
            xytext=(best_quarter_idx, quarterly_data['sales'].max() + 30000),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2),
            fontsize=12, color='blue', ha='center')

ax.set_title('Quarterly Sales Performance vs Target', fontsize=16, fontweight='bold')
ax.set_ylabel('Sales (SAR)', fontsize=12)
ax.set_xlabel('Quarter', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

#### Multiple Y-axes Chart:
```python
fig, ax1 = plt.subplots(figsize=(10, 6))

# Sales on left axis
color1 = 'tab:blue'
ax1.set_xlabel('Quarter')
ax1.set_ylabel('Sales (SAR)', color=color1)
ax1.plot(quarterly_data['quarter'], quarterly_data['sales'], 
         color=color1, marker='o', linewidth=3, markersize=8)
ax1.tick_params(axis='y', labelcolor=color1)

# Profit margin on right axis
ax2 = ax1.twinx()
profit_margins = [18, 22, 20, 25]  # Percentage
color2 = 'tab:red'
ax2.set_ylabel('Profit Margin (%)', color=color2)
ax2.plot(quarterly_data['quarter'], profit_margins, 
         color=color2, marker='s', linewidth=3, markersize=8)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Sales and Profit Margin Trends', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

### 📅 15. Time Series Visualization

Working with date/time data effectively.

#### Sample Daily Sales Data:
```python
# Generate sample daily sales data
from datetime import datetime, timedelta
import numpy as np

np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(90)]
# Simulate seasonal pattern with random variation
base_sales = 1000 + 200 * np.sin(np.arange(90) * 2 * np.pi / 30) + np.random.normal(0, 100, 90)

time_series_data = pd.DataFrame({
    'date': dates,
    'sales': base_sales
})
```

#### Time Series Plot:
```python
plt.figure(figsize=(12, 6))
plt.plot(time_series_data['date'], time_series_data['sales'], linewidth=2)
plt.title('Daily Sales Over 3 Months')
plt.xlabel('Date')
plt.ylabel('Sales (SAR)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

#### Moving Average:
```python
# Calculate 7-day moving average
time_series_data['moving_avg'] = time_series_data['sales'].rolling(window=7).mean()

plt.figure(figsize=(12, 6))
plt.plot(time_series_data['date'], time_series_data['sales'], 
         alpha=0.5, label='Daily Sales', color='lightblue')
plt.plot(time_series_data['date'], time_series_data['moving_avg'], 
         linewidth=3, label='7-Day Moving Average', color='red')
plt.title('Daily Sales with Moving Average Trend')
plt.xlabel('Date')
plt.ylabel('Sales (SAR)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### 🚀 16. Advanced Exercise Projects

**Complete Dashboard Project:**
Create a comprehensive business dashboard using the following data:

```python
# Sample business performance data
business_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'revenue': [120000, 135000, 145000, 160000, 175000, 180000],
    'costs': [80000, 85000, 90000, 95000, 100000, 105000],
    'customers': [450, 520, 580, 630, 720, 800],
    'online_sales_pct': [35, 40, 45, 48, 52, 55]
})

# Calculate profit
business_data['profit'] = business_data['revenue'] - business_data['costs']
business_data['profit_margin'] = (business_data['profit'] / business_data['revenue'] * 100).round(1)
```

**Your Tasks:**
1. Create a 2x3 subplot dashboard showing:
   - Revenue and costs line chart
   - Profit margin bar chart  
   - Customer growth scatter plot
   - Online sales percentage area chart
   - Monthly profit pie chart
   - Correlation heatmap of all metrics

2. Style it professionally with:
   - Consistent colors
   - Proper titles and labels
   - Grid lines
   - Annotations for key insights

3. Export the dashboard as a high-resolution PNG

---

### ✅ Summary

* Visualization enhances understanding and communication
* Matplotlib is great for static charts; Plotly for interactive ones
* Customize titles, labels, and colors for clarity and appeal
* Choose the right chart for the story your data tells
* Save charts to share them in reports or presentations
