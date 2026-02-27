class Device:
    def __init__(self, name):
        self.name = name
        # Приватный атрибут: доступ к нему ограничен внутри класса
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"[{self.name}] Прибор включен.")

    def turn_off(self):
        self.__is_on = False
        print(f"[{self.name}] Прибор выключен.")

    # Метод-геттер, чтобы дочерние классы могли проверить состояние,
    # не меняя его напрямую
    def is_enabled(self):
        return self.__is_on


class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 50

    def set_brightness(self, level):
        if self.is_enabled():
            self.brightness = level
            print(f"[{self.name}] Яркость установлена на {self.brightness}%.")
        else:
            print(f"[{self.name}] Ошибка: Нельзя изменить яркость, пока свет выключен!")


class AirConditioner(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 22

    def set_temperature(self, temp):
        if self.is_enabled():
            self.temperature = temp
            print(f"[{self.name}] Температура установлена на {self.temperature}°C.")
        else:
            print(f"[{self.name}] Ошибка: Кондиционер выключен. Сначала включите его.")