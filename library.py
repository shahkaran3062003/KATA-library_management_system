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


books = []


def add_book(book):
    """This function take Book class object as parameter and store in list right now and return books list"""
    books.append(book)
    return books


def borrow_book(isbn):
    """This function takes isbn number of book and return if book is available if not then raise error"""
    for book in books:
        if (book.isbn == isbn):

            return book
    raise Exception("Book not available in library.")


def main():
    user_input = None
    while True:
        print("1) Add Book")
        print("e) exit")
        user_input = input("Enter your choice : ")

        if (user_input == '1'):
            isbn = input("Book ISBN : ")
            title = input("Book Title : ")
            author = input("Book Author : ")
            year = input("Book Publish Year : ")
            try:
                book = Book(isbn, title, author, year)
                add_book(book)
                print("New book added to library!!!")
            except ValueError as e:
                print(e)

        elif user_input == 'e':
            break


if __name__ == '__main__':
    main()
