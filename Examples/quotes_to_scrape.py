from playwright.sync_api import sync_playwright
import pandas as pd

# List to store scraped quotes
results = []

# Use Playwright to automate browser actions
with sync_playwright() as p:
    # Launch a Chromium browser instance in non-headless mode with a delay for each action
    browser = p.chromium.launch(headless=False, slow_mo=1000)

    # Create a new browser page
    page = browser.new_page()

    # Navigate to the Quotes to Scrape website
    page.goto("http://quotes.toscrape.com/")  # Demo site for quotes scraping

    # Wait for quote elements to load on the page
    page.wait_for_selector(".quote")

    # Locate all quote elements on the page
    quotes = page.locator(".quote")
    count = quotes.count()  # Get the total number of quotes
    print(count)  # Print the count of quotes for debugging purposes

    # Loop through each quote element and extract data
    for i in range(count):
        q = quotes.nth(i)  # Select the nth quote element
        text = q.locator(".text").inner_text()  # Extract the quote text
        author = q.locator(".author").inner_text()  # Extract the author's name
        results.append({"quote": text, "author": author})  # Append the extracted data to the results list

    # Close the browser instance
    browser.close()

# Convert the scraped data into a Pandas DataFrame
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv("quotes.csv", index=False)

# Print a confirmation message and display the first few rows of the DataFrame
print("Scraped quotes saved to quotes.csv")
print(df.head())