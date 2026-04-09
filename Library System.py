#library system using OOP in python
by Aya Alzwghaibi

# --- STEP 1: Define the classes ---

# Represents an individual book in the system
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # New books are available by default

# Represents a person using the library
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store Book objects borrowed by this member

    # Prints a list of books currently held by this specific member
    def display_my_books(self):
        print(f"\n--- Books borrowed by {self.name} ---")
        if not self.borrowed_books:
            print("You haven't borrowed any books yet.")
        else:
            # enumerate helps us create a numbered list (1, 2, 3...)
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book.title} (Author: {book.author})")   

# Manages the collection of books and the logic for borrowing/returning
class Library:
    def __init__(self):
        self.books = []  # Main storage for all Book objects in the library

    # Adds a new Book object to the library's collection
    def add_book(self, book):
        self.books.append(book)

    # Logic to borrow a book: checks if it exists and is currently available
    def borrow_book(self, member, title):
        for book in self.books:
            # .lower() ensures "python" matches "Python"
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False  # Change status to unavailable
                member.borrowed_books.append(book)  # Add book to member's list
                # This only runs if the loop finishes without finding the book
                print(f"\nSuccess: You have borrowed '{book.title}'.")
                return
        print(f"Error: '{title}' is not available.")

    # Logic to return a book: checks if the member actually has the book
    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title.lower() == title.lower():
                book.is_available = True  # Make the book available again
                member.borrowed_books.remove(book)  # Remove from member's list
                print(f"Success: You returned '{book.title}'.")
                return
        print(f"Error: You don't have '{title}' in your list.")

    # Displays all books in the library and whether they are available or borrowed
    def display_books(self):
        print("\n--- Library Collection ---")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"[{status}] {book.title} by {book.author}")
    

# --- STEP 2: Execution (The Main Program) ---

# 1. Initialize the library and populate it with Book objects
my_library = Library()
my_library.add_book(Book("Python Basics", "John Smith"))
my_library.add_book(Book("Networking 101", "Alice Brown"))
my_library.add_book(Book("Web Design", "Sara Lee"))
my_library.add_book(Book("Software Design", "Ali Ali"))

# 2. Setup the User (Member)
print("\nWelcome to the Library System\n")
name_input = input("Enter your name: ")
user = Member(name_input)  # Create a Member object using the input name

# 3. Interactive Menu Loop
while True:
    print(f"\nWelcome {user.name}! How can I help you?\n")
    print("1. View Library Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View MY Borrowed Books")
    print("5. Exit")
    
    choice = input("Select (1-5): ")

    if choice == '1':
        my_library.display_books()
        
    elif choice == '2':
        t = input("Enter book title to borrow: ")
        # Pass the 'user' object so the library can update the member's list
        my_library.borrow_book(user, t)
        
    elif choice == '3':
        t = input("Enter book title to return: ")
        # Pass the 'user' object so the library can remove the book from it
        my_library.return_book(user, t)
        
    elif choice == '4':
        # Use the member's own method to show their books
        user.display_my_books()
        
    elif choice == '5':
        print(f"Goodbye {user.name}!")
        break  # End the loop and exit the program
    else:
        print("Invalid choice. Please pick 1 through 5.")
