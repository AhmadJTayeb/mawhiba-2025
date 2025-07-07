import sys
from playwright.sync_api import sync_playwright

import pandas as pd

products_data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://gcc.luluhypermarket.com/ar-sa/fresh-food-fruits-vegetables/", timeout=60000)

    page.wait_for_selector("div.product-box")

    products = page.query_selector_all("div.product-box")

    for product in products:
        title_element = product.query_selector(".product-box-name")
        price_element = product.query_selector(".product-box-price")
        image_element = product.query_selector("img")

        title = title_element.inner_text().strip() if title_element else "N/A"
        price = price_element.inner_text().strip() if price_element else "N/A"
        image_url = image_element.get_attribute("src") if image_element else "N/A"

        products_data.append({
            "Title": title,
            "Price": price,
            "Image URL": image_url
        })

    df = pd.DataFrame(products_data)
    df.to_csv("luluhypermarket_products.csv", index=False, encoding='utf-8-sig')
    print("Scraped and saved", len(products_data), "products.")

    browser.close()
