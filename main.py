from books import Book

def main():
    while True:
        print("\nOptions:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Lihat Catalog")
        print("4. Quit")

        choice = input("Menu (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            view_catalog()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Masukkan menu 1 - 4.")

def add_book():
    judul = input("Masukkan Judul: ")
    author = input("Masukkan penulis: ")
    tahun = int(input("Masukkan tahun terbit: "))
    Book.add_book(judul, author, tahun)

def search_book():
    search_term = input("Masukkan Judul: ")
    search_results = Book.search_book(search_term)
    if search_results:
        print("Search Results:")
        for book in search_results:
            print("- judul:", book['judul'])
            print("  Author:", book['author'])
            print("  tahun:", book['tahun'])
    else:
        print("No matching Book found.")

def view_catalog():
    all_Book = Book.view_catalog()
    if all_Book:
        print("All Book:")
        for book in all_Book:
            print("- judul:", book['judul'])
            print("  Author:", book['author'])
            print("  tahun:", book['tahun'])
    else:
        print("No Book in the catalog.")

if __name__ == "__main__":
    main()
