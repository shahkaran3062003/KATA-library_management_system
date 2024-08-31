import json


class Book:
    # Book class holding all essential parts of Book like isbn number, author, title and publish year.
    def __init__(self, isbn: str, title: str, author: str, year: str):

        ISBN_LEN = 13
        if (len(isbn) != ISBN_LEN):
            raise ValueError("ISBN Length should be of 13.")

        if (not isbn.isnumeric()):
            raise ValueError("ISBN Should be a number.")

        if (not year.isnumeric()):
            raise ValueError("Year Should be a number.")

        if (len(year) != 4):
            raise ValueError("Year should be between of 1000 - 9999")

        self.isbn = isbn
        self.title = title
        self.author = author
        self.year: int = int(year)
        self.is_borrowed = False

    def show_book(self):
        """This function prints Book information to console. takes no parameter and not return anything.
        Parameter : None
        Return : None
        """
        print("-"*10)
        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Publication Year : {self.year}")
        print("-"*10)


class Library:
    def __init__(self, filePath):
        self.books = []
        self.load_data(filePath)

    def read_file(filePath='books_data.json'):
        """This class function read JSON file and return file object if file not found then it create new file
        Parameter = file path of json file
        Return = file object to read
        """
        import os
        if not os.path.exists(filePath):
            with open(filePath, 'w') as f:
                json.dump([], f)

        file = open(filePath)
        return file

    def load_data(self, filePath):
        """This method loads all books data from JSON file
        Parameter : file path of json file
        Return : True or False
        """
        file = Library.read_file(filePath)
        if (file):
            book_data = json.load(file)
            if (len(book_data) == 0):
                self.books = []
            else:
                for book in book_data:
                    book_obj = Book(book['isbn'], book['title'],
                                    book['author'], book['year'])
                    self.books.append(book_obj)
            print(self.books)
            return True
        else:
            return False

    def add_book(self, book):
        """This function take Book class object as parameter and store in list right now and return books list
        Parameter : Book class object
        Return : all books of Library
        """
        for library_book in self.books:
            if library_book.isbn == book.isbn:
                raise Exception(
                    f"Book with ISBN {book.isbn} is already exist in library.")
        self.books.append(book)
        return self.books

    def borrow_book(self, isbn):
        """This function takes isbn number of book and return if book is available if not then raise error
        Parameter : Book isbn number
        Return : book class object or raise Exception
        """
        for book in self.books:
            if (book.isbn == isbn and not book.is_borrowed):
                book.is_borrowed = True
                return book
        raise Exception("Book not available in library.")

    def return_book(self, isbn):
        """This function takes isbn number of book and first check is this book Borrowed?? if yes then it change Borrowed to false other wise raise error
        Parameter : Book isbn number
        return : True or raise Exception
        """
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    return True
                else:
                    raise Exception("This book is not Borrowed...")

        raise Exception(f"Book with isbn {isbn} is not available.")

    def available_books(self):
        """This function print all available books in library not including borrowed books.
        Parameter : None
        Return : None
        """
        available_books_list = []
        for book in self.books:
            if (not book.is_borrowed):
                available_books_list.append(book)

        if not available_books_list:
            raise Exception("No books are Availble...")
        else:
            return available_books_list


def main():
    user_input = None
    BOOK_FILE_PATH = 'books_data.json'
    myLibarary = Library(BOOK_FILE_PATH)
    while True:
        print("1) Add Book")
        print("2) Borrow Book")
        print("3) Return Book")
        print("4) Available Books")
        print("e) exit")
        user_input = input("Enter your choice : ")

        if (user_input == '1'):
            isbn = input("Book ISBN : ")
            title = input("Book Title : ")
            author = input("Book Author : ")
            year = input("Book Publish Year : ")
            try:
                book = Book(isbn, title, author, year)
                myLibarary.add_book(book)
                print("New book added to library!!!")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)

        elif user_input == '2':
            isbn = input("Book ISBN : ")

            try:
                book = myLibarary.borrow_book(isbn)
                book.show_book()
                print("Book Borrowed Successfully!!!")
            except Exception as e:
                print(e)

        elif user_input == '3':
            isbn = input("Enter Book ISBN : ")
            try:
                if (myLibarary.return_book(isbn)):
                    print("Book Return Successfully!!!")
            except Exception as e:
                print(e)

        elif user_input == '4':

            try:
                available_books = myLibarary.available_books()
                print("List of Available Books : ")
                for i, book in enumerate(available_books):
                    print(f"Book {i+1}")
                    book.show_book()
            except Exception as e:
                print(e)

        elif user_input == 'e':
            break

        else:
            print("Invalid input...")


if __name__ == '__main__':
    main()
