# class Library1:
#     books = ["a", 'b', 'c', 'd', 'e', 'f', 'g' ,'h']
#     no_of_books = len(books)

#     def no_books(self):
#         return len(self.books)
    
# lib1 = Library1()
# print(lib1.books)
# print(lib1.no_of_books)
# print(lib1.no_books())

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.no_of_books} book.")

l1 = Library()
l1.addBook("Harry Porter1")
l1.addBook("Harry Porter2")
l1.addBook("Harry Porter3")
l1.showInfo()

