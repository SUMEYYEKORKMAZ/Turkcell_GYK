'''
Pair-2
Sümeyye KORKMAZ
Fatma Büşra TİLKİ
Ayşenur GÖZE
Aslı ÇOŞKUN

'''

class Book:
    def __init__(self, title, author, page_count, isbn):
        self.__title = title
        self.__author = author
        self.__page_count = page_count
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def __str__(self):
        str = f"Book : {self.__title}, Author : {self.__author}, PAge Count : {self.__page_count}, ISBN : {self.__isbn}"
        return str
    

class BookAlreadyExistsError(Exception):
    pass


class Library:

    def __init__(self):
        self.__books = []
    
    def add_book(self,book):
        for b in self.__books:
            if b.get_isbn() == book.get_isbn():
                raise BookAlreadyExistsError(f"Book with ISBN {book.get_isbn()} already exists")
        self.__books.append(book)
        print(f"Book with ISBN {book.get_isbn()} succesfully added.")

    def remove_book(self,isbn):
        for book in self.__books:
            if book.get_isbn()==isbn:
                self.__books.remove(book)
                print(f"Book with ISBN {isbn} succesfully removed.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def show_books(self):
        if not self.__books:
            print ("Library is empty.")
        else:
            for book in self.__books:
                print(book)


library = Library()

books =[ 
        Book("İnsancıklar", "Fyodor Dostoyevski", 175, "0001"),
        Book("Kendime Düşünceler", "Marcus Aurelius", 184, "0002"),
        Book("Beyaz Zambaklar Ülkesinde", "Grigory Petrow", 140, "0002"),
        Book("Dorian Gray'in Potresi", "Oscar Wilde", 280, "0004")
]

for book in books:
        try:
            library.add_book(book)
        except BookAlreadyExistsError as e:
            print("Error:", e)


library.show_books()
