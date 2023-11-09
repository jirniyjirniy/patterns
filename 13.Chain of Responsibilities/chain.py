from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, TypeVar


T = TypeVar('T')


class EnumOrder(Enum):
    VEGAN = 1
    NOT_VEGAN = 2
    BINGE = 3
    NOT_ORDER = 4


class RequestOrder:
    def __init__(self, description: List[str], order_type: EnumOrder):
        self.__description = description
        self.__order_type = order_type

    @property
    def order_type(self):
        return self.__order_type

    @property
    def order_list(self):
        return self.__description


class Handler(ABC):
    def __init__(self, successor: Optional[T] = None):
        self.__successor = successor

    def handle(self, request: RequestOrder) -> None:
        res = self._check_request(request.order_type)
        if not res and self.__successor:
            self.__successor.handle(request)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, successor: Optional[T]):
        self.__successor = successor

    @abstractmethod
    def _check_request(self, request_type: EnumOrder) -> bool:
        pass


class WaiterHandler(Handler):
    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.BINGE,
                                 EnumOrder.VEGAN,
                                 EnumOrder.NOT_VEGAN)
        if check:
            print('The waiter took the order')
        else:
            print('The waiter refused the order')
        return not check


class KitchenHandler(Handler):
    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.VEGAN,
                                 EnumOrder.NOT_VEGAN)
        if check:
            print('The cook took the order')
        else:
            print('The cook refused the order')
        return check


class BarmanHandler(Handler):
    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type is EnumOrder.BINGE
        if check:
            print("Bartender pours the order")
        else:
            print("The bartender is shocked")
        return check


if __name__ == '__main__':
    kitchen = KitchenHandler()
    bar = BarmanHandler(kitchen)
    waiter = WaiterHandler()
    waiter.successor = bar
    def request_handler(request: RequestOrder):
        print(f'Waiter order {request.order_list}')
        waiter.handle(request)

    req_list = ['Spaghetti', 'Pizza']
    request = RequestOrder(req_list, EnumOrder.NOT_VEGAN)
    request_handler(request)

    req_list = ['Vodka']
    request = RequestOrder(req_list, EnumOrder.BINGE)
    request_handler(request)

    req_list = ['Hello', 'World']
    request = RequestOrder(req_list, EnumOrder.NOT_ORDER)
    request_handler(request)