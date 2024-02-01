class Book:
    def __init__(self,name,author,isbn,is_available=True):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
