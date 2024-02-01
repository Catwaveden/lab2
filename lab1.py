# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Cat:
    def __init__(self, name:str, age: float, weight: float):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: имя кота
        :param age: возраст кота в месяцах
        :param weight: вес кота в килограммах

        Примеры:
        >>> cat = Cat("Мурка", 22, 2.5)  # инициализация экземпляра класса

        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должен быть str")
        self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст кота должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст кота должен быть положительным числом и не равен 0")
        self.age = age

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кота должен быть int или float")
        if weight < 0:
            raise ValueError("Вес кота не может быть отрицательным числом или равным 0")
        self.weight = weight


    def feed_the_cat(self, food_consumed: float) -> None:
        """
        Подсчет веса кота после еды

        :param food_consumed: количество съеденной еды
        :return: вес кота после еды

        Примеры:
        >>> cat = Cat("Мурка", 22, 2.5)
        >>> cat.feed_the_cat(0.035)
        """
        ...

    def cat_show_category(self, age_limit: float) -> None:
        """
        Определение того, к какому классу на кошачьей выставке относится кот в зависимости от возраста
        :param age_limit: минимальный допустимый возраст кота-участника
        :raise ValueError: Если возраст меньше допустимого, вызываем ошибку.
        :return: Категория участника (int)

        Примеры:
        >>> cat = Cat("Мурка", 22, 2.5)
        >>> cat.cat_show_category(4)
        """
        ...


class TelegramChannel:
    def __init__(self, name:str, followers: int, posts: int):
        """
        Создание и подготовка к работе объекта "Телеграм Канал"

        :param name: название канала
        :param followers: количество читателей канала
        :param posts: количество постов в канале

        Примеры:
        >>> channel = TelegramChannel("Это смешно или нет", 5267, 1252)  # инициализация экземпляра класса

        """
        if not isinstance(name, str):
            raise TypeError("Имя канала должен быть str")
        self.name = name

        if not isinstance(followers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if followers <= 0:
            raise ValueError("Количество подписчиков должно быть положительным числом")
        self.followers = followers

        if not isinstance(posts, int):
            raise TypeError("Количество постов должно быть типа int")
        if posts <= 0:
            raise ValueError("Количество постов не может быть отрицательным числом")
        self.posts = posts


    def add_post(self, posts_added: int) -> None:
        """
        Подсчет общего количество постов после публикации новых

        :param posts_added: количество опубликованных постов

        Примеры:
        >>> channel = TelegramChannel("Это смешно или нет", 5267, 1252)
        >>> channel.add_post(3)
        """
        ...

    def subscribed_channel(self, subscribed_users: int) -> None:
        """
        Подсчет подписчиков канала после того, как на него кто-то подписался
        :param subscribed_users: количество новых подписчиков
        :raise TypeError: Если subscribed_users не типа int
        :raise ValueError: Если количество подписавшихся 0 и меньше, вызываем ошибку.

        Примеры:
        >>> channel = TelegramChannel("Это смешно или нет", 5267, 1252)
        >>> channel.subscribed_channel(7)
        """
        ...
    def unsubscribed_channel(self, unsubscribed_users: int) -> None:
        """
        Подсчет подписчиков канала после того, как от него кто-то отписался
        :param unsubscribed_users: количество отписавшихся пользователей
        :raise TypeError: Если unsubscribed_users не типа int
        :raise ValueError: Если количество отписавшихся меньше 0 или больше общего числа подписчиков followers, вызываем ошибку.


        Примеры:
        >>> channel = TelegramChannel("Это смешно или нет", 5267, 1252)
        >>> channel.unsubscribed_channel(8)
        """
        ...


class Bus:
    def __init__(self, route: int, passengers_count: int, conductor_supervised: bool):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param route: номер маршрута
        :param passengers_count: количество пассажиров в автобусе
        :param conductor_supervised: есть ли в автобусе кондуктор

        Примеры:
        >>> bus = Bus(227, 17, True)  # инициализация экземпляра класса

        """
        if not isinstance(route, int):
            raise TypeError("Номер маршрута должен быть типа int")
        if route < 0:
            raise ValueError("Номер маршрута не должен быть отрицательным числом")
        self.route = route

        if not isinstance(passengers_count, int):
            raise TypeError("Количество пассажиров должно быть типа int")
        if passengers_count < 0:
            raise ValueError("Количество пассажиров должно быть положительным числом")
        self.passengers_count = passengers_count

        if not isinstance(conductor_supervised, bool):
            raise TypeError("Наличие кондуктора должно быть типа bool")
        self.conductor_supervised = conductor_supervised


    def change_route(self, new_route: int) -> None:
        """
        Замена маршрута на новый и высадка пассажиров,-> количество пассажиров = 0

        :param new_route: новый маршрут
        :raise TypeError: Если new_route не типа int
        :raise ValueError: Если немер маршрута меньше 0, вызываем ошибку
        Примеры:
        >>> bus = Bus(227, 17, True)
        >>> bus.change_route(76)
        """
        ...

    def is_supervised(self) -> None:
        """
        Проверка есть ли кондуктор на маршруте
        :return: есть ли кондуктор или нет в автобусе
        Примеры:
        >>> bus = Bus(227, 17, True)
        >>> bus.is_supervised()
        """
        ...




if __name__ == "__main__":
    doctest.testmod()
    pass
