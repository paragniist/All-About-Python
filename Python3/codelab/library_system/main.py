import book
import library
import borrower

# Create Books
book1 = book.Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = book.Book("1984", "George Orwell")
book3 = book.Book("Brave New World", "Aldous Huxley")
book4 = book.Book("Pride and Prejudice", "Jane Austen")

# Add books to Library
lib = library.Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

print("Initial books in the library:")
for b in lib.inventory:
    print("- " + b.title)

# Create Borrowers
john = borrower.Borrower("John Doe")
jane = borrower.Borrower("Jane Smith")

print("\nJohn tries to borrow 'The Great Gatsby'...")
lib.checkout_book(book1, john)

print("\nJane tries to borrow 'The Great Gatsby'...")  # This should fail since John already borrowed it
lib.checkout_book(book1, jane)

print("\nBooks John has borrowed:")
for b in john.borrowed_books:
    print("- " + b.title)

print("\nAvailable books in the library:")
print(lib.list_available_books())

print("\nJane tries to return 'The Great Gatsby'...")  # This should fail since Jane never borrowed it
lib.return_book(book1, jane)

print("\nJohn returns 'The Great Gatsby'...")
lib.return_book(book1, john)

print("\nJane tries again to borrow 'The Great Gatsby'...")  # This should succeed now
lib.checkout_book(book1, jane)

print("\nBooks Jane has borrowed:")
for b in jane.borrowed_books:
    print("- " + b.title)

print("\nCurrent available books in the library:")
print(lib.list_available_books())
