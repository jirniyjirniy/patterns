from abc import ABC, abstractmethod
from typing import List


class Spaghetti:
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_ingredient(self, ingredient: str) -> None:
        print(f'In pizza added {ingredient}')
        self.__state.append(ingredient)

    def __str__(self):
        return f'Ingredients in pizza: {",".join(self.__state)}'


class SpaghettiMaker(ABC):
    def make_spaghetti(self, spaghetti: Spaghetti) -> None:
        self.prepare_sauce(spaghetti)
        self.prepare_topping(spaghetti)
        self.cook(spaghetti)

    @abstractmethod
    def prepare_sauce(self, spaghetti: Spaghetti) -> None:
        pass

    @abstractmethod
    def prepare_topping(self, spaghetti: Spaghetti) -> None:
        pass

    @abstractmethod
    def cook(self, spaghetti: Spaghetti) -> None:
        pass


class SpicyPork(SpaghettiMaker):
    def prepare_sauce(self, spaghetti: Spaghetti) -> None:
        spaghetti.add_ingredient('Chily')

    def prepare_topping(self, spaghetti: Spaghetti) -> None:
        spaghetti.add_ingredient('Pork')
        spaghetti.add_ingredient('Onion')

    def cook(self, spaghetti: Spaghetti) -> None:
        print('Spaghetti "Spicy Pork" will be ready in 15 minutes')


class Vegan(SpaghettiMaker):
    def prepare_sauce(self, spaghetti: Spaghetti) -> None:
        spaghetti.add_ingredient('Kari')

    def prepare_topping(self, spaghetti: Spaghetti) -> None:
        spaghetti.add_ingredient('Tomato')
        spaghetti.add_ingredient('Onion')

    def cook(self, spaghetti: Spaghetti) -> None:
        print('Spaghetti "Vegan" will be ready in 15 minutes')


class Chief:
    def __init__(self, template_spaghetti: SpaghettiMaker):
        self.__cook = template_spaghetti

    def set_cook_template(self, template_spaghetti: SpaghettiMaker):
        self.__cook = template_spaghetti

    def make_spaghetti(self) -> Spaghetti:
        spaghetti = Spaghetti()
        self.__cook.make_spaghetti(spaghetti)
        return spaghetti


if __name__ == '__main__':
    chief = Chief(SpicyPork())
    print('-'*5, 'Spicy Pork', '-'*5)
    print(chief.make_spaghetti())
    print('-'*5, 'Vegan', '-'*5)
    chief.set_cook_template(Vegan())
    print(chief.make_spaghetti())