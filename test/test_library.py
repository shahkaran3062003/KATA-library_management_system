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


if __name__ == '__main__':
    unittest.main()
