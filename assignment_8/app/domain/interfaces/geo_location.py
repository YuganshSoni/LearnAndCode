from abc import ABC, abstractmethod

class LocationProvider(ABC):

    @abstractmethod
    def get_coordinates(self, location : str) -> list:
        pass