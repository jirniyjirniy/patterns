from abc import ABC, abstractmethod
from typing import List


class InterfaceCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Assistant:
    def prepare_rice(self) -> None:
        print('Assistant preparing rice for sushi')

    def prepare_topping(self) -> None:
        print('Assistant prepares sushi filling')


class Sushi_Machine:
    def prepare_sushi_machine(self) -> None:
        print('Sushi machine getting ready for cooking')

    def cooking_sushi(self) -> None:
        print('Machine wraps sushi')


class ChiefCooker:
    def make_sushi_base(self):
        print('The chef makes the base for the sushi')

    def applied_rice(self):
        print('The chef puts rice on nori')

    def add_topping(self):
        print('Chef adds toppings to sushi')


class PrepareSushiMachine(InterfaceCommand):
    def __init__(self, executor: Sushi_Machine):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_sushi_machine()


class PrepareRiceCommand(InterfaceCommand):
    def __init__(self, executor: Assistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_rice()


class PrepareToppingCommand(InterfaceCommand):
    def __init__(self, executor: Assistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class CookingSushi(InterfaceCommand):
    def __init__(self, executor: Sushi_Machine):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_sushi()


class MakeSushiBase(InterfaceCommand):
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_sushi_base()


class AppliedRice(InterfaceCommand):
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.applied_rice()


class AddTopping(InterfaceCommand):
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping()


class SushiMarket:
    def __init__(self):
        self.history: List[InterfaceCommand] = []

    def add_command(self, command: InterfaceCommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print('Nothing to do!')
        else:
            for executor in self.history:
                executor.execute()
            self.history.clear()


if __name__ == '__main__':
    chief = ChiefCooker()
    assistant = Assistant()
    machine = Sushi_Machine()
    sushi_m = SushiMarket()

    sushi_m.add_command(PrepareSushiMachine(machine))
    sushi_m.add_command(MakeSushiBase(chief))
    sushi_m.add_command(PrepareRiceCommand(assistant))
    sushi_m.add_command(AppliedRice(chief))
    sushi_m.add_command(PrepareToppingCommand(assistant))
    sushi_m.add_command(AddTopping(chief))
    sushi_m.add_command(CookingSushi(machine))
    sushi_m.cook()
