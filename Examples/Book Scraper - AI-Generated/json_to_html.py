import json
import os
from datetime import datetime
from typing import List, Dict, Any

class BooksHTMLConverter:
    """
    Converts books JSON data to an interactive HTML page
    """
    
    def __init__(self, json_file: str = "books_data.json"):
        self.json_file = json_file
        self.books_data = []
        self.load_data()
    
    def load_data(self):
        """Load books data from JSON file"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                self.books_data = json.load(f)
            print(f"Loaded {len(self.books_data)} books from {self.json_file}")
        except FileNotFoundError:
            print(f"Error: {self.json_file} not found. Please run the scraper first.")
            self.books_data = []
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            self.books_data = []
    
    def get_rating_stars(self, rating: str) -> str:
        """Convert rating text to star HTML"""
        rating_map = {
            'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
        }
        stars = rating_map.get(rating, 0)
        filled_stars = '★' * stars
        empty_stars = '☆' * (5 - stars)
        return f'<span class="stars">{filled_stars}{empty_stars}</span>'
    
    def get_categories(self) -> List[str]:
        """Get unique categories from books data"""
        categories = set()
        for book in self.books_data:
            if book.get('category') and book['category'].strip():
                categories.add(book['category'])
        return sorted(list(categories))
    
    def get_price_range(self) -> Dict[str, float]:
        """Get min and max prices"""
        prices = []
        for book in self.books_data:
            try:
                # Extract numeric price from "£XX.XX" format
                price_str = book.get('price', '').replace('£', '').replace(',', '')
                if price_str:
                    prices.append(float(price_str))
            except ValueError:
                continue
        
        if prices:
            return {'min': min(prices), 'max': max(prices)}
        return {'min': 0, 'max': 100}
    
    def generate_html(self, output_file: str = "books_explorer.html"):
        """Generate the complete HTML page"""
        
        # Get statistics
        total_books = len(self.books_data)
        categories = self.get_categories()
        price_range = self.get_price_range()
        
        # Create the HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Books Explorer - {total_books} Books</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        
        .stat-card {{
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 15px 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        
        .stat-card h3 {{
            font-size: 1.8rem;
            margin-bottom: 5px;
        }}
        
        .controls {{
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 25px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .controls h3 {{
            margin-bottom: 15px;
            color: #333;
            font-size: 1.3rem;
        }}
        
        .filter-row {{
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
            flex-wrap: wrap;
            align-items: center;
        }}
        
        .filter-group {{
            display: flex;
            flex-direction: column;
            gap: 5px;
        }}
        
        .filter-group label {{
            font-weight: 600;
            color: #555;
            font-size: 0.9rem;
        }}
        
        .filter-group input, .filter-group select {{
            padding: 8px 12px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }}
        
        .filter-group input:focus, .filter-group select:focus {{
            outline: none;
            border-color: #667eea;
        }}
        
        .search-box {{
            flex: 1;
            min-width: 250px;
        }}
        
        .books-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .book-card {{
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }}
        
        .book-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }}
        
        .book-image {{
            width: 100%;
            height: 250px;
            object-fit: cover;
            background: #f8f9fa;
        }}
        
        .book-info {{
            padding: 20px;
        }}
        
        .book-title {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: #333;
            line-height: 1.4;
        }}
        
        .book-price {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }}
        
        .book-rating {{
            margin-bottom: 10px;
        }}
        
        .stars {{
            color: #ffd700;
            font-size: 1.1rem;
            letter-spacing: 2px;
        }}
        
        .book-availability {{
            color: #28a745;
            font-weight: 500;
            margin-bottom: 10px;
        }}
        
        .book-category {{
            background: #f8f9fa;
            color: #666;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            display: inline-block;
        }}
        
        .book-link {{
            display: inline-block;
            margin-top: 10px;
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
        }}
        
        .book-link:hover {{
            text-decoration: underline;
        }}
        
        .no-results {{
            text-align: center;
            padding: 50px;
            color: #666;
            font-size: 1.2rem;
        }}
        
        .pagination {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 30px;
        }}
        
        .pagination button {{
            padding: 10px 15px;
            border: none;
            background: #667eea;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }}
        
        .pagination button:hover {{
            background: #5a6fd8;
        }}
        
        .pagination button:disabled {{
            background: #ccc;
            cursor: not-allowed;
        }}
        
        .pagination .current {{
            background: #4a5568;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 50px;
            opacity: 0.8;
        }}
        
        @media (max-width: 768px) {{
            .books-grid {{
                grid-template-columns: 1fr;
            }}
            
            .filter-row {{
                flex-direction: column;
                align-items: stretch;
            }}
            
            .search-box {{
                min-width: auto;
            }}
            
            .stats {{
                gap: 15px;
            }}
            
            .stat-card {{
                padding: 10px 15px;
            }}
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Books Explorer</h1>
            <p>Discover and explore {total_books} amazing books</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>{total_books}</h3>
                <p>Total Books</p>
            </div>
            <div class="stat-card">
                <h3>{len(categories)}</h3>
                <p>Categories</p>
            </div>
            <div class="stat-card">
                <h3>£{price_range['min']:.2f}</h3>
                <p>Lowest Price</p>
            </div>
            <div class="stat-card">
                <h3>£{price_range['max']:.2f}</h3>
                <p>Highest Price</p>
            </div>
        </div>
        
        <div class="controls">
            <h3>🔍 Search & Filter</h3>
            <div class="filter-row">
                <div class="filter-group search-box">
                    <label for="search">Search Books</label>
                    <input type="text" id="search" placeholder="Search by title, category, or rating...">
                </div>
                <div class="filter-group">
                    <label for="category">Category</label>
                    <select id="category">
                        <option value="">All Categories</option>
                        {''.join(f'<option value="{cat}">{cat}</option>' for cat in categories)}
                    </select>
                </div>
                <div class="filter-group">
                    <label for="rating">Rating</label>
                    <select id="rating">
                        <option value="">All Ratings</option>
                        <option value="One">⭐ One Star</option>
                        <option value="Two">⭐⭐ Two Stars</option>
                        <option value="Three">⭐⭐⭐ Three Stars</option>
                        <option value="Four">⭐⭐⭐⭐ Four Stars</option>
                        <option value="Five">⭐⭐⭐⭐⭐ Five Stars</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label for="sort">Sort By</label>
                    <select id="sort">
                        <option value="title">Title A-Z</option>
                        <option value="title-desc">Title Z-A</option>
                        <option value="price">Price Low-High</option>
                        <option value="price-desc">Price High-Low</option>
                        <option value="rating">Rating Low-High</option>
                        <option value="rating-desc">Rating High-Low</option>
                    </select>
                </div>
            </div>
        </div>
        
        <div id="books-container">
            <div class="books-grid" id="books-grid">
                {self.generate_book_cards()}
            </div>
        </div>
        
        <div class="pagination" id="pagination">
            <!-- Pagination will be generated by JavaScript -->
        </div>
        
        <div class="footer">
            <p>Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')} | Data from books.toscrape.com</p>
        </div>
    </div>

    <script>
        // Books data
        const booksData = {json.dumps(self.books_data)};
        let filteredBooks = [...booksData];
        let currentPage = 1;
        const booksPerPage = 12;
        
        // DOM elements
        const searchInput = document.getElementById('search');
        const categorySelect = document.getElementById('category');
        const ratingSelect = document.getElementById('rating');
        const sortSelect = document.getElementById('sort');
        const booksGrid = document.getElementById('books-grid');
        const pagination = document.getElementById('pagination');
        
        // Event listeners
        searchInput.addEventListener('input', filterBooks);
        categorySelect.addEventListener('change', filterBooks);
        ratingSelect.addEventListener('change', filterBooks);
        sortSelect.addEventListener('change', filterBooks);
        
        function filterBooks() {{
            const searchTerm = searchInput.value.toLowerCase();
            const selectedCategory = categorySelect.value;
            const selectedRating = ratingSelect.value;
            const sortBy = sortSelect.value;
            
            // Filter books
            filteredBooks = booksData.filter(book => {{
                const matchesSearch = book.title.toLowerCase().includes(searchTerm) ||
                                    (book.category && book.category.toLowerCase().includes(searchTerm)) ||
                                    book.rating.toLowerCase().includes(searchTerm);
                const matchesCategory = !selectedCategory || book.category === selectedCategory;
                const matchesRating = !selectedRating || book.rating === selectedRating;
                
                return matchesSearch && matchesCategory && matchesRating;
            }});
            
            // Sort books
            filteredBooks.sort((a, b) => {{
                switch(sortBy) {{
                    case 'title':
                        return a.title.localeCompare(b.title);
                    case 'title-desc':
                        return b.title.localeCompare(a.title);
                    case 'price':
                        return parseFloat(a.price.replace('£', '')) - parseFloat(b.price.replace('£', ''));
                    case 'price-desc':
                        return parseFloat(b.price.replace('£', '')) - parseFloat(a.price.replace('£', ''));
                    case 'rating':
                        return getRatingValue(a.rating) - getRatingValue(b.rating);
                    case 'rating-desc':
                        return getRatingValue(b.rating) - getRatingValue(a.rating);
                    default:
                        return 0;
                }}
            }});
            
            currentPage = 1;
            displayBooks();
            updatePagination();
        }}
        
        function getRatingValue(rating) {{
            const ratingMap = {{'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}};
            return ratingMap[rating] || 0;
        }}
        
        function getRatingStars(rating) {{
            const ratingMap = {{'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}};
            const stars = ratingMap[rating] || 0;
            const filledStars = '★'.repeat(stars);
            const emptyStars = '☆'.repeat(5 - stars);
            return `<span class="stars">${{filledStars}}${{emptyStars}}</span>`;
        }}
        
        function displayBooks() {{
            const startIndex = (currentPage - 1) * booksPerPage;
            const endIndex = startIndex + booksPerPage;
            const booksToShow = filteredBooks.slice(startIndex, endIndex);
            
            if (booksToShow.length === 0) {{
                booksGrid.innerHTML = '<div class="no-results">No books found matching your criteria.</div>';
                return;
            }}
            
            booksGrid.innerHTML = booksToShow.map(book => {{
                const categoryHtml = book.category ? `<div class="book-category">${{book.category}}</div>` : '';
                return `
                    <div class="book-card">
                        <img src="${{book.image_url}}" alt="${{book.title}}" class="book-image" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZjhmOWZhIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPk5vIEltYWdlPC90ZXh0Pjwvc3ZnPg=='">
                        <div class="book-info">
                            <div class="book-title">${{book.title}}</div>
                            <div class="book-price">${{book.price}}</div>
                            <div class="book-rating">${{getRatingStars(book.rating)}}</div>
                            <div class="book-availability">${{book.availability || 'In stock'}}</div>
                            ${{categoryHtml}}
                            <a href="${{book.book_url}}" target="_blank" class="book-link">View Book →</a>
                        </div>
                    </div>
                `;
            }}).join('');
        }}
        
        function updatePagination() {{
            const totalPages = Math.ceil(filteredBooks.length / booksPerPage);
            
            if (totalPages <= 1) {{
                pagination.innerHTML = '';
                return;
            }}
            
            let paginationHTML = '';
            
            // Previous button
            paginationHTML += `<button onclick="changePage(${{currentPage - 1}})" ${{currentPage === 1 ? 'disabled' : ''}}>Previous</button>`;
            
            // Page numbers
            for (let i = 1; i <= totalPages; i++) {{
                if (i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {{
                    paginationHTML += `<button onclick="changePage(${{i}})" class="${{i === currentPage ? 'current' : ''}}">${{i}}</button>`;
                }} else if (i === currentPage - 3 || i === currentPage + 3) {{
                    paginationHTML += `<button disabled>...</button>`;
                }}
            }}
            
            // Next button
            paginationHTML += `<button onclick="changePage(${{currentPage + 1}})" ${{currentPage === totalPages ? 'disabled' : ''}}>Next</button>`;
            
            pagination.innerHTML = paginationHTML;
        }}
        
        function changePage(page) {{
            const totalPages = Math.ceil(filteredBooks.length / booksPerPage);
            if (page >= 1 && page <= totalPages) {{
                currentPage = page;
                displayBooks();
                updatePagination();
                window.scrollTo({{top: 0, behavior: 'smooth'}});
            }}
        }}
        
        // Initialize
        displayBooks();
        updatePagination();
        
        // Add some interactivity
        document.addEventListener('DOMContentLoaded', function() {{
            // Add loading animation
            const cards = document.querySelectorAll('.book-card');
            cards.forEach((card, index) => {{
                card.style.animationDelay = `${{index * 0.1}}s`;
                card.style.animation = 'fadeInUp 0.6s ease-out forwards';
            }});
        }});
    </script>
</body>
</html>"""
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML page generated successfully: {output_file}")
        print(f"📊 Total books: {total_books}")
        print(f"📂 Categories: {len(categories)}")
        print(f"💰 Price range: £{price_range['min']:.2f} - £{price_range['max']:.2f}")
        
        return output_file
    
    def generate_book_cards(self) -> str:
        """Generate HTML for book cards (first page only)"""
        cards_html = ""
        books_to_show = self.books_data[:12]  # Show first 12 books initially
        
        for book in books_to_show:
            category_html = f'<div class="book-category">{book.get("category", "")}</div>' if book.get("category") else ""
            
            card_html = f"""
                <div class="book-card">
                    <img src="{book.get('image_url', '')}" alt="{book.get('title', '')}" class="book-image" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZjhmOWZhIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPk5vIEltYWdlPC90ZXh0Pjwvc3ZnPg=='">
                    <div class="book-info">
                        <div class="book-title">{book.get('title', '')}</div>
                        <div class="book-price">{book.get('price', '')}</div>
                        <div class="book-rating">{self.get_rating_stars(book.get('rating', ''))}</div>
                        <div class="book-availability">{book.get('availability', 'In stock')}</div>
                        {category_html}
                        <a href="{book.get('book_url', '')}" target="_blank" class="book-link">View Book →</a>
                    </div>
                </div>
            """
            cards_html += card_html
        
        return cards_html

def main():
    """Main function to run the converter"""
    print("=== Books JSON to HTML Converter ===")
    print("Converting books_data.json to interactive HTML page...")
    print()
    
    # Create converter instance
    converter = BooksHTMLConverter()
    
    if not converter.books_data:
        print("❌ No books data found. Please run the scraper first to generate books_data.json")
        return
    
    # Generate HTML
    output_file = converter.generate_html()
    
    print()
    print("🎉 Conversion completed successfully!")
    print(f"📄 Open {output_file} in your web browser to explore the books")
    print()
    print("✨ Features included:")
    print("   • Search books by title, category, or rating")
    print("   • Filter by category and rating")
    print("   • Sort by title, price, or rating")
    print("   • Responsive design for mobile and desktop")
    print("   • Pagination for large datasets")
    print("   • Beautiful modern UI with animations")

if __name__ == "__main__":
    main() 