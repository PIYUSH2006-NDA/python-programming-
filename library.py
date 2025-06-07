class Library:
    def __init__(self):
        self.book_name = []
        self.no_of_book = 0

    def addbook(self, book):
        self.book_name.append(book)
        self.no_of_book += 1

    def showdet(self):
        print(f"The library has {self.no_of_book} books. Book names:")
        for book in self.book_name:
            print(book)

# Create an object of Library
l1 = Library()
l1.addbook("Harry Potter 1")
l1.addbook("Harry Potter 2")
l1.showdet()
