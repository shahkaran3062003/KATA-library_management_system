import unittest


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        self.assertIsNotNone(add_book())


if __name__ == '__main__':
    unittest.main()
