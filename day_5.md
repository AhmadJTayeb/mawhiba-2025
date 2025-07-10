## 🤖 Day 5 Notes: Using AI to Assist with Data Projects

### 🎯 Learning Objectives

By the end of this lesson, you will be able to:
* Write effective prompts to get coding help from AI tools
* Use AI to debug Python errors and improve code
* Generate web scraping code with AI assistance
* Create data analysis and visualization scripts using AI
* Apply best practices for AI-assisted programming

---

### 🧠 1. Introduction to AI-Assisted Programming

#### What AI Tools Can Help With:
- **Code Generation**: Write functions, classes, and complete scripts
- **Debugging**: Explain errors and suggest fixes
- **Code Review**: Improve code quality and performance
- **Documentation**: Generate comments and explanations
- **Learning**: Explain programming concepts and syntax

#### Popular AI Tools:
- **ChatGPT** (OpenAI) - General purpose AI assistant
- **Claude** (Anthropic) - Strong at code analysis and explanations
- **GitHub Copilot** - AI pair programmer in your IDE
- **Cursor** - AI-powered code editor

---

### 📝 2. Prompt Engineering for Programming

#### ❌ Bad Prompts vs ✅ Good Prompts

**❌ Bad:** "Help me with Python"
**✅ Good:** "Help me write a Python function that takes a list of dictionaries containing product data and filters out products with price > 100"

**❌ Bad:** "Fix this error"
**✅ Good:** "I'm getting a KeyError: 'price' when running this code: [paste code]. The error occurs on line 15. What's wrong and how do I fix it?"

#### 🎯 Prompt Templates You Can Use:

**For Code Generation:**
```
I need a Python function that:
- Takes [input parameters]
- Does [specific task]
- Returns [expected output]
- Should handle [edge cases]

Example input: [sample data]
Expected output: [sample result]
```

**For Debugging:**
```
I'm getting this error: [exact error message]
Here's my code: [paste code]
I'm trying to: [explain what you want to accomplish]
What's wrong and how do I fix it?
```

**For Code Improvement:**
```
Please review this code and suggest improvements for:
- Performance
- Readability
- Best practices
- Error handling

[paste your code]
```

#### 🔍 Essential Context for AI:

**Always Provide:**
1. **Exact error messages** (copy-paste the full traceback)
2. **Sample data structure** (first few rows of CSV, example JSON)
3. **Expected output** (what you want the result to look like)
4. **Libraries you're using** (pandas, requests, Playwright, etc.)
5. **Your current code** (even if broken)

**Example of Good Context:**
```
I'm trying to analyze sales data using pandas. Here's my CSV structure:
date,product,price,quantity
2024-01-15,iPhone,999.99,2
2024-01-16,Samsung,899.99,1

I want to calculate monthly revenue totals. Here's what I tried:
[paste your broken code]

I'm getting this error: [exact error message]
Expected output: A dataframe with months and total revenue per month.
```

---

### 🕷️ 3. AI-Assisted Web Scraping

**The Key:** Always inspect the HTML structure first, then create informed prompts.

#### Step 1: Analyze the Website Structure

Before asking AI for help, inspect the website:
1. Press F12 → Navigate to Elements tab
2. Right-click on data you want → "Inspect"
3. Look for repeating HTML patterns

Example pattern you might find:
```html
<div class="product-item">
    <h3 class="product-title">iPhone 15 Pro</h3>
    <span class="price">$999.99</span>
    <div class="rating" data-rating="4.5">★★★★☆</div>
    <span class="availability">In Stock</span>
</div>
```

Extract key selectors: `.product-item`, `.product-title`, `.price`, `.rating`, `.availability`

#### Step 2: Create Your Prompt

**Template:**
```
I want to scrape [website URL] to extract [list data you need].

Here's the HTML structure I found:
[paste the HTML code from developer tools]

The data I need is located in:
- [Data field 1]: CSS selector
- [Data field 2]: CSS selector

Please write a [Playwright/BeautifulSoup] script that:
1. Loads the page and waits for content
2. Extracts data using selectors above
3. Handles missing elements gracefully
4. Exports to CSV with error handling

Expected output: CSV with columns [list your columns]
```

