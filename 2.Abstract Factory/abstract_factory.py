from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(self, style: str):
        self._style = style

    @abstractmethod
    def create(self):
        pass


class Table(ABC):
    def __init__(self, style: str):
        self._style = style

    @abstractmethod
    def create(self):
        pass


class Sofa(ABC):
    def __init__(self, style: str):
        self._style = style

    @abstractmethod
    def create(self):
        pass


class ModernChair(Chair):
    def __init__(self):
        super().__init__('Модерн')

    def create(self):
        print(f"Создание кресла в стиле '{self._style}'")


class ModernTable(Table):
    def __init__(self):
        super().__init__('Модерн')

    def create(self):
        print(f"Создание стола в стиле '{self._style}'")


class ModernSofa(Sofa):
    def __init__(self):
        super().__init__('Модерн')

    def create(self):
        print(f"Создание дивана в стиле '{self._style}'")


class ArtDecoChair(Chair):
    def __init__(self):
        super().__init__('Ар-деко')

    def create(self):
        print(f"Создание кресла в стиле '{self._style}'")


class ArtDecoTable(Table):
    def __init__(self):
        super().__init__('Ар-деко')

    def create(self):
        print(f"Создание стола в стиле '{self._style}'")


class ArtDecoSofa(Sofa):
    def __init__(self):
        super().__init__('Ар-деко')

    def create(self):
        print(f"Создание дивана в стиле '{self._style}'")


class VictorianChair(Chair):
    def __init__(self):
        super().__init__('Викторианский')

    def create(self):
        print(f"Создание кресла в стиле '{self._style}'")


class VictorianTable(Table):
    def __init__(self):
        super().__init__('Викторианский')

    def create(self):
        print(f"Создание стола в стиле '{self._style}'")


class VictorianSofa(Sofa):
    def __init__(self):
        super().__init__('Викторианский')

    def create(self):
        print(f"Создание дивана в стиле '{self._style}'")


class AbstractFactory(ABC):
    @abstractmethod
    def get_chair(self) -> Chair:
        pass

    @abstractmethod
    def get_table(self) -> Table:
        pass

    @abstractmethod
    def get_sofa(self) -> Sofa:
        pass


class ModernFactory(AbstractFactory):
    def get_chair(self) -> Chair:
        return ModernChair()

    def get_table(self) -> Table:
        return ModernTable()

    def get_sofa(self) -> Sofa:
        return ModernSofa()


class ArtDecoFactory(AbstractFactory):
    def get_chair(self) -> Chair:
        return ArtDecoChair()

    def get_table(self) -> Table:
        return ArtDecoTable()

    def get_sofa(self) -> Sofa:
        return ArtDecoSofa()


class VictorianFactory(AbstractFactory):
    def get_chair(self) -> Chair:
        return VictorianChair()

    def get_table(self) -> Table:
        return VictorianTable()

    def get_sofa(self) -> Sofa:
        return VictorianSofa()


class Customer:
    def __init__(self, factory: AbstractFactory):
        self._factory = factory

    def create_furniture(self):
        chair = self._factory.get_chair()
        table = self._factory.get_table()
        sofa = self._factory.get_sofa()
        chair.create()
        table.create()
        sofa.create()


def create_factory(factory_name: str) -> AbstractFactory:
    factory_dict = {
        'Modern': ModernFactory,
        'Art-Deco': ArtDecoFactory,
        'Victorian': VictorianFactory
    }
    return factory_dict[factory_name]()


if __name__ == '__main__':
    factory_name = ['Modern', 'Art-Deco', 'Victorian']
    for f in factory_name:
        factory = create_factory(f)
        customer = Customer(factory)
        customer.create_furniture()
