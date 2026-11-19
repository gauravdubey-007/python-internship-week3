"""Assignment 2: Library Management System (OOP).

Add/remove books, issue/return books.
"""

from datetime import date, timedelta

LOAN_DAYS = 14


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = None
        self.due_date = None

    @property
    def is_available(self):
        return self.issued_to is None

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = f"Issued to {self.issued_to} (due {self.due_date})"
        return f"{self.book_id:<6}{self.title:<28}{self.author:<20}{status}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"Book '{title}' added.")

    def remove_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif not book.is_available:
            print("Cannot remove a book that is currently issued.")
        else:
            del self.books[book_id]
            print(f"Book '{book.title}' removed.")

    def issue_book(self, book_id, member):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif not book.is_available:
            print(f"Sorry, '{book.title}' is already issued.")
        else:
            book.issued_to = member
            book.due_date = date.today() + timedelta(days=LOAN_DAYS)
            print(f"'{book.title}' issued to {member}. Due date: {book.due_date}")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif book.is_available:
            print("This book was not issued.")
        else:
            late_days = (date.today() - book.due_date).days
            if late_days > 0:
                print(f"Returned {late_days} day(s) late. Fine: Rs. {late_days * 2}")
            print(f"'{book.title}' returned by {book.issued_to}.")
            book.issued_to = None
            book.due_date = None

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print(f"\n{'ID':<6}{'Title':<28}{'Author':<20}Status")
        print("-" * 75)
        for book in self.books.values():
            print(book)


def main():
    library = Library()
    library.add_book("B1", "Python Basics", "Guido")
    library.add_book("B2", "Clean Code", "Robert Martin")

    while True:
        print("\n===== LIBRARY MANAGEMENT =====")
        print("1. Add Book\n2. Remove Book\n3. Issue Book\n4. Return Book")
        print("5. Display Books\n6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            book_id = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            if book_id and title and author:
                library.add_book(book_id, title, author)
            else:
                print("All fields are required.")
        elif choice == "2":
            library.remove_book(input("Book ID to remove: ").strip())
        elif choice == "3":
            book_id = input("Book ID to issue: ").strip()
            member = input("Member name: ").strip()
            if member:
                library.issue_book(book_id, member)
            else:
                print("Member name is required.")
        elif choice == "4":
            library.return_book(input("Book ID to return: ").strip())
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
