## 🌐 Day 2 Notes: Web Scraping with Playwright

### 🎯 Objectives

By the end of this lesson, you should be able to:

* Understand the structure of web pages (HTML, CSS selectors)
* Use browser developer tools to inspect page content
* Set up and use Playwright in Python
* Extract data like product names and prices
* Save scraped data into a CSV file using `pandas`

---

### 🕸️ 1. What is Web Scraping?

Web scraping is the process of automatically extracting data from websites. It's useful when:

* You want to gather prices or products from e-commerce sites
* Collect data for research or analysis
* Monitor public information

**⚠️ Ethics Reminder:** Always check a website's terms of service. Don’t overload servers or scrape restricted areas.

---

### ⚖️ 1.1 Ethics in Web Scraping

Web scraping is a powerful tool, but it comes with serious **ethical** and **legal** responsibilities. Before scraping any site, consider the following:

#### 🗂️ **robots.txt: The Website’s Scraping “Rulebook”**

* Websites often have a `robots.txt` file (e.g., `https://example.com/robots.txt`) that specifies which parts of the site can or cannot be accessed by automated bots—including scrapers.
* **Respecting `robots.txt`**: Always check this file before scraping. If it disallows certain paths, do not scrape those sections.
* **How to check**: Just add `/robots.txt` to the site’s URL (e.g., `https://google.com/robots.txt`) and read the rules.
* **Example of a `robots.txt` rule:**

  ```
  User-agent: *
  Disallow: /private/
  Allow: /public/
  ```

  * This means bots should avoid `/private/` but are allowed in `/public/`.
* **Note:** `robots.txt` is not legally binding everywhere, but ignoring it can get your IP blocked, damage your reputation, or even lead to legal action.

#### 📜 **Check Terms of Service**

* Many websites explicitly forbid or limit scraping in their Terms of Service. Violating these terms can result in legal issues or bans.
* Always **read and follow** the terms before you scrape.

#### 🧑‍💻 **Be a Good Web Citizen**

* **Don’t overload servers:** Use polite scraping techniques:

  * Limit your request rate (e.g., use `time.sleep()` between requests).
  * Don’t make too many simultaneous connections.
  * Identify your scraper with a user-agent string.
* **Don’t scrape private or sensitive data:** Only collect public information.
* **Give credit and respect copyright:** Don’t republish scraped content as your own.
* **Contact the site owner:** If in doubt, ask for permission!

---
### 🛠️ 1.2 Other Ways to Collect Data

Web scraping isn't the only way to collect online data. In fact, many websites and services offer APIs that allow you to access data more easily and ethically.

#### 📁 What's an API?

An **API** (Application Programming Interface) is a structured way for programs to request and exchange data.

**Benefits of APIs:**

* More stable and reliable than scraping
* Often faster and easier to parse (usually JSON format)
* Approved by the service provider

#### 🔹 Example: OpenWeatherMap API (requires API key)

```python
import requests

API_KEY = "your_api_key"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Riyadh&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
print(data["main"]["temp"])
```

#### 🔹 Example: Exchange Rate API (no API key required)

```python
import requests

url = "https://api.exchangerate.host/latest?base=USD"
response = requests.get(url)
data = response.json()
print("EUR exchange rate:", data["rates"]["EUR"])
```

#### 🔹 Example: CNN News via saurav.tech NewsAPI (no API key required)

```python
import requests

url = "https://saurav.tech/NewsAPI/everything/cnn.json"
response = requests.get(url)
data = response.json()

for article in data["articles"]:
    print(article["title"])
    print(article["description"])
    print("---")
```

**Tip:** Always read the API documentation and sign up for an API key if required.

---

### 🧾 1.3 Understanding JSON Format

Many APIs return data in **JSON** (JavaScript Object Notation) format. JSON is a lightweight way to represent structured data, and it's easy to use with Python.

#### 🧠 What Does JSON Look Like?

Here's an example JSON response from a news API:

