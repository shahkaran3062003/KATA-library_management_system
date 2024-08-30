class Book:
    # Book class holding all essential parts of Book like isbn number, author, title and publish year.
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


books = []


def add_book(book):
    """This function take Book class object as parameter and store in list right now and return books list"""
    books.append(book)
    return books


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
            year = int(input("Book Publish Year : "))
            book = Book(isbn, title, author, year)
            add_book(book)
            print("New book added to library!!!")

        elif user_input == 'e':
            break


if __name__ == '__main__':
    main()
