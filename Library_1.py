class Library1:
    def __init__(self, list_of_books, name_library):
        self.books = list_of_books
        self.name_library = name_library
        self.lend_books = {}

    def displaybooks(self):
        for books in self.books:
            print(books)
    def Lend_books(self, book, reader):
        if book not in self.lend_books.keys():
                self.lend_books.update({book : reader})
                print(f"YOU HAVE LENDED {book} BOOK")
        else:
            print(f"Sorry the book {self.lend_books[book]} is lended by someone")
            print(self.lend_books)
    def addBooks(self, book):
        self.books.append(book)
        print("YOUR BOOK HAS ADDED")
    def returnBook(self,book):
        self.lend_books.pop(book)
if __name__ == '__main__':
    lis = ["PYTHON", "JAVA", "C", "C++", "MYSQL"]
    sona = Library1(lis, "SONA'S LIBRARY")

    while True:
        n = input("Enter the keys: ")
        print(f"Welcome to the {sona.name_library}")
        if n == "display":
            sona.displaybooks()
        elif n == "add":
            book1 = input("Enter the book name: ")
            sona.addBooks(book1)
        elif n == "lend":
            book2 = input("Enter book name to lend book: ")
            reader = input("Enter ur name: ")
            sona.Lend_books(book2, reader)
        elif n == "Return":
            book3 = input("Enter book name to return: ")
            sona.returnBook(book3)
        else:
            print("Not a valid option")
        print("Enter q to quit and c to continue")
        user = ""
        while user != "q" and user != "c":
            user = input()
            if user == "q":
                exit()
            elif user == "c":
                continue