```json
{
  "status": "ok",
  "totalResults": 2,
  "articles": [
    {
      "title": "Breaking News Headline",
      "description": "A short summary of the article.",
      "url": "https://example.com/news1"
    },
    {
      "title": "Another Story",
      "description": "Another summary here.",
      "url": "https://example.com/news2"
    }
  ]
}
```

#### 🛠️ Working with JSON in Python

You can access data using Python's dictionary syntax:

```python
import requests

response = requests.get("https://saurav.tech/NewsAPI/everything/cnn.json")
data = response.json()

print(data["status"])
print("Total Articles:", data["totalResults"])

for article in data["articles"]:
    print(article["title"])
    print(article["description"])
```

You’ll often work with nested structures, like a list of dictionaries inside the main response. Practice navigating and accessing the values you need.

---

### 🧱 2. Understanding HTML Basics

* HTML is the language websites use to structure content
* **Tags**: `<div>`, `<span>`, `<p>`, `<a>`, etc.
* **Attributes**: `class`, `id`, `href`, `src`

**Example:**

```html
<div class="product">
  <h2 class="product-name">Apple</h2>
  <span class="price">$1.25</span>
</div>
```

You will use these classes (like `product-name` and `price`) to find the data.

---

### 🎨 2.1 What is CSS?

**CSS** (Cascading Style Sheets) is the language that makes websites look beautiful. While HTML structures the content, CSS controls:

* **Colors** and **fonts**
* **Layout** and **spacing** 
* **Styling** of elements

**CSS Selectors** are patterns used to find and style specific elements on a webpage. We use these same selectors in web scraping to target the data we want.

**Example CSS:**
```css
.product-name {
    color: blue;
    font-size: 18px;
}
.price {
    color: green;
    font-weight: bold;
}
```

---

### ⚡ 2.2 What is JavaScript?

**JavaScript** is a programming language that makes websites interactive and dynamic. It can:

* **Load content** after the page loads
* **Update information** without refreshing the page
* **Respond to user actions** (clicks, form submissions)

**Why this matters for scraping:** Some websites use JavaScript to load product data, prices, or other information after the initial page loads. This means the data might not be available immediately when the page first opens.

---

### 🎯 2.3 CSS Selectors for Web Scraping

CSS selectors help you target specific elements on a webpage:

* `.class-name` - Selects elements with a specific class
* `#id-name` - Selects element with a specific ID  
* `tag-name` - Selects all elements of that type
* `parent > child` - Selects direct child elements
* `[attribute="value"]` - Selects by attribute

**Example:** `.product-name` finds all elements with class="product-name"

---

### ⏳ 2.4 Handling JavaScript-Rendered Content

Some websites load content using JavaScript after the page loads. If your selectors don't work:

* Use `page.wait_for_selector(".element")` to wait for content
* Try `page.wait_for_load_state("networkidle")` for dynamic pages
* Add small delays with `time.sleep(2)` for simple cases

---

### 🔍 3. Using Developer Tools

**What are Developer Tools?** Developer Tools are built-in browser features that let you "see behind the scenes" of any website. They show you the HTML structure, CSS styles, and JavaScript code that make up the webpage.

**Why do we need them for scraping?** Before you can scrape data, you need to know:
* What HTML elements contain the data you want
* What CSS classes or IDs those elements have
* How the page is structured

**How to use them:**

1. Right-click on a webpage and select **Inspect**
2. Use the element picker tool (🔍 icon) to select parts of the page
3. Note the tag, class, or id of the element you want to extract
4. Look at the highlighted HTML code to understand the structure

**Pro tip:** The element picker tool is your best friend - it shows you exactly which HTML element corresponds to what you see on the page!

---

### ⚙️ 4. Setting Up Playwright

You can set up Playwright in two main ways:

#### 🖥️ **On Your Local Machine (Laptop/Desktop)**

Install Playwright:

```bash
pip install playwright
playwright install
```

#### ☁️ **On Google Colab (Cloud Notebook)**

Since Colab runs in the cloud, use a `!` before commands:

