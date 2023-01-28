class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError('Количество сраниц дожно быть целочисленным')
        if new_pages <= 0:
            raise ValueError('Количество сраниц дожно быть положительным')
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Объём {self.pages} страниц(ы)."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError('Длительность книги дожна быть вещественнным числом')
        if new_duration <= 0:
            raise ValueError('Длительность книги дожна быть положительной')
        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность {self.duration} минут(ы)."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
