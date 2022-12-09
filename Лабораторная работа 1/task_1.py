import doctest
from typing import Union


class Bath:
    def __init__(self, bath_volume: Union[int, float], water_volume: Union[int, float]):
        """
               Создание и подготовка к работе объекта "Ванна"
               :param bath_volume: Объем ванны
               :param water_volume: Объем воды в ванне
               Примеры:
               >>> bath = Bath(500, 0)  # инициализация экземпляра класса
               """
        if not isinstance(bath_volume, (int, float)):
            raise TypeError("Объем ванны должен быть типа int или float")
        if bath_volume <= 0:
            raise ValueError("Объем ванны должен быть положительным числом")
        self.bath_volume = bath_volume

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Количество жидкости в ванне должно быть int или float")
        if water_volume < 0:
            raise ValueError("Количество жидкости в ванне не может быть отрицательным числом")
        if water_volume > bath_volume:
            raise ValueError("Количество жидкости в ванне не может превышать объём ванны")
        self.water_volume = water_volume

    def is_empty_bath(self) -> bool:
        """
        Функция которая проверяет является ли ванна пустой
        :return: Является ли ванна пустой
        Примеры:
        >>> bath = Bath(500, 0)
        >>> bath.is_empty_bath()
        """
        if self.water_volume == 0:
            return True
        else:
            return False

    def fill_bath(self, water: Union[int, float]) -> None:
        """
        Функция которая наполняет ванну водой
        Примеры:
        >>> bath = Bath(500, 0)
        >>> bath.fill_bath(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Количество добавляемой жидкости должно быть int или float")
        if water < 0:
            raise ValueError("Количество добавляемой жидкости не может быть отрицательным числом")
        if water > (self.bath_volume - self.water_volume):
            raise ValueError('Количество добавляемой жидкости не может превышать возможный максимум свободного объёма')
        self.water_volume += water

    def drain_water(self, retractable_water: Union[int, float]) -> None:
        """
        Извлечение воды из ванны.
        :param retractable_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в ванне,
        то возвращается ошибка.
        Примеры:
        >>> bath = Bath(500, 500)
        >>> bath.drain_water(200)
        """
        if not isinstance(retractable_water, (int, float)):
            raise TypeError("Количество извлекаемой жидкости должно быть int или float")
        if retractable_water < 0:
            raise ValueError("Количество извлекаемой жидкости не может быть отрицательным числом")
        if retractable_water > self.water_volume:
            raise ValueError('Количество извлекаемой жидкости не может превышать объём залитой жидкости')
        self.water_volume -= retractable_water


class Smartphone:
    def __init__(self, energy: Union[int, float], battery: Union[int, float]):
        """
               Создание и подготовка к работе объекта "Телефон"
               :param energy: Уровень заряда телефона
               :param battery: Объём батареи телефона
               Примеры:
               >>> smartphone = Smartphone(0, 500)  # инициализация экземпляра класса
               """
        if not isinstance(battery, (int, float)):
            raise TypeError("Уровень заряда телефона должен быть типа int или float")
        if battery <= 0:
            raise ValueError("Уровень заряда телефона должен быть положительным числом")
        self.battery = battery

        if not isinstance(energy, (int, float)):
            raise TypeError("Уровень заряда телефона должно быть int или float")
        if energy < 0:
            raise ValueError("Уровень заряда телефона не может быть отрицательным числом")
        self.energy = energy

    def is_smartphone_charged(self) -> bool:
        """
        Функция которая проверяет является ли телефон заряженным на 100%
        :return: Является ли телефон заряженным на 100%
        Примеры:
        >>> smartphone = Smartphone(500, 500)
        >>> smartphone.is_smartphone_charged()
        """
        if self.energy == self.battery:
            return True
        else:
            return False

    def is_smartphone_discharged(self) -> bool:
        """
        Функция которая проверяет является ли телефон заряженным на 0%
        :return: Является ли телефон заряженным на 0%
        Примеры:
        >>> smartphone = Smartphone(0, 500)
        >>> smartphone.is_smartphone_discharged()
        """
        if self.energy == 0:
            return True
        else:
            return False

    def charging(self, percents: int) -> None:
        """
        Зарядка телефона
        :param percents: На сколько процентов надо зарядить телефон
        Примеры:
        >>> smartphone = Smartphone(250, 500)
        >>> smartphone.charging(60)
        """
        if not isinstance(percents, int):
            raise TypeError("Количество процентов должно быть int")
        if percents < 0:
            raise ValueError("Количество процентов не может быть отрицательным числом")
        self.energy += percents * (self.battery / 100)
        if self.energy > self.battery:
            self.energy = self.battery


class Lamp:
    def __init__(self, power: bool, level_power: int, mode: bool):
        """
               Создание и подготовка к работе объекта "Лампа"
               :param power: Кнопка включения
               :param level_power: Мощность лампы(регуруется)
               :param mode: Режим мерцания
               Примеры:
               >>> lamp = Lamp(True, 50, False)  # инициализация экземпляра класса
               """
        if not isinstance(power, bool):
            raise TypeError("Кнопка включения должна быть типа bool")
        self.power = power

        if not isinstance(level_power, int):
            raise TypeError("Мощность лампы должна быть int")
        if level_power < 0:
            raise ValueError("Мощность лампы не может быть отрицательным числом")
        if level_power > 100:
            raise ValueError("Мощность лампы не может превышать 100%")
        self.level_power = level_power

        if not isinstance(mode, bool):
            raise TypeError("Режим мерцания должен быть типа bool")
        self.mode = mode

    def button_press(self) -> None:
        """
        Функция которая нажимает на кнопку вкл/выкл
        Примеры:
        >>> lamp = Lamp(True, 50, False)
        >>> lamp.button_press()
        """
        if self.power:
            self.power = False
        else:
            self.power = True

    def light_change(self, level_change: int) -> None:
        """
        Функция которая регулирует мощность лампы
        Примеры:
        >>> lamp = Lamp(True, 50, False)
        >>> lamp.light_change(-30)
        """
        if not self.power:
            raise ValueError('Для изменения мощности лампы надо её включить')
        if not isinstance(level_change, int):
            raise TypeError("Изменение мощности лампы должна быть int")
        self.level_power += level_change
        if self.level_power < 0:
            self.level_power = 0
        elif self.level_power > 100:
            self.level_power = 100

    def change_mode(self) -> None:
        """
        Включение и ввыключение режима мерцания
        Примеры:
        >>> lamp = Lamp(True, 50, False)
        >>> lamp.change_mode()
        """
        if self.mode:
            self.mode = False
        else:
            self.mode = True


if __name__ == "__main__":
    doctest.testmod()
