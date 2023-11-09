from abc import ABC, abstractmethod
import time

class Bread:
    def __init__(self, name: str, cook_time: int, cook_temperature: int):
        self.name = name
        self.cook_time = cook_time
        self.cook_temperature = cook_temperature
        self._isCook = False

    def cook(self) -> None:
        self._isCook = True

    def isCooked(self) -> bool:
        return self._isCook

class OvenImplementor(ABC):
    @abstractmethod
    def warm_up(self, temperature: int) -> None:
        pass

    @abstractmethod
    def cool_down(self, temperature: int) -> None:
        pass

    @abstractmethod
    def cook_bread(self, bread) -> None:
        pass

    @abstractmethod
    def get_temperature(self) -> int:
        pass

    @abstractmethod
    def get_oven_type(self) -> str:
        pass

class ClayOvenImplementor(OvenImplementor):
    def __init__(self, temperature: int=0):
        self.temperature = temperature
        self.type = 'Clay Oven'

    def warm_up(self, temperature: int) -> None:
        print(f'Temperature warm up from {self.temperature} to {temperature}')
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        print(f'Temperature cool down from {self.temperature} to {temperature}')
        self.temperature = temperature

    def cook_bread(self, bread: Bread) -> None:
        bread.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature

class ElectricOvenImplementor(OvenImplementor):
    def __init__(self, temperature: int):
        self.temperature = temperature
        self.type = 'Electric Oven'

    def warm_up(self, temperature: int) -> None:
        print(f'Temperature warm up from {self.temperature} to {temperature}')
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        print(f'Temperature cool down from {self.temperature} to {temperature}')
        self.temperature = temperature

    def cook_bread(self, bread: Bread) -> None:
        bread.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature

class Oven:
    def __init__(self, implementor: OvenImplementor):
        self.__implementor = implementor

    def __prepare_stove(self, temperature: int):
        current_temperature = self.__implementor.get_temperature()
        if current_temperature > temperature:
            self.__implementor.cool_down(temperature)
        elif current_temperature < temperature:
            self.__implementor.warm_up(temperature)
        else:
            print('Ideal temperature')
        print('Oven prepared')

    def cook_bread(self, bread: Bread) -> None:
        self.__prepare_stove(bread.cook_temperature)
        print(f'Cooking {bread.name} bread for {bread.cook_time} minutes at {bread.cook_temperature} C')
        self.__implementor.cook_bread(bread)
        if bread.isCooked():
            print('Bread already done!')
        else:
            print('Something wrong!')

    def change_implementor(self, implementor: OvenImplementor) -> None:
        self.__implementor = implementor

    def get_temperature(self) -> int:
        return self.__implementor.get_temperature()

    def get_implementor_name(self) -> str:
        return self.__implementor.get_oven_type()

if __name__ == '__main__':
    first_bread = Bread('Borodinsky', 15, 200)
    second_bread = Bread('White', 10, 150)

    implementor = ClayOvenImplementor()
    oven = Oven(implementor)
    print(f'Implementor type: {oven.get_implementor_name()}')
    oven.cook_bread(first_bread)
    oven.cook_bread(second_bread)

    new_implementor = ElectricOvenImplementor(oven.get_temperature())
    first_bread = Bread('Borodinsky', 19, 220)
    second_bread = Bread('White', 11, 168)
    oven = Oven(new_implementor)
    print(f'Implementor type: {oven.get_implementor_name()}')
    oven.cook_bread(first_bread)
    oven.cook_bread(second_bread)
