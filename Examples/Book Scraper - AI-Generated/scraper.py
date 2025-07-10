import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import re
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BooksToScrapeScraper:
    """
    A comprehensive web scraper for books.toscrape.com
    Extracts book information from all pages of the website
    """
    
    def __init__(self, base_url: str = "https://books.toscrape.com/"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.books_data = []
        
    def get_page_content(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a web page
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_book_info(self, book_element) -> Dict:
        """
        Extract detailed information from a single book element
        """
        try:
            # Extract title
            title_element = book_element.find('h3').find('a')
            title = title_element.get('title', '').strip()
            
            # Extract price
            price_element = book_element.find('p', class_='price_color')
            price = price_element.text.strip() if price_element else ''
            
            # Extract rating
            rating_element = book_element.find('p', class_='star-rating')
            rating = ''
            if rating_element and rating_element.get('class'):
                classes = rating_element.get('class')
                if len(classes) > 1:
                    rating = classes[1]
            
            # Extract availability
            availability_element = book_element.find('p', class_='instock availability')
            availability = availability_element.text.strip() if availability_element else ''
            
            # Extract book URL
            book_url = urljoin(self.base_url, title_element.get('href', ''))
            
            # Extract image URL
            img_element = book_element.find('img')
            image_url = urljoin(self.base_url, img_element.get('src', '')) if img_element else ''
            
            # Extract book category (from breadcrumb or parent page)
            category = self._extract_category_from_url(book_url)
            
            return {
                'title': title,
                'price': price,
                'rating': rating,
                'availability': availability,
                'book_url': book_url,
                'image_url': image_url,
                'category': category
            }
        except Exception as e:
            logger.error(f"Error extracting book info: {e}")
            return {}
    
    def _extract_category_from_url(self, book_url: str) -> str:
        """
        Extract category from book URL
        """
        try:
            # URL pattern: /catalogue/category/books/.../index.html
            path_parts = urlparse(book_url).path.split('/')
            if len(path_parts) >= 4:
                return path_parts[3].replace('-', ' ').title()
            return ''
        except:
            return ''
    
    def scrape_books_from_page(self, page_url: str) -> List[Dict]:
        """
        Scrape all books from a single page
        """
        soup = self.get_page_content(page_url)
        if not soup:
            return []
        
        books = []
        book_elements = soup.find_all('article', class_='product_pod')
        
        for book_element in book_elements:
            book_info = self.extract_book_info(book_element)
            if book_info:
                books.append(book_info)
                logger.info(f"Scraped: {book_info['title']}")
        
        return books
    
    def get_all_page_urls(self) -> List[str]:
        """
        Get URLs for all pages in the website
        """
        page_urls = [self.base_url + "catalogue/page-1.html"]
        
        # Get the first page to find pagination
        soup = self.get_page_content(page_urls[0])
        if not soup:
            return page_urls
        
        # Find pagination links
        pagination = soup.find('li', class_='next')
        if pagination:
            next_link = pagination.find('a')
            if next_link and hasattr(next_link, 'get'):
                # Extract the base pattern and find all pages
                current_url = next_link.get('href')
                if current_url:
                    # Parse the URL pattern to find total pages
                    page_num = 2
                    while True:
                        next_url = self.base_url + f"catalogue/page-{page_num}.html"
                        test_soup = self.get_page_content(next_url)
                        if test_soup and test_soup.find('article', class_='product_pod'):
                            page_urls.append(next_url)
                            page_num += 1
                        else:
                            break
        
        return page_urls
    
    def scrape_all_books(self) -> List[Dict]:
        """
        Scrape all books from all pages
        """
        logger.info("Starting to scrape all books...")
        
        page_urls = self.get_all_page_urls()
        logger.info(f"Found {len(page_urls)} pages to scrape")
        
        all_books = []
        for i, page_url in enumerate(page_urls, 1):
            logger.info(f"Scraping page {i}/{len(page_urls)}: {page_url}")
            books = self.scrape_books_from_page(page_url)
            all_books.extend(books)
            
            # Be respectful - add delay between requests
            time.sleep(1)
        
        self.books_data = all_books
        logger.info(f"Successfully scraped {len(all_books)} books")
        return all_books
    
    def save_to_csv(self, filename: str = "books_data.csv"):
        """
        Save scraped data to CSV file
        """
        if not self.books_data:
            logger.warning("No data to save. Run scrape_all_books() first.")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['title', 'price', 'rating', 'availability', 'book_url', 'image_url', 'category']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for book in self.books_data:
                    writer.writerow(book)
            
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")
    
    def save_to_json(self, filename: str = "books_data.json"):
        """
        Save scraped data to JSON file
        """
        if not self.books_data:
            logger.warning("No data to save. Run scrape_all_books() first.")
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(self.books_data, jsonfile, indent=2, ensure_ascii=False)
            
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to JSON: {e}")
    
    def create_sample_data(self):
        """
        Create sample data for testing and documentation
        """
        sample_books = [
            {
                'title': 'A Light in the Attic',
                'price': '£51.77',
                'rating': 'Three',
                'availability': 'In stock (22 available)',
                'book_url': 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
                'image_url': 'https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg',
                'category': 'Poetry'
            },
            {
                'title': 'Tipping the Velvet',
                'price': '£53.74',
                'rating': 'One',
                'availability': 'In stock (20 available)',
                'book_url': 'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
                'image_url': 'https://books.toscrape.com/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg',
                'category': 'Historical Fiction'
            },
            {
                'title': 'Soumission',
                'price': '£50.10',
                'rating': 'One',
                'availability': 'In stock (20 available)',
                'book_url': 'https://books.toscrape.com/catalogue/soumission_998/index.html',
                'image_url': 'https://books.toscrape.com/media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg',
                'category': 'Fiction'
            }
        ]
        
        # Save sample data
        with open('sample_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'price', 'rating', 'availability', 'book_url', 'image_url', 'category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in sample_books:
                writer.writerow(book)
        
        with open('sample_books.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(sample_books, jsonfile, indent=2, ensure_ascii=False)
        
        logger.info("Sample data created: sample_books.csv and sample_books.json")
        return sample_books

def analyze_html_structure():
    """
    Analyze the HTML structure of the books.toscrape.com website
    """
    print("=== HTML Structure Analysis ===")
    print("""
    The Books to Scrape website has the following HTML structure:
    
    1. Main Container: <div class="page_inner">
    2. Book Grid: <ol class="row">
    3. Individual Book: <article class="product_pod">
       - Title: <h3><a title="Book Title">Book Title</a></h3>
       - Price: <p class="price_color">£XX.XX</p>
       - Rating: <p class="star-rating One/Two/Three/Four/Five"></p>
       - Availability: <p class="instock availability">In stock (X available)</p>
       - Image: <img src="image_url" alt="Book Title">
    
    4. Pagination: <ul class="pager">
       - Next: <li class="next"><a href="next_page_url">next</a></li>
    
    5. Categories: <div class="side_categories">
       - Category Links: <a href="category_url">Category Name</a>
    """)

def main():
    """
    Main function to run the scraper
    """
    print("=== Books to Scrape - Web Scraper ===")
    print("This scraper extracts book information from https://books.toscrape.com/")
    print()
    
    # Analyze HTML structure
    analyze_html_structure()
    print()
    
    # Create scraper instance
    scraper = BooksToScrapeScraper()
    
    # Create sample data first
    print("Creating sample data...")
    sample_data = scraper.create_sample_data()
    print(f"Sample data created with {len(sample_data)} books")
    print()
    
    # Ask user if they want to scrape real data
    print("Options:")
    print("1. Use sample data (already created)")
    print("2. Scrape real data from the website")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        print("\nStarting real data scraping...")
        print("This may take a few minutes. Please be patient...")
        
        # Scrape all books
        books = scraper.scrape_all_books()
        
        if books:
            # Save data
            scraper.save_to_csv("books_data.csv")
            scraper.save_to_json("books_data.json")
            
            # Display summary
            print(f"\n=== Scraping Complete ===")
            print(f"Total books scraped: {len(books)}")
            print(f"Data saved to: books_data.csv and books_data.json")
            
            # Show first few books
            print(f"\n=== First 5 Books ===")
            for i, book in enumerate(books[:5], 1):
                print(f"{i}. {book['title']} - {book['price']} - Rating: {book['rating']}")
        else:
            print("No books were scraped. Please check your internet connection.")
    
    else:
        print("\nUsing sample data...")
        print("Sample files created: sample_books.csv and sample_books.json")
        print("\n=== Sample Books ===")
        for i, book in enumerate(sample_data, 1):
            print(f"{i}. {book['title']} - {book['price']} - Rating: {book['rating']}")

if __name__ == "__main__":
    main()
