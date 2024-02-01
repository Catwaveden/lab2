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

    def __str__(self) -> str:
        # Вывод названия книги формата 'Книга "название_книги"'
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        # Формирование валидной python строки, по которой можно инициализировать точно такой же экземпляр."
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
    ...

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
