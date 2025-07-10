# Books to Scrape - Web Scraper

A comprehensive Python web scraper for extracting book information from [books.toscrape.com](https://books.toscrape.com/).

## Features

- **Complete Book Information**: Extracts title, price, rating, availability, book URL, image URL, and category
- **Multi-page Scraping**: Automatically discovers and scrapes all pages
- **Multiple Output Formats**: Saves data to CSV and JSON formats
- **Error Handling**: Robust error handling with logging
- **Rate Limiting**: Respectful scraping with delays between requests
- **Sample Data**: Includes sample data for testing and documentation
- **HTML Structure Analysis**: Provides detailed analysis of the website structure

## Installation

1. Clone or download this project
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the scraper:

```bash
python a1.py
```

The script will:
1. Display HTML structure analysis
2. Create sample data files
3. Ask if you want to use sample data or scrape real data
4. Save results to CSV and JSON files

### Programmatic Usage

```python
from a1 import BooksToScrapeScraper

# Create scraper instance
scraper = BooksToScrapeScraper()

# Scrape all books
books = scraper.scrape_all_books()

# Save to files
scraper.save_to_csv("my_books.csv")
scraper.save_to_json("my_books.json")

# Or use sample data
sample_books = scraper.create_sample_data()
```

## HTML Structure Analysis

The Books to Scrape website has the following HTML structure:

### Main Container
```html
<div class="page_inner">
```

### Book Grid
```html
<ol class="row">
```

### Individual Book
```html
<article class="product_pod">
  <!-- Title -->
  <h3><a title="Book Title">Book Title</a></h3>
  
  <!-- Price -->
  <p class="price_color">£XX.XX</p>
  
  <!-- Rating -->
  <p class="star-rating One/Two/Three/Four/Five"></p>
  
  <!-- Availability -->
  <p class="instock availability">In stock (X available)</p>
  
  <!-- Image -->
  <img src="image_url" alt="Book Title">
</article>
```

### Pagination
```html
<ul class="pager">
  <li class="next"><a href="next_page_url">next</a></li>
</ul>
```

### Categories
```html
<div class="side_categories">
  <a href="category_url">Category Name</a>
</div>
```

## Sample Data

The scraper creates sample data files with the following structure:

### CSV Format (sample_books.csv)
```csv
title,price,rating,availability,book_url,image_url,category
A Light in the Attic,£51.77,Three,In stock (22 available),https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html,https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg,Poetry
Tipping the Velvet,£53.74,One,In stock (20 available),https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html,https://books.toscrape.com/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg,Historical Fiction
Soumission,£50.10,One,In stock (20 available),https://books.toscrape.com/catalogue/soumission_998/index.html,https://books.toscrape.com/media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg,Fiction
```

### JSON Format (sample_books.json)
```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "rating": "Three",
    "availability": "In stock (22 available)",
    "book_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "image_url": "https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
    "category": "Poetry"
  },
  {
    "title": "Tipping the Velvet",
    "price": "£53.74",
    "rating": "One",
    "availability": "In stock (20 available)",
    "book_url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    "image_url": "https://books.toscrape.com/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg",
    "category": "Historical Fiction"
  }
]
```

## Output Files

When you run the scraper, it creates the following files:

- `sample_books.csv` - Sample data in CSV format
- `sample_books.json` - Sample data in JSON format
- `books_data.csv` - Real scraped data in CSV format (if option 2 is chosen)
- `books_data.json` - Real scraped data in JSON format (if option 2 is chosen)

## Data Fields

Each book entry contains the following information:

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Book title | "A Light in the Attic" |
| `price` | Book price in pounds | "£51.77" |
| `rating` | Star rating (One, Two, Three, Four, Five) | "Three" |
| `availability` | Stock availability | "In stock (22 available)" |
| `book_url` | Direct link to book page | "https://books.toscrape.com/catalogue/..." |
| `image_url` | Book cover image URL | "https://books.toscrape.com/media/cache/..." |
| `category` | Book category | "Poetry" |

## Features Explained

### 1. HTML Structure Understanding
The scraper analyzes the website's HTML structure to understand:
- How books are organized in the DOM
- Where to find specific information (title, price, rating, etc.)
- How pagination works
- How categories are structured

### 2. Robust Data Extraction
- **Title**: Extracted from the `title` attribute of the book link
- **Price**: Found in elements with class `price_color`
- **Rating**: Extracted from the `star-rating` class (One, Two, Three, Four, Five)
- **Availability**: Found in elements with class `instock availability`
- **URLs**: Both book URLs and image URLs are properly constructed
- **Category**: Extracted from the URL structure

### 3. Error Handling
- Network timeout handling
- Missing element handling
- Graceful degradation when data is unavailable
- Comprehensive logging

### 4. Rate Limiting
- 1-second delay between page requests
- Respectful scraping practices
- Session management for efficient requests

## Example Output

When you run the scraper, you'll see output like this:

```
=== Books to Scrape - Web Scraper ===
This scraper extracts book information from https://books.toscrape.com/

=== HTML Structure Analysis ===
The Books to Scrape website has the following HTML structure:
...

Creating sample data...
Sample data created with 3 books

Options:
1. Use sample data (already created)
2. Scrape real data from the website

Enter your choice (1 or 2): 2

Starting real data scraping...
This may take a few minutes. Please be patient...
2024-01-15 10:30:15 - INFO - Starting to scrape all books...
2024-01-15 10:30:15 - INFO - Found 50 pages to scrape
2024-01-15 10:30:15 - INFO - Scraping page 1/50: https://books.toscrape.com/catalogue/page-1.html
2024-01-15 10:30:16 - INFO - Scraped: A Light in the Attic
2024-01-15 10:30:16 - INFO - Scraped: Tipping the Velvet
...

=== Scraping Complete ===
Total books scraped: 1000
Data saved to: books_data.csv and books_data.json

=== First 5 Books ===
1. A Light in the Attic - £51.77 - Rating: Three
2. Tipping the Velvet - £53.74 - Rating: One
3. Soumission - £50.10 - Rating: One
4. Sharp Objects - £47.82 - Rating: Four
5. Sapiens: A Brief History of Humankind - £54.23 - Rating: Five
```

## Notes

- The website contains approximately 1000 books across 50 pages
- Each page contains 20 books
- The scraper automatically discovers all pages
- Sample data is always created for testing purposes
- Real scraping may take 2-3 minutes due to rate limiting

## Legal and Ethical Considerations

- This scraper is for educational purposes
- It includes rate limiting to be respectful to the server
- The target website (books.toscrape.com) is designed for scraping practice
- Always check a website's robots.txt and terms of service before scraping 