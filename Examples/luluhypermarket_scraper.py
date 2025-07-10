"""
Lulu Hypermarket Electronics & Gaming Products Web Scraper

This module provides functionality to scrape product information from the Lulu Hypermarket
electronics and gaming section. It extracts product names, prices, images, and links
from multiple pages and saves the data to a CSV file.

Features:
- Multi-page scraping with automatic pagination detection
- Product data extraction (name, price, image URL, product link)
- Duplicate removal based on product name and link
- Error handling and logging
- CSV export with UTF-8 encoding
"""

from playwright.sync_api import sync_playwright, TimeoutError
import pandas as pd
from urllib.parse import urljoin
import logging


# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration constants
BASE_URL = "https://gcc.luluhypermarket.com/ar-sa/electronics-gaming?page="
OUTPUT_FILE = "luluhypermarket_products.csv"


def extract_product_data(element, page_url):
    """
    Extracts product information from a single product element on the page.
    
    This function parses the HTML structure of a product card to extract:
    - Product name from the anchor tag
    - Price from the price span element
    - Image URL from the img tag
    - Product link from the anchor tag
    
    Args:
        element: Playwright ElementHandle representing a product card
        page_url (str): Current page URL for constructing absolute links
        
    Returns:
        dict: Dictionary containing product information with keys:
            - name (str): Product name/title
            - price (float): Product price (None if not available)
            - image_url (str): URL to product image (None if not available)
            - link (str): Direct link to product page
        None: If product data extraction fails
        
    Example:
        >>> element = page.query_selector('div[class*="rounded-[32px]"]')
        >>> product = extract_product_data(element, "https://gcc.luluhypermarket.com/ar-sa/electronics-gaming?page=1")
        >>> print(product)
        {'name': 'Samsung Galaxy S21', 'price': 2999.0, 'image_url': 'https://...', 'link': 'https://...'}
    """
    product = {}
    try:
        # Extract image URL from img tag
        img_element = element.query_selector('img')
        product['image_url'] = img_element.get_attribute('src') if img_element else None

        # Extract product name and link from anchor tag
        a_element = element.query_selector('a[data-testid]')
        if a_element:
            product['name'] = a_element.text_content().strip()
            # Convert relative URL to absolute URL
            product['link'] = urljoin(page_url, a_element.get_attribute('href'))

        # Extract and parse price from price span
        price_element = element.query_selector('span[data-testid="product-price"]')
        if price_element:
            price_text = price_element.text_content().strip().replace(",", "")
            try:
                product['price'] = float(price_text)
            except ValueError:
                # Handle cases where price text cannot be converted to float
                product['price'] = None
                
        # Only return product if we successfully extracted a name
        return product if 'name' in product else None
        
    except Exception as e:
        logging.warning(f"Failed to extract product data: {e}")
        return None


def scrape_products():
    """
    Scrapes product information from all pages of Lulu Hypermarket electronics section.
    
    This function implements a pagination-aware scraper that:
    1. Launches a browser instance
    2. Iterates through pages until no more products are found
    3. Extracts product data from each page
    4. Handles timeouts and errors gracefully
    5. Returns all collected product records
    
    The scraper uses CSS selectors to identify product containers and automatically
    detects when it has reached the last page by checking for empty product lists.
    
    Returns:
        list: List of dictionaries, each containing product information
        
    Example:
        >>> products = scrape_products()
        >>> print(f"Scraped {len(products)} products")
        >>> print(products[0])
        {'name': 'Samsung Galaxy S21', 'price': 2999.0, 'image_url': 'https://...', 'link': 'https://...'}
        
    Note:
        This function opens a visible browser window (headless=False) for debugging.
        Set headless=True in production for faster execution.
    """
    records = []
    with sync_playwright() as p:
        # Launch browser with visible window for debugging
        browser = p.chromium.launch(headless=False)
        page_number = 1

        try:
            while True:
                # Create new page for each iteration to avoid memory issues
                page = browser.new_page()
                logging.info(f"Navigating to page {page_number}")
                
                # Navigate to the current page with timeout
                page.goto(f"{BASE_URL}{page_number}", timeout=15000)

                try:
                    # Wait for page content to load
                    page.wait_for_load_state('domcontentloaded', timeout=10000)
                except TimeoutError:
                    logging.warning("Page took too long to load.")
                    page.close()
                    break

                # CSS selector to find product containers
                # Targets div elements with specific styling classes
                css_selector = 'div[class*="rounded-[32px]"][class*="border"][class*="border-[#d9d9d9]"]'
                elements = page.query_selector_all(css_selector)

                # If no products found, we've reached the end
                if not elements:
                    logging.info("No more products found. Stopping.")
                    page.close()
                    break

                # Extract data from each product element
                for element in elements:
                    product = extract_product_data(element, page.url)
                    if product:
                        records.append(product)

                # Clean up page and move to next
                page.close()
                page_number += 1

        finally:
            # Ensure browser is always closed
            browser.close()

    return records


def save_to_csv(records, filename):
    """
    Saves product records to a CSV file with duplicate removal.
    
    This function processes the scraped data by:
    1. Converting the list of dictionaries to a pandas DataFrame
    2. Removing duplicate products based on name and link
    3. Saving to CSV with UTF-8 encoding for Arabic text support
    4. Logging the results
    
    Args:
        records (list): List of product dictionaries to save
        filename (str): Output CSV filename
        
    Example:
        >>> products = [{'name': 'Product 1', 'price': 100}, {'name': 'Product 2', 'price': 200}]
        >>> save_to_csv(products, 'output.csv')
        INFO - Saved 2 products to 'output.csv'
        
    Note:
        The CSV is saved with UTF-8-sig encoding to ensure proper display
        of Arabic text in Excel and other applications.
    """
    if records:
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(records)
        
        # Remove duplicates based on product name and link
        df.drop_duplicates(subset=["name", "link"], inplace=True)
        
        # Save to CSV with UTF-8 encoding for Arabic text
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        logging.info(f"Saved {len(df)} products to '{filename}'")
    else:
        logging.warning("No records to save.")


if __name__ == "__main__":
    """
    Main execution block for the Lulu Hypermarket scraper.
    
    When run as a script, this will:
    1. Scrape all available products from Lulu Hypermarket electronics section
    2. Save the results to the specified CSV file
    3. Display progress information during execution
    
    Usage:
        python luluhypermarket_scraper.py
        
    Output:
        - Console logs showing scraping progress
        - CSV file with scraped product data
        - Error messages if any issues occur during scraping
    """
    # Execute the scraping process
    products = scrape_products()
    
    # Save results to CSV file
    save_to_csv(products, OUTPUT_FILE)