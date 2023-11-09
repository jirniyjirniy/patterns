from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderType(Enum):
    LATTE = 1
    CAPPUCCINO = 2
    AMERICANO = 3


class Order:
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1


    def __str__(self):
        return f'Order №{self.order_id}/{self.type.name.title()}'


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        pass


class Subject(ABC):
    def __init__(self):
        self.__observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self.__observers:
            observer.update(order_id)


class Barista(Subject):
    def __init__(self):
        super().__init__()
        self.__orders: List[Order] = []
        self.__finish_orders: List[Order] = []

    def take_order(self, order: Order) -> None:
        print(f'Barista accepted {order}')
        self.__orders.append(order)

    def get_order(self, order_id: int) ->Order:
        order = None
        for it in self.__finish_orders:
            if it.id == order_id:
                order = it
                break
        self.__finish_orders.remove(order)
        return order

    def processing_order(self):
        if self.__orders:
            order = choice(self.__orders)
            self.__orders.remove(order)
            self.__finish_orders.append(order)
            print(f'Barista done {order}')
            self.notify(order.id)
        else:
            print('Barista sleeping')


class Client(Observer):
    def __init__(self, name: str, barista: Barista):
        self.__barista = barista
        self.__name = name
        self.order: Order = None

    def update(self, order_id: int) -> None:
        if self.order is not None:
            if order_id == self.order.id:
                print(f'Client {self.__name} received {self.__barista.get_order(order_id)}')
                self.__barista.detach(self)

    def create_order(self) -> None:
        order_type = choice([OrderType.LATTE, OrderType.AMERICANO, OrderType.CAPPUCCINO])
        self.order = Order(order_type)
        print(f'Client {self.__name} - {self.order}')
        self.__barista.attach(self)
        self.__barista.take_order(self.order)


if __name__ == "__main__":
    names = ['Ben', 'Sam',
             'Dave', 'Michael', 'August']
    barista = Barista()
    clients = [Client(name, barista) for name in names]
    for client in clients:
        print("-"*25)
        client.create_order()
    print('-'*25)
    print('Barista starts working')
    for _ in range(6):
        print("-"*25)
        barista.processing_order()