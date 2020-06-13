from classes.simobject import SimObject
from classes.engine import Engine
from classes.conversion import MPHtoMPG


class Vehicle(SimObject):
    def __init__(self, carWeight, trailerWeight, volume, loadList):
        self.carWeight = carWeight
        self.weight = float()
        self.trailerWeight = trailerWeight
        self.volume = volume
        # flattening loadList
        self.loadList = self._flattenList(loadList)
        # TODO check load constraints
        self._updateWeight()

        self.velocity = 0.0

    def update(self, velocity, step):
        self._updateWeight()
        for load in self.loadList:
            if isinstance(load, Engine):
                fuelEfficiency = MPHtoMPG(velocity)
                fuelEfficiency += (-0.5 / 10000) * self.weight

                assert fuelEfficiency > 0

                # Speed / Fuel Efficiency -> Gallon / Hour -> Gallon / millsec
                consumeRate = velocity / fuelEfficiency / 3600 / 1000
                load.update(consumeRate, step)

    def _updateWeight(self):
        weightSum = 0
        for item in self.loadList:
            weightSum += item.weight
        self.weight = weightSum + self.trailerWeight  # carWeight is considered builtin

    def load(self, objectList):
        self.loadList.extend(objectList)
        self._updateWeight()

    def __str__(self):
        retString = ""
        for item in self.loadList:
            retString += item.__str__()
        return retString