#### Complete Example: Books Site

**What we found by inspecting books.toscrape.com:**
```html
<article class="product_pod">
    <h3><a href="..." title="A Light in the Attic">A Light in the ...</a></h3>
    <p class="price_color">£51.77</p>
    <p class="star-rating Three"></p>
    <p class="availability">In stock</p>
</article>
```

**Our informed prompt:**
```
I want to scrape book data from books.toscrape.com first page.

I inspected the HTML and found this structure:
<article class="product_pod">
    <h3><a href="..." title="A Light in the Attic">A Light in the ...</a></h3>
    <p class="price_color">£51.77</p>
    <p class="star-rating Three"></p>
    <p class="availability">In stock</p>
</article>

The data I need:
- Title: <h3><a> tag's "title" attribute 
- Price: <p class="price_color"> text content
- Rating: class name after "star-rating" (One=1, Two=2, etc.)
- Availability: <p class="availability"> text content

Please write a Playwright script that handles missing elements and exports to CSV.
```

**AI generates this complete script:**
```python
from playwright.sync_api import sync_playwright
import pandas as pd
import re

def scrape_books():
    """Scrape book data from books.toscrape.com"""
    books_data = []
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("http://books.toscrape.com/")
            
            # Wait for content to load
            page.wait_for_selector('.product_pod')
            
            # Get all book containers
            books = page.query_selector_all('.product_pod')
            
            for book in books:
                try:
                    # Extract title
                    title_element = book.query_selector('h3 a')
                    title = title_element.get_attribute('title') if title_element else 'N/A'
                    
                    # Extract price
                    price_element = book.query_selector('.price_color')
                    price_text = price_element.text_content() if price_element else '£0.00'
                    price = float(re.sub(r'[£,]', '', price_text))
                    
                    # Extract rating
                    rating_element = book.query_selector('.star-rating')
                    rating_class = rating_element.get_attribute('class') if rating_element else ''
                    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
                    rating = 0
                    for word, num in rating_map.items():
                        if word in rating_class:
                            rating = num
                            break
                    
                    # Extract availability
                    availability_element = book.query_selector('.availability')
                    availability = availability_element.text_content().strip() if availability_element else 'Unknown'
                    
                    books_data.append({
                        'title': title,
                        'price': price,
                        'rating': rating,
                        'availability': availability
                    })
                    
                except Exception as e:
                    print(f"Error processing book: {e}")
                    continue
            
            browser.close()
            
        except Exception as e:
            print(f"Error during scraping: {e}")
            return []
    
    return books_data

# Run the scraper and save to CSV
if __name__ == "__main__":
    print("Starting book scraper...")
    books = scrape_books()
    
    if books:
        df = pd.DataFrame(books)
        df.to_csv('scraped_books.csv', index=False)
        print(f"Successfully scraped {len(books)} books!")
        print("\nFirst 5 books:")
        print(df.head())
    else:
        print("No books scraped.")
```

**Step 4: Test and Iterate (Following Our Guide)**

After running the script, we might encounter issues. Let's follow our iterative improvement process:

**Issues we found after testing:**
1. Some books might not have ratings
2. Price extraction could be more robust
3. Need progress indicators for larger scraping jobs
4. Could add retry logic for failed requests

**Step 5: Iterative Improvement Prompt**
```
The script works but I found these issues during testing:
1. Some books don't have ratings - the script crashes with AttributeError
2. Price extraction fails when there are special offers or discounts
3. Need progress indicators when scraping multiple pages
4. Website sometimes blocks requests - need retry logic

Here's the error I'm getting:
AttributeError: 'NoneType' object has no attribute 'get_attribute'

Please modify the code to:
- Handle missing rating elements gracefully
- Add more robust price extraction
- Include progress indicators
- Add retry logic with exponential backoff
```

**This demonstrates the complete process:** Inspect → Prompt → Code → Test → Improve

