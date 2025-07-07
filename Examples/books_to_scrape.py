from playwright.sync_api import sync_playwright
import pandas as pd

# List to store scraped data
results = []

# Use Playwright to automate browser actions
with sync_playwright() as p:
    # Launch a Chromium browser instance in non-headless mode
    browser = p.chromium.launch(headless=False)

    # Create a new browser page
    page = browser.new_page()

    # Navigate to the Books to Scrape website
    page.goto("https://books.toscrape.com/")  # Real demo site for scraping practice

    # Wait for book elements to load on the page
    page.wait_for_selector("article.product_pod")

    # Locate all book elements on the page
    books = page.locator("article.product_pod")
    count = books.count()  # Get the total number of books

    # Loop through each book element and extract data
    for i in range(count):
        book = books.nth(i)  # Select the nth book element
        title = book.locator("h3 a").get_attribute("title")  # Extract the book title
        price = book.locator(".price_color").inner_text()  # Extract the book price
        availability = book.locator(".availability").inner_text().strip()  # Extract availability status

        # Append the extracted data to the results list
        results.append({"title": title, "price": price, "availability": availability})

    # Close the browser instance
    browser.close()

# Convert the scraped data into a Pandas DataFrame
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv("books.csv", index=False)

# Print a confirmation message and display the first few rows of the DataFrame
print("Scraped data saved to books.csv")
print(df.head())