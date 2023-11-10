import json

from shared.imodel import IModel


class Model(IModel):
    __data: dict
    __step: int

    def __init__(self):
        self.__step = 0
        with open("data/data.json") as jsonfile:
            self.__data = json.load(jsonfile)

    def getFromKey(self, key: str) -> str:
        try:
            return self.__data[key]
        except KeyError:
            return "Key " + key + " unknown"

    def moveMobiles(self):
        self.__step += 4

    def getPlaneX(self):
        return (int(self.__data["planeStartX"]) + self.__step) % int(self.__data["width"])

    def getPlaneY(self):
        return (int(self.__data["planeStartY"]) + self.__step) % int(self.__data["height"])
