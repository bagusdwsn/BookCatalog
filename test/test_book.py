import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from books import Book
import json

class TestBookCatalog(unittest.TestCase):
    def setUp(self):
        # Clear the contents of books.json before each test
        with open("data/books.json", "w") as file:
            json.dump({'books': []}, file)

    def test_add_book(self):
        Book.add_book("Python Programming", "John Doe", 2022)
        all_books = Book.view_catalog()
        self.assertEqual(len(all_books), 1)
        self.assertEqual(all_books[0]['judul'], "Python Programming")
        self.assertEqual(all_books[0]['author'], "John Doe")
        self.assertEqual(all_books[0]['tahun'], 2022)

    def test_search_book(self):
        Book.add_book("Python Programming", "John Doe", 2022)
        Book.add_book("Data Science Handbook", "Jane Smith", 2021)

        # Test searching by title
        search_results = Book.search_book("Python Programming")
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0]['judul'], "Python Programming")

        # Test searching by author
        search_results = Book.search_book("Jane Smith")
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0]['author'], "Jane Smith")

    def test_view_catalog(self):
        Book.add_book("Python Programming", "John Doe", 2022)
        Book.add_book("Data Science Handbook", "Jane Smith", 2021)

        all_books = Book.view_catalog()
        self.assertEqual(len(all_books), 2)
        self.assertEqual(all_books[0]['judul'], "Python Programming")
        self.assertEqual(all_books[1]['judul'], "Data Science Handbook")

if __name__ == "__main__":
    unittest.main()
