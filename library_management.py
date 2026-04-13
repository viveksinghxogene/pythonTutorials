#this is the sample code for the library management to test the working of the opps concepts (polymorphism) in real world application

class Book:
    def __init__(self,title,author,isbn):
                self.title=title
                self.author=author
                self.isbn=isbn
    def display_info(self):
        print(f"The title of the book is {self.title}")
        print(f"The author of the book is: {self.author}")
        print(f"The ISBN number of the book is: {self.isbn}")

class Library:
    def __init__(self):
        self.book=[]
    def addBook(self,book):
        self.book.append(book)
        print(f'the book with ISBN {book.isbn} is successfully added to the library!')
    def removeBook(self,isbn):
        book_to_remove=None
        for book in self.book:
            if book.isbn==isbn:
                book_to_remove=book
            if book_to_remove:
                self.book.remove(book_to_remove)
            print(f'the book {book_to_remove.title} is removed successfully')
    def display_book(self):
        if self.book is None:
            print('there is no book in the library as of now')
        else :
            for book in self.book:
                book.display_info()
class SpecialLibrary(Library):
    def addBook(self,book):
        super().addBook(book)
        print(f'the book is added to the special library successfully')

b1=Book("Little Life","Vivek Singh","987654321")
b2=Book("Sucession of the Logan Roy","Roman Roy","923145678")
b3=Book("Vigilantes","Anime Lover","987655555551")
library=Library()
library.addBook(b1)
library.addBook(b2)
library.display_book()
library.addBook(b3)
library.display_book()
sl1=SpecialLibrary()
sl1.addBook(b1)
sl1.addBook(b2)
