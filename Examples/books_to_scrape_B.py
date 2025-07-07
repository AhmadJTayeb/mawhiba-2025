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

    # Wait for the ordered list (ol) element containing books to load
    page.wait_for_selector("ol")

    # Select all book list items using the specific CSS classes
    books = page.locator("ol").locator("li")

    # Iterate through each book element directly
    for book in books.all():
        # Look for the article.product_pod within each li element
        article = book.locator("article.product_pod")

        # Extract the book title from the anchor tag within the article
        title = article.locator("h3 a").get_attribute("title")

        # Extract the book price from the element with the class price_color
        price = article.locator(".price_color").inner_text()

        # Extract the availability status and strip any extra whitespace
        availability = article.locator(".availability").inner_text().strip()

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