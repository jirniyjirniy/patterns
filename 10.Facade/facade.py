from abc import ABC, abstractmethod
from enum import Enum


class MenuType(Enum):
    VEGAN = 1
    NOT_VEGAN = 2
    MIXED = 3


class InterfaceMenu(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class VeganMenu(InterfaceMenu):
    def get_name(self) -> str:
        return 'Vegan Menu'


class NoteVeganMenu(InterfaceMenu):
    def get_name(self) -> str:
        return 'Not Vegan Menu'


class MixedMenu(InterfaceMenu):
    def get_name(self) -> str:
        return 'Mixed Menu'


class InterfaceClient(ABC):
    @abstractmethod
    def request_menu(self, menu: InterfaceMenu) -> None:
        pass

    @abstractmethod
    def form_order(self) -> dict:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Kitchen:
    def prepare_food(self):
        print('Food is being prepared')

    def call_waiter(self):
        print('Give the food to the waiter')


class Waiter:
    def take_order(self, client: InterfaceClient):
        print(f'The waiter took {client.get_name()}\'s order')

    def send_to_kitchen(self, kitchen: Kitchen):
        print('The waiter took the order to the kitchen')

    def serve_client(self, client: InterfaceClient):
        print(f'The dish is ready, we bring it to the client with a name {client.get_name()}')


class PizzeriaFacade:
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {
            MenuType.VEGAN: VeganMenu,
            MenuType.NOT_VEGAN: NoteVeganMenu,
            MenuType.MIXED: MixedMenu
        }

    def get_menu(self, type_menu: MenuType) -> InterfaceMenu:
        return self.menu[type_menu]()

    def take_order(self, client: InterfaceClient):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self) -> None:
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()


class Client(InterfaceClient):
    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu: InterfaceMenu) -> None:
        print(f'Client {self.name} search food in "{menu.get_name()}"')


    def form_order(self) -> dict:
        print(f'Client {self.name} do order')
        return {}

    def get_name(self) -> str:
        return self.name


if __name__ == '__main__':
    pizzeria = PizzeriaFacade()
    client1 = Client('Olga')
    client2 = Client('Nikita')
    client1.request_menu(pizzeria.get_menu(MenuType.MIXED))
    pizzeria.take_order(client1)
    client2.request_menu(pizzeria.get_menu(MenuType.NOT_VEGAN))
    pizzeria.take_order(client2)
