import unittest
from library import add_book


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        book_1 = {'isbn': '123456789', 'title': 'Learn Python',
                  'author': 'xyz', 'year': 2024}

        book_2 = {'isbn': '123456788', 'title': 'Learn Python 2',
                  'author': 'xyz', 'year': 2024}

        self.assertEqual(add_book(book_1), [book_1])
        self.assertEqual(add_book(book_2), [book_1, book_2])


if __name__ == '__main__':
    unittest.main()
