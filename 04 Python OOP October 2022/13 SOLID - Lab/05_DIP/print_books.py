class Book:
    def __init__(self, content):
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content


class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)

