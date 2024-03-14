import json

class Book:
    def __init__(self, judul, author, tahun):
        self.judul = judul
        self.author = author
        self.tahun = tahun

def load_books():
    try:
        with open("data/books.json", "r") as file:
            return json.load(file)['books']
    except FileNotFoundError:
        return []

def save_books(books):
    with open("data/books.json", "w") as file:
        json.dump({'books': books}, file, indent=4)

def add_book(judul, author, tahun):
    new_book = Book(judul, author, tahun)
    books = load_books()
    books.append(vars(new_book))
    save_books(books)
    print("Buku berhasil ditambahkan")

def search_book(search_term):
    books = load_books()
    search_results = []

    for book in books:
        if search_term.lower() in book['judul'].lower() or search_term.lower() in book['author'].lower():
            search_results.append(book)

    return search_results

def view_catalog():
    books = load_books()
    return books