```python
!pip install playwright
!playwright install
```

* After running these cells, Playwright will be installed and ready to use in Colab.
* Note: For web automation, you may need to use Playwright in headless mode (the default in Colab).

---

### 🧪 5. Using Playwright in Python

Basic usage:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # visible browser
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

---

### 📄 6. Extracting Data from Web Pages

Playwright provides powerful ways to find and extract data from web pages. We'll focus on the modern `page.locator()` method, which is more reliable and easier to use.

#### 🎯 Understanding the Page Structure

First, let's look at a typical product page structure:

```html
<div class="product">
  <h2 class="product-name">iPhone 15</h2>
  <span class="price">$999</span>
  <div class="rating">⭐⭐⭐⭐⭐</div>
</div>
<div class="product">
  <h2 class="product-name">Samsung Galaxy</h2>
  <span class="price">$899</span>
  <div class="rating">⭐⭐⭐⭐</div>
</div>
```

#### 🔍 Using `page.locator()` (Recommended Method)

`page.locator()` is the modern way to find elements. It's more reliable and supports advanced features:

**Basic Selectors:**
* `.class-name` – Selects elements with a specific class
* `#id-name` – Selects element with a specific ID  
* `tag-name` – Selects all elements of that type
* `parent > child` – Selects direct child elements
* `[attribute="value"]` – Selects by attribute

**Examples:**

```python
# Get the first product name
product_name = page.locator(".product-name").first
print(product_name.inner_text())  # Output: iPhone 15

# Get all product names
all_names = page.locator(".product-name")
print(all_names.count())  # Output: 2

# Get specific product by index
second_product = page.locator(".product-name").nth(1)
print(second_product.inner_text())  # Output: Samsung Galaxy
```

**Looping Through Multiple Elements:**

```python
# Get all products
products = page.locator(".product")
count = products.count()

for i in range(count):
    product = products.nth(i)
    name = product.locator(".product-name").inner_text()
    price = product.locator(".price").inner_text()
    rating = product.locator(".rating").inner_text()
    print(f"{name}: {price} - {rating}")
```

**Output:**
```
iPhone 15: $999 - ⭐⭐⭐⭐⭐
Samsung Galaxy: $899 - ⭐⭐⭐⭐
```

---

### 🛡️ 7. Handling Errors with Try-Except

When working with web scraping or APIs, things can go wrong—pages might not load, selectors might not match, or data might be missing. To prevent your whole program from crashing, use a `try-except` block to catch errors and continue running your code.

#### 🔍 Why Use Try-Except?

It allows your program to respond to errors gracefully instead of stopping completely.

#### 🧪 Example:

```python
try:
    name = product.locator(".product-name").inner_text()
    price = product.locator(".price").inner_text()
    print(name, price)
except Exception as e:
    print("Error extracting product info:", e)
```

This approach is especially helpful when looping through many items—some may work, others might not.

---

### 💾 8. Saving Data to a CSV

```python
import pandas as pd

data = [
    {"name": "Apple", "price": 1.25},
    {"name": "Banana", "price": 0.75}
]

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("products.csv", index=False)
print("Data saved to products.csv")
```

---

### 🔧 9. Common Issues and Fixes

**Problem: "Element not found" error**
```python
# Solution: Wait for the element to appear
page.wait_for_selector(".product-name")
product = page.locator(".product-name").first
```

**Problem: Empty text when extracting**
```python
# Solution: Try different extraction methods
text = element.inner_text()  # Gets visible text
text = element.get_attribute("textContent")  # Gets all text including hidden
text = element.text_content()  # Alternative method
```

**Problem: Page loads slowly**
```python
# Solution: Add waiting strategies
page.wait_for_load_state("networkidle")  # Wait for network to be idle
time.sleep(2)  # Simple delay (use sparingly)
```

**Problem: Selector not working**
```python
# Solution: Check the actual HTML structure
# Use Developer Tools to verify the correct class/id names
# Try different selectors: .class, #id, tag-name, etc.
```