**Common challenges & solutions:**
- **Dynamic Content:** "The content loads dynamically. Add wait conditions for when elements appear."
- **Anti-Bot Protection:** "Add random delays, user agents, and mouse movements to avoid detection."
- **Complex Selectors:** "Here's a larger HTML snippet showing the full page structure: [paste more HTML]"

---

### 📊 4. AI-Assisted Data Analysis & Visualization

**The Key:** Always explore your data first, then create specific prompts with context.

#### Step 1: Understand Your Data First

Before asking AI for analysis, examine your data:
```python
import pandas as pd
df = pd.read_csv('your_data.csv')
print(df.info())
print(df.head())
print(df.describe())
```

Identify issues: Missing values? Wrong data types? Inconsistent formats? Outliers?

Document what you found:
```
Example issues in my sales data:
- Date column has mixed formats: "2024-01-15" and "15/02/2024"
- Price column has some negative values (errors)
- Customer_id has missing values
- Product names have extra whitespace
```

#### Step 2: Create Informed Analysis Prompts

**Template:**
```
I have a dataset with [X] rows and [Y] columns containing [describe the data].

Data structure:
[paste df.info() output or describe columns]

Issues I identified:
- [Issue 1]
- [Issue 2]
- [Issue 3]

Please help me:
1. Clean these specific issues
2. Create [specific analysis you want]
3. Generate [specific visualizations]
4. Provide insights about [specific business questions]

Here's a sample of the data:
[paste df.head() output]
```

#### Complete Example: Cleaning Messy Sales Data

We have messy sales data (`Examples/messy_sales_data.csv`) with these issues:
- Inconsistent date formats, missing values, negative prices, extra whitespace

**Our prompt to AI:**
```
I have a messy sales CSV file with these problems:
- Dates in different formats: "2024-01-15", "15/02/2024", "04-04-2024"
- Missing values in price and customer_id columns
- Some negative prices (should be positive)
- Extra whitespace around product names

Please write a complete pandas script to:
1. Load the data from 'Examples/messy_sales_data.csv'
2. Clean all these issues
3. Show before/after statistics
4. Save the cleaned data and create a summary report
```

