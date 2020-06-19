from classes.simobject import SimObject
from classes.engine import *
from classes.conversion import *


class Vehicle(SimObject):
    def __init__(self, carWeight, trailerWeight, volume, loadList):
        self.carWeight = carWeight
        self.weight = float()
        self.trailerWeight = trailerWeight
        self.volume = volume
        # flattening loadList
        self.loadList = self._flattenList(loadList)
        self._updateWeight()
        assert self.weight < 3510 # Ford transit max payload

        self.velocity = 0.0

    def update(self, velocity, incline, step):
        self._updateWeight()
        for load in self.loadList:
            if isinstance(load, Engine):
                if isinstance(load,GasEngine):
                    fuelEfficiency = MPHtoMPG_Gas(velocity)
                    fuelEfficiency += (-0.5 / 10000) * self.weight
                    if incline >= 0:
                        fuelEfficiency += (-2) * incline
                    else:
                        fuelEfficiency += (1.3) * incline

                if isinstance(load,EletricEngine):
                    fuelEfficiency = MPHtoMPG_Electric(velocity)
                    fuelEfficiency += (-0.5 / 10000) * self.weight
                    if incline >= 0:
                        fuelEfficiency += (-2) * incline
                    else:
                        fuelEfficiency = 99999999 # MPGe -> infinity
                    fuelEfficiency = MPGtoMPKWh(fuelEfficiency)

                assert fuelEfficiency > 0

                # Speed / Fuel Efficiency -> Gallon / Hour -> Gallon / millsec
                consumeRate = velocity / fuelEfficiency / 3600 / 1000
                load.update(consumeRate, step)

    def _updateWeight(self):
        weightSum = 0
        for item in self.loadList:
            weightSum += item.weight
        self.weight = weightSum  # carWeight is considered builtin

    def load(self, objectList):
        self.loadList.extend(objectList)
        self._updateWeight()

    def __str__(self):
        retString = ""
        for item in self.loadList:
            retString += item.__str__()
        return retString
