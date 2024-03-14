import unittest
from books.Book import Book

class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        # Instance book baru
        book = Book("Sample Title", "Sample Author", 2022)

        # Check if attributes are set correctly
        self.assertEqual(book.title, "Sample Title")
        self.assertEqual(book.author, "Sample Author")
        self.assertEqual(book.year, 2022)

if __name__ == '__main__':
    unittest.main()
