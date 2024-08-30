import unittest
from library import add_book


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        book = {'isbn': '123456789', 'title': 'Learn Python',
                'author': 'xyz', 'year': 2024}
        self.assertIsNotNone(add_book(book))


if __name__ == '__main__':
    unittest.main()
