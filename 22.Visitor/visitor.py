from abc import ABC, abstractmethod
from typing import List


class OrderItemVisitor(ABC):
    @abstractmethod
    def visit(self, item) -> float:
        pass


class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor: OrderItemVisitor) -> float:
        pass


class Pizza(ItemElement):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class Coffee(ItemElement):
    def __init__(self, name: str,
                 price: float,
                 capacity: float):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self) -> float:
        return self.price

    def get_capacity(self) -> float:
        return self.capacity

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class WithOutDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyPizzaDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
            cost -= cost * 0.15
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.35
        return cost


class AllDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        cost -= cost * 0.20
        return cost


class Waiter:
    def __init__(self, discount: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: OrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price


order: List[ItemElement] = [Pizza("Margherita", 12.3),
                            Coffee("Latte", 5, 0.3),
                            Pizza("FourCheeses", 10.5),
                            Pizza("Salami", 15.2),
                            Coffee("Cappuccino", 4, 0.27)]
discount = WithOutDiscountVisitor()
waiter = Waiter(discount)
waiter.set_order(order)
print(f"Order total without discounts: "
      f"{waiter.calculate_finish_price()}")
discount = OnlyPizzaDiscountVisitor()
waiter.set_discount(discount)
print(f"Order total with pizza discount: "
      f"{waiter.calculate_finish_price()}")
discount = OnlyCoffeeDiscountVisitor()
waiter.set_discount(discount)
print(f"Order total with coffee discount: "
      f"{waiter.calculate_finish_price()}")
discount = AllDiscountVisitor()
waiter.set_discount(discount)
print(f"Order total with all discounts: "
      f"{waiter.calculate_finish_price()}")
