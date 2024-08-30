import unittest
from library import add_book, Book, borrow_book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book_1 = Book('1234567890123', 'Learn Python', 'xyz', '2024')
        self.book_2 = Book('1234567880123', 'Learn Python 2', 'xyz', '2024')

    def tearDown(self):
        pass

    def test_add_book(self):

        self.assertEqual(add_book(self.book_1), [self.book_1])
        self.assertEqual(add_book(self.book_2), [self.book_1, self.book_2])

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
        add_book(Book('1234567890123', 'xyz', 'xyz', '2024'))
        self.assertIsNotNone(borrow_book(isbn='1234567890123'))

        self.assertRaises(Exception, borrow_book, '90909090')

        self.asserRaise(Exception, borrow_book, '1234567890123')


if __name__ == '__main__':
    unittest.main()
