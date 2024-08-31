import unittest
from library import Library, Book
import json


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.TEST_FILE_PATH = 'test_book_data.json'
        self.myLibrary = Library(self.TEST_FILE_PATH)
        self.book_1 = Book('1234567890123', 'Learn Python', 'xyz', '2024')
        self.book_2 = Book('1234567880123', 'Learn Python 2', 'xyz', '2024')

    def tearDown(self):
        del self.myLibrary
        with open(self.TEST_FILE_PATH, 'w') as wf:
            json.dump([], wf)

    def test_read_file(self):
        self.assertIsNotNone(Library.read_file(self.TEST_FILE_PATH))
        self.assertTrue(Library.read_file(self.TEST_FILE_PATH))

    def test_write_data(self):
        new_library = Library(self.TEST_FILE_PATH)
        new_library.add_book(self.book_1)
        new_library.add_book(self.book_2)
        del new_library
        file = open(self.TEST_FILE_PATH)
        if (file):
            data = json.load(file)
            self.assertEqual(
                data, [self.book_1.to_dict(), self.book_2.to_dict()])

        file.close()

    def test_load_data(self):
        self.assertIsNotNone(self.myLibrary.load_data(self.TEST_FILE_PATH))
        self.assertTrue(self.myLibrary.load_data(self.TEST_FILE_PATH))

    def test_add_book(self):
        duplicate_book = Book('1234567890123', 'Learn C++', 'xyz', '2024')

        self.assertEqual(self.myLibrary.add_book(self.book_1), [self.book_1])
        self.assertEqual(self.myLibrary.add_book(
            self.book_2), [self.book_1, self.book_2])

        self.assertRaises(Exception, self.myLibrary.add_book, duplicate_book)

    def test_book_class(self):
        book_3 = Book('1234567890123', 'fjdlksjfsdkl', 'dfjlkdslkfads', '2024')

        self.assertRaises(ValueError, Book,
                          'fdksfjl', 'fdsajklf', 'fkljdsljf', '2023')
        self.assertRaises(ValueError, Book,
                          '123456', 'fdsajklf', 'fkljdsljf', '2023')
        self.assertRaises(ValueError, Book,
                          '1234567890123', 'fdsajklf', 'fkljdsljf', 'fdsaf')
        self.assertRaises(ValueError, Book,
                          '1234567890123', 'fdsajklf', 'fkljdsljf', '200')
        self.assertRaises(ValueError, Book,
                          '1234567890123', 'fdsajklf', 'fkljdsljf', '10001')
        self.assertIsInstance(book_3.isbn, str)
        self.assertIsInstance(book_3.year, int)
        self.assertGreaterEqual(book_3.year, 999)
        self.assertLessEqual(book_3.year, 9999)
        self.assertEqual(book_3.isbn.isnumeric(), True)
        self.assertEqual(len(book_3.isbn), 13)

    def test_borrow_book(self):
        self.myLibrary.add_book(Book('1234567890123', 'xyz', 'xyz', '2024'))
        self.assertIsNotNone(self.myLibrary.borrow_book(isbn='1234567890123'))

        self.assertRaises(Exception, self.myLibrary.borrow_book, '90909090')

        self.assertRaises(
            Exception, self.myLibrary.borrow_book, '1234567890123')

    def test_return_book(self):
        self.myLibrary.add_book(self.book_1)
        self.myLibrary.borrow_book(isbn=self.book_1.isbn)
        self.assertTrue(self.myLibrary.return_book(isbn='1234567890123'))

        self.myLibrary.add_book(self.book_2)
        self.assertRaises(
            Exception, self.myLibrary.return_book, '1234567880123')

        self.assertRaises(Exception, self.myLibrary.return_book, '')
        self.assertRaises(
            Exception, self.myLibrary.return_book, '1234567890123')

    def test_available_books(self):
        new_library = Library(self.TEST_FILE_PATH)
        new_library.add_book(self.book_1)
        new_library.add_book(self.book_2)

        self.assertIsNotNone(new_library.available_books())
        self.assertEqual(new_library.available_books(),
                         [self.book_1, self.book_2])

        new_library.borrow_book(self.book_1.isbn)
        self.assertEqual(new_library.available_books(), [self.book_2])

        new_library.borrow_book(self.book_2.isbn)
        self.assertRaises(Exception, new_library.available_books)

    def test_update_book(self):
        self.myLibrary.add_book(self.book_1)
        self.myLibrary.add_book(self.book_2)
        self.assertIsNotNone(self.myLibrary.update_book(
            self.book_1.isbn, "C++", "XYZ", "2024"))


if __name__ == '__main__':
    unittest.main()
