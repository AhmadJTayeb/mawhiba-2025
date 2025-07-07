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
* **How to check**: Just add `/robots.txt` to the site’s URL (e.g., `https://books.toscrape.com/robots.txt`) and read the rules.
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

### 🔍 3. Using Developer Tools

1. Right-click on a webpage and select **Inspect**
2. Use the element picker tool to select parts of the page
3. Note the tag, class, or id of the element you want to extract

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

There are several ways to find elements in a webpage using Playwright:

* `page.query_selector(".class")` – Selects the first element with that class
* `page.query_selector("#id")` – Selects element by ID
* `page.query_selector("tag")` – Selects the first element with that tag name (e.g., `div`, `h2`)
* `page.query_selector("div > span")` – Selects nested/child elements
* `page.query_selector("[attribute='value']")` – Selects using attributes like `data-id`, `name`, etc.
* `page.locator("selector")` – Recommended for modern usage (supports advanced actions like chaining, waiting, and bulk selection)

#### 🧠 Why Use `page.locator()`?

`locator()` is Playwright's preferred method because it allows more robust interaction with elements, supports retries, and can perform advanced queries and actions.

**Basic Example:**

```python
product_name = page.locator(".product-name").first
print(product_name.inner_text())
```

**Clicking a Button by Text:**

```python
page.locator("text=Buy Now").click()
```

**Looping Through Multiple Elements:**

```python
items = page.locator(".product")
count = items.count()

for i in range(count):
    name = items.nth(i).locator(".product-name").inner_text()
    price = items.nth(i).locator(".price").inner_text()
    print(name, price)
```

`locator()` is especially powerful when dealing with dynamic or JavaScript-rendered pages.

**Example:**

```python
products = page.query_selector_all(".product")

for product in products:
    name = product.query_selector(".product-name").inner_text()
    price = product.query_selector(".price").inner_text()
    print(name, price)
```

---

### 🛡️ 7. Handling Errors with Try-Except

When working with web scraping or APIs, things can go wrong—pages might not load, selectors might not match, or data might be missing. To prevent your whole program from crashing, use a `try-except` block to catch errors and continue running your code.

#### 🔍 Why Use Try-Except?

It allows your program to respond to errors gracefully instead of stopping completely.

#### 🧪 Example:

```python
try:
    name = product.query_selector(".product-name").inner_text()
    price = product.query_selector(".price").inner_text()
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

* **Elements not found?** Wait for page to load: `page.wait_for_selector()`
* **Text extraction issues?** Try `.inner_text()` or `.get_attribute()`
* **Pages loading slowly?** Use time delays (e.g., `time.sleep(2)`) for demos

---

### 🚀 10 Full Example: Scraping Quotes from Quotes to Scrape

```python
from playwright.sync_api import sync_playwright
import pandas as pd

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

1. Use Playwright to open a webpage and print its title
2. Scrape product names and prices from a mock HTML page
3. Save the scraped data to a CSV file using `pandas`
4. Calculate and display the average price of all products

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
