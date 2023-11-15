from abc import ABC, abstractmethod


class InterfaceSpaghetti(ABC):
    @abstractmethod
    def cost(self) -> None:
        pass


class SpaghettiBase(InterfaceSpaghetti):
    def __init__(self, cost: float):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost


class InterfaceDecorator(InterfaceSpaghetti):
    @abstractmethod
    def name(self) -> str:
        pass


class SpaghettiSpicy(InterfaceDecorator):
    def __init__(self, wrapped: SpaghettiBase, sp_cost: float):
        self.__wrapped = wrapped
        self.__sp_cost = sp_cost
        self.__name = 'Spicy Spaghetti'

    def cost(self) -> float:
        return self.__sp_cost + self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


if __name__ == '__main__':
    def nprint(spaghetti: InterfaceDecorator) -> None:
        print(f'Spaghetti {spaghetti.name()} cost {spaghetti.cost()}')

    spaghetti_base = SpaghettiBase(2.5)
    print(f'Spaghetti base cost {spaghetti_base.cost()}')
    spicy = SpaghettiSpicy(spaghetti_base, 10)
    nprint(spicy)