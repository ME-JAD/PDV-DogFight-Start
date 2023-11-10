from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getFromKey(self, key: str) -> str:
        ...

    @abstractmethod
    def moveMobiles(self):
        ...

    def getPlaneX(self):
        ...

    def getPlaneY(self):
        ...
