BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id: идентификатор книги
        :param name: название книги
        :param pages: кол-во страниц в книге

        Примеры:
        book1 = Book(4, "Тихий дон", 1650)  # инициализация экземпляра класса
        """

        if not isinstance(id, int):
            raise TypeError("Идентификатор должен быть типа int")
        if id <= 0:
            raise ValueError("Идентификатор должен быть положительным числом")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Имя книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Кол-во страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Кол-во страниц в книге не может быть отрицательным числом или равным 0")
        self.pages = pages
    ...
# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа str")
        self.books = books

    def get_next_book_id(self):
        if len(self.books) is 0:
            return 1
        else:
            last_book_id = self.books[-1].id
            return last_book_id + 1

    def get_index_by_book_id(self, id_in_search: int):
        for index, value in enumerate(self.books):
            if value.id is id_in_search:
                return index
            else:
                raise ValueError("Книги с запрашиваемым id не существует")
    ...


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
