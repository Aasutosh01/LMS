import csv
from lib.book import Book
class Library:
    def __init__(self):
        self.books = self.load_books_from_file()

    def load_books_from_file(self):
        books = []
        try:
            with open("book.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    author = row['Author']
                    isbn = row['ISBN']
                    is_available = row['is_available'].lower() == 'true'
                    books.append(Book(name, author, isbn, is_available))
        except FileNotFoundError:
            pass
        return books


    def save_books_to_file(self):
        with open("book.csv", "a", newline="") as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.name, book.author, book.isbn, str(book.is_available)])


    def add_book(self):
        name = input("Enter Name of the Book: ")
        author = input("Enter Name of the Author: ")
        isbn = input("Enter ISBN: ")

        new_book = Book(name, author, isbn, True)
        self.books.append(new_book)
        self.save_books_to_file()

    def display_books(self):
        for book in self.books:
            print(f"{book.name} by {book.author} (ISBN: {book.isbn}) - Available: {book.is_available}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                print(f"You have borrowed '{book.name}' by {book.author}.")
                self.save_books_to_file()
                return
        print("Book not found or not available for borrowing.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_available:
                book.is_available = True
                print(f"You have returned '{book.name}' by {book.author}.")
                self.save_books_to_file()
                return
        print("Book not found or already returned.")