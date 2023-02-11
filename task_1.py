if __name__ == "__main__":
    class Car:
        def __init__(self, expenditure: int, stamp: str, fuel: int = 100):
            """
            Создание и подготовка к работе объекта "Машина"
            все непубличные параметры задаются производителем автомобиля и пользователь не может менять менять
            такие значения, как расход топлива или марка,
            но он может расходовать топливо и заправиться с помощью методов.
            :param expenditure: Расход топлива на 1 км
            :param fuel: Объем топлива в процентах
            :param stamp: Марка автомообиля
            Примеры:
            >>> сar = Car(12, 'Skoda', 100)  # инициализация экземпляра класса
            """
            self._expenditure = expenditure
            self._fuel = fuel
            self._stamp = stamp

        @property
        def expenditure(self) -> int:
            return self._expenditure

        @property
        def fuel(self) -> int:
            return self._fuel

        @property
        def stamp(self) -> str:
            return self._stamp

        def __str__(self) -> str:
            return f"Автомобиль марки {self.stamp}." \
                   f"Имеет расход топлива на 1 км {self.expenditure}, запас топлива {self.fuel}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(expenditure={self.expenditure!r}," \
                   f"stamp={self.stamp!r}, fuel={self.fuel!r})"

        def refill(self):
            """
            Функция которая заправляет автомобиль.
            Примеры:
            >>> сar = Car(12,'Skoda',50)
            >>> сar.refill()
            """
            if 0 <= self.fuel < 100:
                self._fuel = 100
                print('Машина запрвлена.')
            elif self._fuel == 100:
                print('Машина в запрвке не нуждается.')

        def driving(self, distance: int):
            """
            Функция которая инициализирует езду автомобиля на заданное расстояние в км.
            Примеры:
            >>> сar = Car(12, 'Skoda', 100)
            >>> сar.driving
            """
            self._fuel -= distance * self.expenditure
            print(f'Машина проехала {distance!r} и израсходовала {distance * self.expenditure!r}')


    class Truck(Car):
        def __init__(self, expenditure: int, stamp: str, fuel: int = 100, workload: bool = False):
            """
            Создание и подготовка к работе объекта "Грузовик"
            все прошлые атрибуты наследуются и добавляется один новый,
            он также непубличный так как по умолчанию грузовик
            разгружен и есть методы для изменения этого.
            :param workload: Загружен ли грузовик в даннй момент, по умолчанию нет.
            Примеры:
            >>> truck = Truck(12,'Камаз',100)  # инициализация экземпляра подкласса
            """
            super().__init__(expenditure, stamp, fuel)
            self._workload = workload

        @property
        def workload(self) -> int:
            return self._workload

        def __str__(self) -> str:
            return f"Грузовик марки {self.stamp}." \
                   f"Имеет расход топлива на 100 км {self.expenditure}, запас топлива {self.fuel}" \
                   f" и загруженность {self.workload}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(expenditure={self.expenditure!r}," \
                   f"stamp={self.stamp!r}, fuel={self.fuel!r}, load_capacity={self.workload !r})"

        def driving(self, distance: int):
            """
            Функция которая инициализирует езду автомобиля на заданное расстояние в км, но теперь
            ещё и проверяет загружжен ли грузовик, так как от этого меняется расход топлива.
            Примеры:
            >>> truck = Truck(12,'Камаз',100)
            >>> truck.driving(50)
            """
            if not self.workload:
                self._fuel -= distance * self.expenditure
                print(f'Машина проехала {distance!r} и израсходовала {distance * self.expenditure!r}')
            else:
                self._fuel -= distance * self.expenditure * 2
                print(f'Машина проехала {distance!r} и израсходовала {distance * self.expenditure * 2!r}')

        def loading(self):
            """
            Функция которая инициализирует загрузку и выгрузку грузовика.
            Примеры:
            >>> truck = Truck(12,'Камаз',100)
            >>> truck.loading()
            """
            if not self.workload:
                self._workload = True
                print('')
            else:
                self._workload = False
