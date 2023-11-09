from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple


SpaghettiBase = namedtuple('SpaghettiBase', ['DoughDepth', 'DoughType'])

class DoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class DoughType(Enum):
    BUCKWHEAT = auto()
    RICE = auto()
    WHEAT = ()


class Protein(Enum):
    CHICKEN = auto()
    PORK = auto()
    BEEF = auto()
    SHRIMPS = auto()
    TOFU = auto()

    def __str__(self):
        return self.name


class Sauce(Enum):
    SOY = auto()
    SWEET_AND_SOUR = auto()
    TERIYAKI = auto()
    CURRY = auto()
    CHILE = auto()

    def __str__(self):
        return self.name


class Vegetables(Enum):
    PEPPER = auto()
    ONION = auto()
    CARROT = auto()
    MUSHROOMS = auto()
    CABBAGE = auto()

    def __str__(self):
        return self.name


class Toppings(Enum):
    EGG = auto()
    CORN = auto()
    MANGO = auto()
    NORI = auto()

    def __str__(self):
        return self.name


class Decor(Enum):
    SESAME = auto()
    GREEN_ONIONS = auto()
    NORI = auto()

    def __str__(self):
        return self.name


class Spaghetti:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.protein = []
        self.sauce = None
        self.vegetables = []
        self.toppings = []
        self.decor = []
        self.cooking_time = None

    def __str__(self):
        info: str = f'Spaghetti name: {self.name} \n'\
                    f'Dough type: {self.dough.DoughDepth.name} & '\
                    f'{self.dough.DoughType.name} \n'\
                    f'Protein: {self.protein} \n'\
                    f'Sauce: {self.sauce} \n'\
                    f'Vegetables: {self.vegetables} \n'\
                    f'Topping: {self.toppings} \n'\
                    f'Decor: {self.decor}'
        return info


class Builder(ABC):
    @abstractmethod
    def prepare_dough(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_protein(self) -> None:
        pass

    @abstractmethod
    def add_vegetables(self) -> None:
        pass

    @abstractmethod
    def add_topping(self) -> None:
        pass

    @abstractmethod
    def add_decor(self) -> None:
        pass


class SpicyPorkSpaghetti(Builder):
    def __init__(self):
        self.spaghetti = Spaghetti('SpicySpaghetti')
        self.spaghetti.cooking_time = 20

    def prepare_dough(self) -> None:
        self.spaghetti.dough = SpaghettiBase(DoughDepth.THICK, DoughType.WHEAT)

    def add_protein(self) -> None:
        self.spaghetti.protein = Protein.PORK

    def add_sauce(self) -> None:
        self.spaghetti.sauce = Sauce.CHILE

    def add_topping(self) -> None:
        self.spaghetti.toppings = Toppings.EGG

    def add_vegetables(self) -> None:
        self.spaghetti.vegetables.extend([t for t in (Vegetables.PEPPER, Vegetables.ONION, Vegetables.CABBAGE)])

    def add_decor(self) -> None:
        self.spaghetti.decor = Decor.GREEN_ONIONS

    def get_spaghetti(self) -> Spaghetti:
        return self.spaghetti


class SeaFoodSpaghetti(Builder):
    def __init__(self):
        self.spaghetti = Spaghetti('SpicyPorkSpaghetti')
        self.spaghetti.cooking_time = 20

    def prepare_dough(self) -> None:
        self.spaghetti.dough = SpaghettiBase(DoughDepth.THICK, DoughType.RICE)

    def add_protein(self) -> None:
        self.spaghetti.protein = Protein.SHRIMPS

    def add_sauce(self) -> None:
        self.spaghetti.sauce = Sauce.TERIYAKI

    def add_topping(self) -> None:
        self.spaghetti.toppings = Toppings.NORI

    def add_decor(self) -> None:
        self.spaghetti.decor = Decor.GREEN_ONIONS

    def add_vegetables(self) -> None:
        self.spaghetti.vegetables.extend([t for t in (Vegetables.ONION, Vegetables.MUSHROOMS, Vegetables.CARROT)])

    def get_spaghetti(self) -> Spaghetti:
        return self.spaghetti


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_spaghetti(self):
        if not self.builder:
            raise ValueError('Builder dead')
        self.builder.prepare_dough()
        self.builder.add_protein()
        self.builder.add_sauce()
        self.builder.add_topping()
        self.builder.add_vegetables()
        self.builder.add_decor()


if __name__ == '__main__':
    director = Director()
    for sp in (SpicyPorkSpaghetti, SeaFoodSpaghetti):
        builder = sp()
        director.set_builder(builder)
        director.make_spaghetti()
        spaghetti = builder.get_spaghetti()
        print(spaghetti, '-----------------', sep='\n')