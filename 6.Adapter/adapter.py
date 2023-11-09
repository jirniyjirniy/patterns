from abc import ABC, abstractmethod


class CruiseControl(ABC):
    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def set_speed(self, sp: int) -> None:
        pass


class MilesControl(ABC):
    @abstractmethod
    def get_ml_speed(self) -> int:
        pass

    @abstractmethod
    def set_ml_speed(self, sp: int) -> None:
        pass


class KilometerControl(CruiseControl):
    def __init__(self, sp: int):
        self.speed = sp

    def set_speed(self, sp: int) -> None:
        self.speed = sp

    def get_speed(self) -> int:
        return self.speed


class CruiseControlAdapter(MilesControl):
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self, cruise_control):
        self.cruise_control = cruise_control

    def get_ml_speed(self) -> int:
        km_speed = self.cruise_control.get_speed()
        return self.km_to_miles(km_speed)

    def set_ml_speed(self, sp: int) -> None:
        km_speed = self.miles_to_km(sp)
        self.cruise_control.set_speed(km_speed)

    def get_km_speed(self) -> int:
        return self.cruise_control.get_speed()

    def km_to_miles(self, km_speed):
        return int(km_speed * self.KILOMETERS_TO_MILES)

    def miles_to_km(self, miles_speed):
        return int(miles_speed / self.KILOMETERS_TO_MILES)


if __name__ == '__main__':
    km_control = KilometerControl(100)
    km_speed = km_control.get_speed()
    print(f'Current speed in kilometers: {km_speed} km/h')
    adapter = CruiseControlAdapter(km_control)
    ml_speed = adapter.get_ml_speed()
    print(f'Current speed in miles: {ml_speed} mph')
    adapter.set_ml_speed(120)
    ml_speed = adapter.get_ml_speed()
    print(f'New speed in miles: {ml_speed} mph')
    km_speed = adapter.miles_to_km(ml_speed)
    print(f'New speed in kilometers: {km_speed}')