**AI generates this complete script:**
```python
import pandas as pd
import numpy as np
from datetime import datetime
import re

def clean_sales_data():
    """Clean messy sales data and generate report"""
    
    # Load the messy data
    print("Loading messy sales data...")
    df = pd.read_csv('Examples/messy_sales_data.csv')
    
    print("=== BEFORE CLEANING ===")
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values per column:")
    print(df.isnull().sum())
    print(f"\nFirst 5 rows:")
    print(df.head())
    print(f"\nData types:")
    print(df.dtypes)
    
    # Make a copy for cleaning
    df_clean = df.copy()
    
    # 1. Clean product names (remove extra whitespace)
    df_clean['product_name'] = df_clean['product_name'].str.strip()
    
    # 2. Fix date formats
    def standardize_date(date_str):
        """Convert various date formats to standard format"""
        if pd.isna(date_str):
            return date_str
        
        try:
            # Try different formats
            formats = ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d']
            for fmt in formats:
                try:
                    return pd.to_datetime(date_str, format=fmt)
                except:
                    continue
            # If none work, try pandas auto-detection
            return pd.to_datetime(date_str)
        except:
            return pd.NaT
    
    df_clean['date'] = df_clean['date'].apply(standardize_date)
    
    # 3. Fix price issues
    # Convert to numeric, handling empty strings
    df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')
    
    # Fix negative prices (make them positive)
    df_clean.loc[df_clean['price'] < 0, 'price'] = abs(df_clean.loc[df_clean['price'] < 0, 'price'])
    
    # Fill missing prices with median of same category
    median_prices = df_clean.groupby('category')['price'].median()
    for category in df_clean['category'].unique():
        mask = (df_clean['category'] == category) & (df_clean['price'].isna())
        if mask.any():
            df_clean.loc[mask, 'price'] = median_prices[category]
    
    # 4. Handle missing customer IDs
    # Generate placeholder IDs for missing values
    missing_customer_mask = df_clean['customer_id'].isna() | (df_clean['customer_id'] == '')
    next_id_num = 1000
    for idx in df_clean[missing_customer_mask].index:
        df_clean.loc[idx, 'customer_id'] = f'CUST{next_id_num:03d}'
        next_id_num += 1
    
    # 5. Calculate revenue
    df_clean['revenue'] = df_clean['price'] * df_clean['quantity']
    
    print("\n=== AFTER CLEANING ===")
    print(f"Dataset shape: {df_clean.shape}")
    print(f"Missing values per column:")
    print(df_clean.isnull().sum())
    print(f"\nFirst 5 rows:")
    print(df_clean.head())
    
    # Save cleaned data
    df_clean.to_csv('cleaned_sales_data.csv', index=False)
    print("\n✅ Cleaned data saved to 'cleaned_sales_data.csv'")
    
    # Generate summary report
    print("\n=== CLEANING SUMMARY REPORT ===")
    print(f"🔧 Fixed {len(df[df['product_name'].str.contains(r'^\s+|\s+$', na=False)])} product names with extra whitespace")
    print(f"📅 Standardized {len(df)} date formats")
    print(f"💰 Fixed {len(df[df['price'] < 0])} negative prices")
    print(f"💸 Filled {df['price'].isna().sum()} missing prices using category medians")
    print(f"👤 Generated IDs for {missing_customer_mask.sum()} missing customers")
    
    print(f"\n📊 FINAL STATISTICS:")
    print(f"Total revenue: ${df_clean['revenue'].sum():,.2f}")
    print(f"Average order value: ${df_clean['revenue'].mean():.2f}")
    print(f"Date range: {df_clean['date'].min().date()} to {df_clean['date'].max().date()}")
    print(f"Categories: {', '.join(df_clean['category'].unique())}")
    
    return df_clean

# Run the cleaning process
if __name__ == "__main__":
    cleaned_data = clean_sales_data()
```

#### Complete Example: Creating Visualizations

**Your Prompt to AI:**
```
Using the cleaned sales data, create a comprehensive dashboard with 4 charts:
1. Monthly revenue trends (line chart)
2. Revenue by category (pie chart)
3. Top 10 products by total revenue (horizontal bar chart)
4. Price distribution by category (box plot)

Make them publication-ready with proper titles, colors, and styling.
Use matplotlib/seaborn and save as a single image file.
```

**AI-Generated Visualization Script:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

