from abc import ABC, abstractmethod



class InterfaceProduct(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Product(InterfaceProduct):
    def __init__(self, name: str, cost: float):
        self.__name = name
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost

    def get_name(self) -> str:
        return self.__name


class CompoundProduct(InterfaceProduct):
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def cost(self) -> float:
        cost = 0
        for prod in self.products:
            cost += prod.cost()
        return cost

    def get_name(self) -> str:
        return self.name

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def clear(self):
        self.products = []


class Spaghetti(CompoundProduct):
    def __init__(self, name: str) -> None:
        super(Spaghetti, self).__init__(name)

    def cost(self) -> float:
        cost = 0
        for sp in self.products:
            cost_sp = sp.cost()
            print(f'Цена {sp.get_name()} = {cost_sp}$')
            cost += cost_sp
        print(f'Цена спаггети {self.name} = {round(cost, 2)}$')
        return cost


if __name__ == "__main__":
    dough = CompoundProduct("тесто")
    dough.add_product(Product("мука", 3))
    dough.add_product(Product("яйцо", 2.3))
    dough.add_product(Product("соль", 1))
    dough.add_product(Product("сахар", 2.1))
    sauce = Product("Чилли", 12.1)
    topping = CompoundProduct("топпинг")
    topping.add_product(Product("Свинина", 14))
    topping.add_product(Product("Маасдам", 7.27))
    spaghetti = Spaghetti("Spicy Pork")
    spaghetti.add_product(dough)
    spaghetti.add_product(sauce)
    spaghetti.add_product(topping)
    print(round(spaghetti.cost(), 2))

