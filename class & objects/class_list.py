# Book library item
class Book:
 
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
    self.is_read = False
    
  def read_book(self):
    self.is_read = True
    print(f"Book {self.title} has been read.")
    
  def info(self):
    status = "read" if self.is_read else "not read"
    print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Status: {status}")
    
# list of 3 books
books = [
    Book("Python Crash Course", "Eric Matthes", 544),
    Book("Clean Code", "Robert Martin", 464), 
    Book("Automate the Boring Stuff", "Al Sweigart", 504)
]

for book in books:
    book.info() # Show initial status
    
print("\n--- Reading first book ---")
books[1].read_book()  
books[1].info()  # Show updated status

# Show all books again
print("\n--- Final library status ---")
for book in books:
    book.info()    
 