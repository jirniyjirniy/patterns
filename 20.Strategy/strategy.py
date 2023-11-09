from abc import ABC, abstractmethod
from enum import Enum


class TransportType(Enum):
    BICYCLE = 1
    AIRPLANE = 2
    METRO = 3


class Location(Enum):
    PARK = 1
    AIRPORT = 2
    STATION = 3
    MUSEUM = 4



class TransportStrategy(ABC):
    @abstractmethod
    def navigate(self, destination):
        pass


class BicycleStrategy(TransportStrategy):
    def navigate(self, destination):
        return f"Let's ride a bike to {destination}"


class AirplaneStrategy(TransportStrategy):
    def navigate(self, destination):
        return f"We fly by plane to {destination}"


class MetroStrategy(TransportStrategy):
    def navigate(self, destination):
        return f"Let's take the metro to {destination}"


class Navigator:
    def __init__(self, transport_strategy):
        self._transport_strategy = transport_strategy

    def set_strategy(self, transport_strategy):
        self._transport_strategy = transport_strategy

    def navigate(self, destination):
        return self._transport_strategy.navigate(destination)


class LocationManager:
    def __init__(self):
        self._locations = {
            Location.PARK: "Beautiful Park",
            Location.AIRPORT: "International Airport",
            Location.STATION: "Main station",
            Location.MUSEUM: "Famous Museum"
        }

    def get_location_description(self, location):
        return self._locations.get(location, "No description")


class TransportManager:
    def get_transport_strategy(self, transport_type):
        if transport_type == TransportType.BICYCLE:
            return BicycleStrategy()
        elif transport_type == TransportType.AIRPLANE:
            return AirplaneStrategy()
        elif transport_type == TransportType.METRO:
            return MetroStrategy()
        else:
            raise TransportTypeInvalid("Invalid transport type")


class LocationNotFound(Exception):
    pass


class TransportTypeInvalid(Exception):
    pass


"""Убрал повторение"""
def navigate_to_destination(location, transport_type):
    location_destination = location_manager.get_location_description(location)
    print(f'Destination: {location_destination}')
    transport_strategy = transport_manager.get_transport_strategy(transport_type)
    navigator = Navigator(transport_strategy)
    print(navigator.navigate(location))


if __name__ == "__main__":
    location_manager = LocationManager()
    transport_manager = TransportManager()

    try:
        """Было"""
        # destination = Location.MUSEUM
        # location_description = location_manager.get_location_description(destination)
        # print(f"Destination: {location_description}")
        # transport_type = TransportType.METRO
        # transport_strategy = transport_manager.get_transport_strategy(transport_type)
        # navigator = Navigator(transport_strategy)
        # print(navigator.navigate(destination))
        #
        # destination = Location.PARK
        # location_description = location_manager.get_location_description(destination)
        # print(f"Destination: {location_description}")
        # transport_type = TransportType.AIRPLANE
        # transport_strategy = transport_manager.get_transport_strategy(transport_type)
        # navigator.set_strategy(transport_strategy)
        # print(navigator.navigate(destination))
        #
        # destination = Location.AIRPORT
        # location_description = location_manager.get_location_description(destination)
        # print(f"Destination: {location_description}")
        # transport_type = TransportType.BICYCLE
        # transport_strategy = transport_manager.get_transport_strategy(transport_type)
        # navigator.set_strategy(transport_strategy)
        # print(navigator.navigate(destination))

        """Стало"""
        navigate_to_destination(Location.MUSEUM, TransportType.METRO)
        navigate_to_destination(Location.PARK, TransportType.AIRPLANE)
        navigate_to_destination(Location.AIRPORT, TransportType.BICYCLE)

    except LocationNotFound as e:
        print(f"Error: {e}")
    except TransportTypeInvalid as e:
        print(f"Error: {e}")
