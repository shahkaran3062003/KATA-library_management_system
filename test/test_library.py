import unittest
from library import add_book, Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book_1 = Book('123456789', 'Learn Python', 'xyz', 2024)
        self.book_2 = Book('123456788', 'Learn Python 2', 'xyz', 2024)

    def tearDown(self):
        pass

    def test_add_book(self):

        self.assertEqual(add_book(self.book_1), [self.book_1])
        self.assertEqual(add_book(self.book_2), [self.book_1, self.book_2])

    def test_book_class(self):
        book_3 = Book('fjdlfjlksd', 'fjdlksjfsdkl', 'dfjlkdslkfads', 'flkdsf')
        self.assertIsInstance(book_3.isbn, str)
        self.assertIsInstance(book_3.title, str)
        self.assertIsInstance(book_3.author, str)
        self.assertIsInstance(book_3.year, int)
        self.assertGreaterEqual(book_3.year, 999)
        self.assertLessEqual(book_3.year, 9999)
        self.assertEqual(book_3.isbn.isnumeric(), True)
        self.assertEqual(len(book_3.isbn), 13)


if __name__ == '__main__':
    unittest.main()
