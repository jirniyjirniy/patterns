from abc import ABC, abstractmethod
import copy
from builder_copy import (SpaghettiBase, DoughDepth, DoughType, Protein, Sauce, Toppings, Vegetables, Decor)


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Spaghetti(Prototype):
    def __init__(self,
                 name,
                 dough=SpaghettiBase(DoughDepth.THICK, DoughType.RICE),
                 protein=Protein.PORK,
                 sauce=Sauce.CHILE,
                 vegetables=Vegetables.ONION,
                 toppings=None,
                 decor=Decor.SESAME,
                 cooking_time=10
                 ):
        self.name = name
        self.dough = dough
        self.protein = protein
        self.sauce = sauce
        self.vegetables = vegetables
        self.toppings = toppings
        self.decor = decor
        self.cooking_time = cooking_time

    def __str__(self):
        info: str = f'Spaghetti name: {self.name} \n' \
                    f'Dough type: {self.dough.DoughDepth.name} & ' \
                    f'{self.dough.DoughType.name} \n' \
                    f'Protein: {self.protein} \n' \
                    f'Sauce: {self.sauce} \n' \
                    f'Vegetables: {self.vegetables} \n' \
                    f'Topping: {self.toppings} \n' \
                    f'Decor: {self.decor} \n'\
                    f'Cooking Time: {self.cooking_time}'
        return info

    def clone(self):
        toppings = copy.deepcopy(self.toppings) if self.toppings is not None else None
        return type(self)(
            self.name,
            self.dough,
            self.protein,
            self.sauce,
            self.vegetables,
            toppings,
            self.decor
        )


if __name__ == '__main__':
    spaghetti = Spaghetti('Spicy', toppings=[Toppings.NORI, Toppings.MANGO],)
    print(spaghetti, '-------------------------', sep='\n')
    new_spaghetti = spaghetti.clone()
    new_spaghetti.name = 'New Spaghetti Copy'
    new_spaghetti.protein = Protein.BEEF
    new_spaghetti.cooking_time = 25
    print(new_spaghetti)
