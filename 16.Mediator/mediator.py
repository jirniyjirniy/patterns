from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from random import choice


class OrderType(Enum):
    FOOD = 1
    BINGE = 2


class Order:
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f'Order №{self.id} ({self.type.name})'


class Event(Enum):
    GET_ORDER = 1
    FINISH_ORDER = 2


class WorkerType(Enum):
    WAITER = 1
    CHIEF = 2
    BARMAN = 3


class InterfaceMediator(ABC):
    @abstractmethod
    def notify(self, worker: 'Worker', order: Order, event: Event):
        pass

    @abstractmethod
    def add_worker(self, worker: 'Worker') -> None:
        pass


class Worker(ABC):
    def __init__(self, name: str, mediator: InterfaceMediator):
        self.mediator = mediator
        self.name = name
        self.orders = []
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        pass

    @abstractmethod
    def finish_order(self, order: Order):
        pass

    @abstractmethod
    def type(self) -> WorkerType:
        pass

    def get_orders_id(self) -> List[int]:
        return [it.id for it in self.orders]


class Waiter(Worker):
    def __init__(self, name: str, mediator: InterfaceMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f'Waiter {self.name} accept {order}')
        self.mediator.notify(self, order, Event.GET_ORDER)

    def finish_order(self, order: Order):
        print(f'Waiter {self.name} carried {order} for client')
        self.orders.remove(order)

    def type(self) -> WorkerType:
        return WorkerType.WAITER


class Barman(Worker):
    def __init__(self, name: str, mediator: InterfaceMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f'Barman {self.name} accept {order}')

    def finish_order(self, order: Order):
        print(f'Barman {self.name} done')
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f'Barman {self.name} done {order}')
            self.finish_order(order)
        else:
            print(f'Barman {self.name} crying')

    def type(self) -> WorkerType:
        return WorkerType.BARMAN


class Chief(Worker):
    def __init__(self, name: str, mediator: InterfaceMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f'Chief {self.name} accept {order}')

    def finish_order(self, order):
        print(f'Chief {self.name} done {order}')
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f'Chief {self.name} done {order}')
            self.finish_order(order)
        else:
            print(f'Chief {self.name} crying')

    def type(self) -> WorkerType:
        return WorkerType.CHIEF


class WorkerMediator(InterfaceMediator):
    def __init__(self):
        self.workers = {
            WorkerType.WAITER: [],
            WorkerType.CHIEF: [],
            WorkerType.BARMAN: []
        }

    def add_worker(self, worker: 'Worker') -> None:
        if worker not in self.workers[worker.type()]:
            self.workers[worker.type()].append(worker)

    def remove_worker(self, worker: Worker):
        if worker in self.workers[worker.type()]:
            self.workers[worker.type()].remove(worker)
        if len(self.workers[worker.type()]) == 0:
            print(f'Attention worker type {worker.type().name} is absent!')

    def notify(self, worker: 'Worker', order: Order, event: Event):
        if (event is Event.GET_ORDER and worker.type() is WorkerType.WAITER):
            if order.type is OrderType.FOOD:
                chief: Chief = choice(self.workers[WorkerType.CHIEF])
                chief.take_order(order)
            else:
                barman: Barman = choice(self.workers[WorkerType.BARMAN])
                barman.take_order(order)
        elif (event is Event.FINISH_ORDER and (worker.type() is WorkerType.BARMAN or worker.type() is WorkerType.CHIEF)):
            for waiter in self.workers[WorkerType.WAITER]:
                if order.id in waiter.get_orders_id():
                    waiter.finish_order(order)
                    break
            else:
                print(f'{order} will not be left to the client')
        else:
            raise NotImplemented('GG WP')


if __name__ == '__main__':
    mediator = WorkerMediator()
    waiter1 = Waiter("Alex", mediator)
    waiter2 = Waiter('Bob', mediator)
    waiter3 = Waiter('Ben', mediator)
    barmen1 = Barman('Olga', mediator)
    barmen2 = Barman('Dasha', mediator)
    chief = Chief('Boris', mediator)

    orders = [Order(choice([OrderType.FOOD, OrderType.BINGE])) for _ in range(5)]
    for it in orders:
        print('-'*25)
        choice([waiter1, waiter2, waiter3]).take_order(it)
    print('-'*25)
    print('-'*5, 'Chief cooking dish', '-'*5)
    print('-' * 25)
    for it in range(5):
        chief.processing_order()
        print('-' * 25)
    print('-' * 25)
    print('-'*5, 'bartender mixes cocktails', '-'*5)
    print('-'*25)
    for it in range(5):
        choice([barmen1, barmen2]).processing_order()
        print('-'*25)