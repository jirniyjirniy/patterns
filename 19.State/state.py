from typing import Dict
from abc import ABC, abstractmethod
from enum import Enum


class CoffeeState(Enum):
    IDLE = 0
    CHOOSE = 1
    CAPPUCCINO = 2
    LATTE = 3
    ESPRESSO = 4
    CHANGE_MONEY = 5


class State(ABC):
    @abstractmethod
    def insert_money(self, coffee_machine) -> None:
        pass

    @abstractmethod
    def eject_money(self, coffee_machine) -> None:
        pass

    @abstractmethod
    def make_coffee(self, coffee_machine) -> None:
        pass


class WaitingState(State):
    def insert_money(self, coffee_machine) -> None:
        print('Let\'s move on to the coffee selection state')
        coffee_machine.set_state(CoffeeState.CHOOSE)

    def eject_money(self, coffee_machine) -> None:
        print('Money?')

    def make_coffee(self, coffee_machine) -> None:
        print('For free you can go away')


class WaitChooseState(State):
    def insert_money(self, coffee_machine) -> None:
        print('Are there enough funds loaded for your order?')

    def eject_money(self, coffee_machine) -> None:
        print('Make order or go away')

    def make_coffee(self, coffee_machine) -> None:
        if coffee_machine.next_state is None:
            print('Choose coffee which you want!')
        else:
            coffee_machine.set_state(coffee_machine.next_state)


class ChangeState(State):
    def insert_money(self, coffee_machine) -> None:
        self.eject_money(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print(f'Refund {coffee_machine.money}$')
        coffee_machine.money = 0
        coffee_machine.set_state(CoffeeState.IDLE)

    def make_coffee(self, coffee_machine) -> None:
        self.eject_money(coffee_machine)


class CappuccinoState(State):
    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Not today")

    def make_coffee(self, coffee_machine) -> None:
        cost = 32
        water = 0.3
        milk = 0.1
        if coffee_machine.money >= cost:
            if (coffee_machine.water >= water and
                    coffee_machine.milk >= milk):
                print("Cooking Capuccino")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Not enough money!")


class LatteState(State):
    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Not today")

    def make_coffee(self, coffee_machine) -> None:
        cost = 40
        water = 0.3
        milk = 0.2
        if coffee_machine.money >= cost:
            if (coffee_machine.water >= water and
                    coffee_machine.milk >= milk):
                print("Cooking Latte")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Not enough money!")


class EspressoState(State):
    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Not today")

    def make_coffee(self, coffee_machine) -> None:
        cost = 25
        water = 0.3
        if coffee_machine.money >= cost:
            if coffee_machine.water >= water:
                print("Cooking Espresso!")
                coffee_machine.water -= water
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Not enough money!")


class CoffeeMachine:
    def __init__(self, water: float, milk: float):
        self.water = water
        self.milk = milk
        self.money: int = 0
        self.__states: Dict[CoffeeState, State] = {
            CoffeeState.IDLE: WaitingState(),
            CoffeeState.CHOOSE: WaitChooseState(),
            CoffeeState.CAPPUCCINO: CappuccinoState(),
            CoffeeState.LATTE: LatteState(),
            CoffeeState.ESPRESSO: EspressoState(),
            CoffeeState.CHANGE_MONEY: ChangeState()
        }
        self.__state: State = self.__states[CoffeeState.IDLE]
        self.next_state: CoffeeState = None

    def get_state(self, state: CoffeeState):
        return self.__states[state]

    def set_state(self, state: CoffeeState):
        self.__state = self.__states[state]

    def insert_money(self, money: int) -> None:
        self.money += money
        print(f'CoffeeMachine received {self.money}$')
        self.__state.insert_money(self)

    def cappuccino(self) -> None:
        print('State: Cappuccino')
        self.next_state = CoffeeState.CAPPUCCINO
        self.__state.make_coffee(self)

    def espresso(self):
        print('State: Espresso')
        self.next_state = CoffeeState.ESPRESSO
        self.__state.make_coffee(self)

    def latte(self):
        print('State: Latte')
        self.next_state = CoffeeState.LATTE
        self.__state.make_coffee(self)

    def make_coffee(self):
        print('Start cooking chosen coffee')
        self.__state.make_coffee(self)

    def return_money(self):
        self.__state.eject_money(self)


if __name__ == '__main__':
    coffee_machine = CoffeeMachine(1.0, 1.0)
    coffee_machine.make_coffee()
    coffee_machine.insert_money(10)
    coffee_machine.insert_money(10)
    coffee_machine.cappuccino()
    coffee_machine.make_coffee()
    coffee_machine.insert_money(20)
    print('---------------------')
    coffee_machine = CoffeeMachine(0.1, 0.1)
    coffee_machine.insert_money(100)
    coffee_machine.make_coffee()
    coffee_machine.latte()
    coffee_machine.make_coffee()