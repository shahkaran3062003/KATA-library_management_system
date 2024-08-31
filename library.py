import json


class Book:
    # Book class holding all essential parts of Book like isbn number, author, title and publish year.
    def __init__(self, isbn: str, title: str, author: str, year: str, is_borrowed=False):

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
        self.is_borrowed = is_borrowed

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

    def to_dict(self):
        book = {}
        book['isbn'] = self.isbn
        book['title'] = self.title
        book['author'] = self.author
        book['year'] = str(self.year)
        book['is_borrowed'] = self.is_borrowed
        return book


class Library:
    def __init__(self, filePath):
        self.books = []
        self.filePath = filePath
        self.load_data(filePath)

    def __del__(self):
        data = []
        for book in self.books:
            book = book.to_dict()
            data.append(book)
        with open(self.filePath, 'w') as wf:
            json.dump(data, wf)

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
        self.file = Library.read_file(filePath)
        if (self.file):
            book_data = json.load(self.file)
            print("In Load Function")
            if (len(book_data) == 0):
                self.books = []
            else:
                for book in book_data:
                    book_obj = Book(book['isbn'], book['title'],
                                    book['author'], book['year'], book['is_borrowed'])
                    self.books.append(book_obj)
            self.file.close()
            return True
        else:
            self.file.close()
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

    def update_book(self, isbn, title, author, year):
        """This function update given isbn number book data and chech year validation too.
        Parameter : isbn, new title, new author, new year
        Return : updated Book object
        """
        for book in self.books:
            if (book.isbn == isbn):
                if (not year.isnumeric()):
                    raise ValueError("Year Should be a number.")
                if (len(year) != 4):
                    raise ValueError("Year should be between of 1000 - 9999")
                book.title = title
                book.author = author
                book.year = int(year)
                return book
        raise Exception(f"Book with isbn {isbn} is not available.")

    def delete_book(self, isbn):
        """This function delete given isbn number book from library
        Parameter : isbn
        Return : deleted book object
        """
        for book in self.books:
            if book.isbn == isbn:
                delete_book = book
                self.books.remove(delete_book)
                return delete_book
        raise Exception(f"Book with isbn {isbn} is not available.")


def main():
    user_input = None
    BOOK_FILE_PATH = 'books_data.json'
    myLibarary = Library(BOOK_FILE_PATH)
    while True:
        print("1) Add Book")
        print("2) Borrow Book")
        print("3) Return Book")
        print("4) Available Books")
        print("5) Update Book")
        print("6) Remove Book")
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

        elif user_input == '5':
            try:
                isbn = input("Enter Book ISBN : ")
                title = input("Enter New Title : ")
                author = input("Enter New Author : ")
                year = input("Enter New Year : ")
                book = myLibarary.update_book(isbn, title, author, year)
                print("Book Updated Successfully!!!")
                print("New Book : ")
                book.show_book()
            except ValueError as e:
                print(e)

            except Exception as e:
                print(e)

        elif user_input == '6':
            try:
                isbn = input("Enter Book ISBN : ")
                deleted_book = myLibarary.delete_book(isbn)
                print("Book Removed Successfully!!!")
                print("Removed Book : ")
                deleted_book.show_book()
                del deleted_book
            except Exception as e:
                print(e)

        elif user_input == 'e':
            break

        else:
            print("Invalid input...")


if __name__ == '__main__':
    main()
