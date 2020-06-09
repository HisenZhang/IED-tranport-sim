class Vehicle:
    def __init__(self, carWeight, trailerWeight, volume, loadList):
        self.carWeight = carWeight
        self.weight = carWeight
        self.trailerWeight = trailerWeight
        self.volume = volume
        self.loadList = loadList
        self._updateWeight()

        self.velocity = 0
        self.power = 0

    def update(self, isDayTime):
        for load in self.loadList:
            load.update()

    def _updateWeight(self):
        weightSum = 0
        for item in self.loadList:
            weightSum += item.weight
        self.weight = weightSum + self.carWeight + self.trailerWeight

    def load(self, objectList):
        self.loadList.extend(objectList)
        self._updateWeight()

    def __str__(self):
        retString = ""
        for item in self.loadList:
            retString += item.__str__()
        return retString