**Problem: Browser closes too quickly**
```python
# Solution: Add a pause or keep browser open
time.sleep(5)  # Pause for 5 seconds
# OR
input("Press Enter to close browser...")  # Wait for user input
```

---

### 🚀 10. Full Example: Scraping Quotes from Quotes to Scrape

```python
from playwright.sync_api import sync_playwright
import pandas as pd
import time

# List to store scraped quotes
results = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://quotes.toscrape.com/")  # Demo site for quotes scraping

    # Wait for quote elements to load
    page.wait_for_selector(".quote")

    quotes = page.locator(".quote")
    count = quotes.count()

    for i in range(count):
        q = quotes.nth(i)
        text = q.locator(".text").inner_text()
        author = q.locator(".author").inner_text()
        results.append({"quote": text, "author": author})

    browser.close()

# Convert to DataFrame and save
df = pd.DataFrame(results)
df.to_csv("quotes.csv", index=False)
print("Scraped quotes saved to quotes.csv")
print(df.head())
```

This example demonstrates:

1. Launching a headless browser to visit a live demo site
2. Selecting each `.quote` element and extracting text and author
3. Storing the data in a list and converting it into a Pandas DataFrame
4. Saving the results to `quotes.csv` and previewing the first entries

---

### ✏️ Mini Exercises

**Exercise 1: Basic Page Navigation**
```python
from playwright.sync_api import sync_playwright

# Open https://quotes.toscrape.com/ and print the page title
# Hint: Use page.title()
```

**Exercise 2: Extract Single Element**
```python
# From the same page, extract and print the first quote text
# Hint: Use page.locator(".text").first.inner_text()
```

**Exercise 3: Extract Multiple Elements**
```python
# Extract all quote texts and authors, store them in a list
# Hint: Use a loop with page.locator(".quote")
```

**Exercise 4: Save to CSV**
```python
import pandas as pd

# Convert your extracted data to a DataFrame and save as "quotes.csv"
# Hint: Use pd.DataFrame() and .to_csv()
```

**Exercise 5: Calculate Statistics**
```python
# Calculate and print the total number of quotes on the page
# Hint: Use .count() method
```

---

### 🏠 Homework

1. Use Playwright to scrape product names and prices from a real e-commerce site (e.g., `https://books.toscrape.com/`).  
2. Save the scraped data to a CSV file using `pandas`.
3. Calculate and print the average price of all products.

---

### ✅ Summary

* Web scraping is a method of extracting online data
* HTML structure and browser inspection help find content
* Playwright automates page interaction and data collection
* `pandas` makes it easy to store data in CSV format

Use this power responsibly — and enjoy building your first real data extractor!

---

### 📚 Glossary

- **API (Application Programming Interface):** A way for programs to communicate and exchange data, often in a structured format like JSON.
- **Attribute:** Extra information added to an HTML tag, such as class, id, or href.
- **Class:** An HTML attribute used to group elements for styling or selection (e.g., class="product").
- **CSS (Cascading Style Sheets):** The language used to style and layout web pages.
- **CSS Selector:** A pattern used to select specific HTML elements (e.g., .product-name, #main, div > span).
- **Headless:** Running a browser without a visible window (useful for automation).
- **HTML (HyperText Markup Language):** The standard language for creating web pages and structuring content.
- **ID:** An HTML attribute that uniquely identifies an element on a page (e.g., id="header").
- **JavaScript:** A programming language that makes web pages interactive and dynamic.
- **JSON (JavaScript Object Notation):** A lightweight data format often used for APIs.
- **Locator:** A Playwright method for finding and interacting with elements on a web page.
- **Pandas:** A Python library for data analysis and working with tables (DataFrames).
- **Playwright:** A Python library for automating browsers and scraping web pages.
- **Scraping:** Automatically extracting data from websites.
- **Selector:** A pattern (like a CSS selector) used to find elements in HTML.
- **Tag:** An HTML element, such as `div`, `span`, or `a`.
