# Create a list of dictionaries, representing a book (title, author, year) & print all books by a specific author.
books = [
  {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
  {"title": "1984", "author": "George Orwell", "year": 1949},
  {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
  {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
  {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]


search_author = input("Enter author name: ").strip()   
search_author = search_author.lower()               

print(f"\nBooks by {search_author.title()}:")        

found = False
for book in books:
  if book["author"].lower() == search_author:      
    print(f"{book['title']} ({book['year']})")
    found = True

if not found:
  print("No books found for this author.")