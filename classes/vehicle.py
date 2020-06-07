class Vehicle:
    def __init__(self, engine, carWeight, trailerWeight, volume, loadList):
        self.carWeight = carWeight
        self.weight = carWeight
        self.trailerWeight = trailerWeight
        self.engine = engine
        self.volume = volume
        self.loadList = loadList
        self._updateWeight()

        self.velocity = 0
        self.power = 0

    def _updateWeight(self):
        weightSum = 0
        for item in self.loadList:
            weightSum += item.weight
        self.weight = weightSum + self.carWeight

    def load(self, objectList):
        self.loadList.extend(objectList)
        self._updateWeight()

    def __str__(self):
        retString = ""
        for item in self.loadList:
            retString += item.__str__()
        return retString
