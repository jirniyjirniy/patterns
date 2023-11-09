from enum import Enum


class CoffeeMachine(Enum):
    LATTE = 0
    MOCHA = 1
    AMERICANO = 2


class Coffee:
    def __init__(self, name: str, milk: int, price: float):
        self.name = name
        self._milk = milk
        self._price = price

    def get_info(self) -> str:
        return f'Name: {self.name} \n'\
                f'Milk: {self._milk}ml \n'\
                f'Price: {self._price}$'


class CoffeLatte(Coffee):
    def __init__(self):
        super().__init__('Latte', 100, 5.0)


class CoffeMocha(Coffee):
    def __init__(self):
        super().__init__('Mocha', 0, 12.5)


class CoffeAmericano(Coffee):
    def __init__(self):
        super().__init__('Americano', 50, 8.0)


def create_coffee(coffee_type: CoffeeMachine) -> Coffee:
    factory_dict = {
        CoffeeMachine.LATTE: CoffeLatte,
        CoffeeMachine.MOCHA: CoffeMocha,
        CoffeeMachine.AMERICANO: CoffeAmericano
    }

    return factory_dict[coffee_type]()


if __name__ == '__main__':
    latte = create_coffee(CoffeeMachine.LATTE)
    print(latte.get_info())
