class Book:
    def __init__(self, title: str, author: str, weight: int, percent_read: int = 0):
        self._title = title
        self._author = author
        self._weight = weight
        self.percent_read = percent_read

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def percent_read(self) -> int:
        return self._percent_read

    @percent_read.setter
    def percent_read(self, value: int):
        if not (0 <= value <= 100):
            raise ValueError("Процент прочтения должен быть в диапазоне от 0 до 100 включительно.")
        self._percent_read = value

    def __str__(self) -> str:
        return f'"{self.title}" {self.author} ({self.weight} стр.) - прочитано {self.percent_read}%'


class ElectronicLibrary:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, index: int):
        if 0 <= index < len(self._books):
            del self._books[index]
        else:
            raise IndexError("Книги с таким индексом нет в библиотеке.")

    def get_book(self, index: int) -> Book:
        if 0 <= index < len(self._books):
            return self._books[index]
        else:
            raise IndexError("Книги с таким индексом нет в библиотеке.")

    def set_percent(self, index: int, percent: int):
        book = self.get_book(index)
        book.percent_read = percent

    def list_books(self):
        if not self._books:
            print("Библиотека пуста.")
        else:
            for i, book in enumerate(self._books):
                print(f"{i}: {book}")

    def __len__(self) -> int:
        return len(self._books)


if __name__ == "__main__":
    lib = ElectronicLibrary()
    book1 = Book("Война и мир", "Лев Толстой", 1300, 25)
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 600)
    lib.add_book(book1)
    lib.add_book(book2)
    print("Список книг после добавления:")
    lib.list_books()
    lib.set_percent(0, 50)
    lib.set_percent(1, 100)
    print("\nПосле изменения процентов:")
    lib.list_books()
    try:
        lib.set_percent(0, 150)
    except ValueError as e:
        print(f"\nОшибка: {e}")
    book = lib.get_book(0)
    print(f"\nНазвание: {book.title}, Автор: {book.author}, Вес: {book.weight} стр.")