def create_sales_dashboard():
    """Create a comprehensive sales dashboard"""
    
    # Load cleaned data
    df = pd.read_csv('cleaned_sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Sales Data Dashboard - 2024', fontsize=20, fontweight='bold')
    
    # Color palette
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
    
    # 1. Monthly Revenue Trends (Line Chart)
    monthly_revenue = df.groupby('month')['revenue'].sum()
    axes[0,0].plot(range(len(monthly_revenue)), monthly_revenue.values, 
                   marker='o', linewidth=3, markersize=8, color='#FF6B6B')
    axes[0,0].set_title('Monthly Revenue Trends', fontsize=14, fontweight='bold')
    axes[0,0].set_xlabel('Month')
    axes[0,0].set_ylabel('Revenue ($)')
    axes[0,0].grid(True, alpha=0.3)
    axes[0,0].tick_params(axis='x', rotation=45)
    
    # Format y-axis as currency
    axes[0,0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # 2. Revenue by Category (Pie Chart)
    category_revenue = df.groupby('category')['revenue'].sum()
    wedges, texts, autotexts = axes[0,1].pie(category_revenue.values, 
                                            labels=category_revenue.index,
                                            autopct='%1.1f%%',
                                            colors=colors[:len(category_revenue)],
                                            startangle=90)
    axes[0,1].set_title('Revenue by Category', fontsize=14, fontweight='bold')
    
    # 3. Top 10 Products by Revenue (Horizontal Bar Chart)
    product_revenue = df.groupby('product_name')['revenue'].sum().sort_values(ascending=True).tail(10)
    bars = axes[1,0].barh(range(len(product_revenue)), product_revenue.values, 
                         color='#4ECDC4', alpha=0.8)
    axes[1,0].set_yticks(range(len(product_revenue)))
    axes[1,0].set_yticklabels([name[:20] + '...' if len(name) > 20 else name 
                              for name in product_revenue.index])
    axes[1,0].set_title('Top 10 Products by Revenue', fontsize=14, fontweight='bold')
    axes[1,0].set_xlabel('Revenue ($)')
    axes[1,0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Add value labels on bars
    for bar in bars:
        width = bar.get_width()
        axes[1,0].text(width, bar.get_y() + bar.get_height()/2, 
                      f'${width:,.0f}', ha='left', va='center', fontweight='bold')
    
    # 4. Price Distribution by Category (Box Plot)
    categories = df['category'].unique()
    price_data = [df[df['category'] == cat]['price'].values for cat in categories]
    
    box_plot = axes[1,1].boxplot(price_data, labels=categories, patch_artist=True)
    axes[1,1].set_title('Price Distribution by Category', fontsize=14, fontweight='bold')
    axes[1,1].set_xlabel('Category')
    axes[1,1].set_ylabel('Price ($)')
    axes[1,1].tick_params(axis='x', rotation=45)
    
    # Color the box plots
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('sales_dashboard.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print summary insights
    print("📊 DASHBOARD INSIGHTS:")
    print(f"💰 Total Revenue: ${df['revenue'].sum():,.2f}")
    print(f"📈 Best Month: {monthly_revenue.idxmax()} (${monthly_revenue.max():,.2f})")
    print(f"🏆 Top Category: {category_revenue.idxmax()} (${category_revenue.max():,.2f})")
    print(f"⭐ Best Product: {product_revenue.idxmax()} (${product_revenue.max():,.2f})")

# Run the dashboard creation
if __name__ == "__main__":
    create_sales_dashboard()
```

---

### 🛠️ 5. Hands-On Exercises with Real Data

#### Exercise 1: Product Analysis Challenge
**Data:** `Examples/sample_products.csv`

**Prompt to try:**
```
I have a product dataset (Examples/sample_products.csv) with columns:
product_id, name, category, price, rating, availability, description

Help me write Python code to:
1. Load and explore the data (shape, info, head)
2. Find the top 3 most expensive products in each category
3. Calculate average price and rating by category
4. Create a scatter plot showing price vs rating, colored by category
5. Identify any products that are out of stock
```

#### Exercise 2: News Data Analysis
**Data:** `Examples/sample_news_data.csv`

**Prompt to try:**
```
Analyze this news dataset (Examples/sample_news_data.csv) and create:
1. Summary statistics of sentiment scores by category
2. Top 5 articles by views with their details
3. Author ranking by total article views
4. A timeline chart showing article count per day
5. Average sentiment score by category (bar chart)
Include insights and explanations for each analysis.
```

#### Exercise 3: Complete Data Pipeline
**Data:** `Examples/messy_sales_data.csv`

**Advanced prompt to try:**
```
Using the cleaned sales data, help me perform advanced analytics:
1. Customer segmentation: Group customers by total spending and frequency
2. Seasonal analysis: Compare sales performance across months
3. Product performance: Calculate metrics like profit margin, turnover rate
4. Regional insights: Compare performance across North, South, East, West
5. Create an executive summary with key findings and recommendations
```

---

### 🎯 6. Mini Project: Your AI-Powered Analysis

**Goal:** Complete a full data analysis project in 45 minutes using AI assistance

#### Quick Project Steps:

1. **Choose Your Data (5 min):** Pick one dataset:
   - `Examples/sample_products.csv` - E-commerce analysis
   - `Examples/sample_news_data.csv` - Media analysis
   - `Examples/messy_sales_data.csv` - Sales analysis

2. **Data Exploration (10 min):** Ask AI to generate an exploration script:
   ```
   Create a comprehensive data exploration script for [your chosen dataset].
   Include: data shape, missing values, data types, basic statistics, 
   and initial insights. Add comments explaining each step.
   ```

3. **Analysis Questions (15 min):** Ask AI to help answer 3 business questions:
   ```
   Based on this dataset, help me answer these business questions:
   1. [Your question 1]
   2. [Your question 2]  
   3. [Your question 3]
   Provide code, visualizations, and clear explanations.
   ```

4. **Create Dashboard (10 min):**
   ```
   Create a 3-chart dashboard summarizing the key findings from my analysis.
   Make it professional with proper titles, colors, and layout.
   ```

5. **Executive Summary (5 min):**
   ```
   Write an executive summary of my analysis including:
   - Key findings
   - Business recommendations
   - Data quality notes
   - Next steps for further analysis
   ```

**Example projects:** Product Portfolio Analysis, Content Performance Study, Sales Performance Review

---

### ⚠️ 7. Best Practices & Common Pitfalls

#### ✅ Do's:
- **Be Specific**: Include exact error messages, sample data, expected output
- **Iterate**: Ask for improvements after getting initial code
- **Test Code**: Always run and test AI-generated code
- **Ask for Explanations**: Request comments explaining how code works
- **Provide Context**: Share relevant parts of your existing codebase

#### ❌ Don'ts:
- **Don't Trust Blindly**: Always review and understand AI-generated code
- **Don't Skip Testing**: AI code may have bugs or not handle edge cases
- **Don't Copy-Paste Everything**: Understand what each line does
- **Don't Ignore Ethics**: Respect website terms of service and robots.txt
- **Don't Forget Error Handling**: Always ask AI to add proper error handling

#### 🔧 Debugging Tips:
```
When AI code doesn't work:
1. Copy the exact error message
2. Share the problematic code section
3. Explain what you expected vs. what happened
4. Ask for a step-by-step fix
```

#### 💡 Pro Tips for Better Results:
- **Share Your Data Structure**: Show AI the first few rows of your CSV
- **Request Multiple Approaches**: "Show me 3 different ways to solve this"
- **Ask for Alternatives**: "What are other visualization options for this data?"
- **Get Explanations**: "Explain why you chose this approach"

---

### 📚 8. Additional Resources

#### Ready-to-Use Prompts:
```
# Data Loading & Exploration
"Load this CSV file and give me a complete data exploration report with visualizations"

# Error Fixing
"I'm getting [error]. Here's my code: [paste code]. Fix it and explain what was wrong."

# Code Improvement
"Review this code and make it more efficient, readable, and robust: [paste code]"

# Visualization
"Create a beautiful [chart type] showing [relationship] with proper styling and annotations"

# Documentation
"Add comprehensive comments and docstrings to this code: [paste code]"
```

#### AI Tools for Programmers:
- **Free**: ChatGPT, Claude, Google Bard
- **Paid**: GitHub Copilot, Cursor Pro, Replit AI
- **Specialized**: Jupyter AI, Google Colab AI

---

### ✅ Summary & Next Steps

**What You Learned Today:**
- How to write effective prompts for programming help
- Using AI for web scraping, data analysis, and visualization
- Best practices for AI-assisted coding
- Common pitfalls and how to avoid them

**Practical Skills Gained:**
- Complete web scraper with error handling
- Data cleaning pipeline for messy data
- Professional dashboard creation
- Debugging workflow with AI

**Action Items:**
1. Try the hands-on exercises with the provided datasets
2. Complete the 45-minute mini project
3. Practice writing better prompts for your coding questions
4. Start incorporating AI into your daily programming workflow
---

### 🎯 Want to Practice More?

Download these files and start coding:
- `Examples/sample_products.csv` - Clean product data
- `Examples/messy_sales_data.csv` - Data that needs cleaning
- `Examples/sample_news_data.csv` - News articles for analysis

**Try asking AI to help you with:**
- Combining multiple datasets
- Creating interactive plots with Plotly
- Building a simple web dashboard with Streamlit
- Automating report generation

Remember: The best way to learn AI-assisted programming is by doing. Start with simple prompts and gradually ask for more complex solutions!
