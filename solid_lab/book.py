class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

class library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

            return None

