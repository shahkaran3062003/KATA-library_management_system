import unittest
from library import add_book


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        self.assertIsNotNone(add_book())


if __name__ == '__main__':
    unittest.main()
