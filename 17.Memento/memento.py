from typing import List


class Memento:
    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Burger:
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_ingredient(self, ingredient: str) -> None:
        print(f'Adding ingredient {ingredient}')
        self.__state.append(ingredient)

    def create_memento(self) -> Memento:
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self) -> str:
        return f'Current state of the burger: {" ".join(self.__state)}'


class Cook:
    def __init__(self, burger: Burger):
        self.burger = burger
        self.burger_state: List[Memento] = []

    def add_ingredient_to_burger(self, ingredient: str):
        self.burger_state.append(self.burger.create_memento())
        self.burger.add_ingredient(ingredient)

    def undo_add_ingredient(self):
        if len(self.burger_state) == 1:
            self.burger.set_memento(self.burger_state[0])
            print('The burger is disassembled to its original state')
            print(self.burger)
        else:
            print('Undo previous action')
            state = self.burger_state.pop()
            self.burger.set_memento(state)
            print(self.burger)


if __name__ == '__main__':
    burger = Burger()
    cook = Cook(burger)
    print(burger)
    print('Adding ingredients')
    cook.add_ingredient_to_burger('sauce')
    cook.add_ingredient_to_burger('veal cutlet')
    cook.add_ingredient_to_burger('cheese')
    cook.add_ingredient_to_burger('salted cucumbers')
    cook.add_ingredient_to_burger('onion')
    print(burger)
    print('We don\'t need onion')
    cook.undo_add_ingredient()
    print(burger)