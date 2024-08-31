class Book:
    # Book class holding all essential parts of Book like isbn number, author, title and publish year.
    def __init__(self, isbn: str, title: str, author: str, year: str):

        if (len(isbn) != 13):
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


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """This function take Book class object as parameter and store in list right now and return books list"""
        self.books.append(book)
        return self.books

    def borrow_book(self, isbn):
        """This function takes isbn number of book and return if book is available if not then raise error"""
        for book in self.books:
            if (book.isbn == isbn and not book.is_borrowed):
                book.is_borrowed = True
                return book
        raise Exception("Book not available in library.")

    def return_book(self, isbn):
        """This function takes isbn number of book and first check is this book Borrowed?? if yes then it change Borrowed to false other wise raise error"""
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    return True
                else:
                    raise Exception("This book is not Borrowed...")

        raise Exception(f"Book with isbn {isbn} is not available.")


def main():
    user_input = None
    myLibarary = Library()
    while True:
        print("1) Add Book")
        print("2) Borrow Book")
        print("3) Return Book")
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

        elif user_input == '2':
            isbn = input("Book ISBN : ")

            try:
                book = myLibarary.borrow_book(isbn)
                print(f"ISBN : {book.isbn}")
                print(f"Title : {book.title}")
                print(f"Author : {book.author}")
                print(f"Publish Year : {book.year}")
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

        elif user_input == 'e':
            break

        else:
            print("Invalid input...")


if __name__ == '__main__':
    main()
