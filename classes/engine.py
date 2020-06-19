from classes.simobject import SimObject
from classes.powersource import GasTank, Battery
from classes.exceptions import PowerSourceMismatchException, PowerSourceDepletion


class Engine(SimObject):

    # Engine and PowerSource management

    def __init__(self, name, weight, powerSourceList, powerRefillList=[]):
        self.name = name
        self.engineWeight = weight
        self.weight = weight
        self.consumeRate = float()
        self.powerSourceList = self._flattenList(powerSourceList)
        self.powerRefillList = self._flattenList(powerRefillList)
        self._updateWeight()
        pass

    def update(self, consumeRate, step):
        self.consumeRate = consumeRate
        self.run(step)
        self._updateWeight()
        pass

    def _updateWeight(self):
        weightSum = 0
        for item in self.powerSourceList:
            weightSum += item.weight
        for item in self.powerRefillList:
            weightSum += item.weight
        self.weight = weightSum + self.engineWeight

    def run(self, step):
        # Consume PowerSource
        isPowerSufficent = False
        for powerSource in self.powerSourceList:
            try:
                powerSource.consume(self.consumeRate, step)
                isPowerSufficent = True
                break
            except PowerSourceDepletion:
                continue
        if not isPowerSufficent:
            raise PowerSourceDepletion
        pass


class EletricEngine(Engine):
    def __init__(self,  name, weight, powerSourceList, powerRefillList=[]):
        super(EletricEngine, self).__init__(
            name, weight, powerSourceList, powerRefillList)
        for powerSource in self.powerSourceList:
            if not isinstance(powerSource, Battery):
                raise PowerSourceMismatchException
        pass

    def run(self, step):
        # Charge up (if supported)
        powerAvailable = float()
        for powerRefill in self.powerRefillList:
            powerRefill.update(step)
            powerAvailable += powerRefill.getOutputPower()

        for powerSource in self.powerSourceList:
            if isinstance(powerSource, Battery):
                chargingPower = powerSource.getChargingPower()
                if powerAvailable > chargingPower:
                    powerSource.chargeUp(step)
                    powerAvailable -= chargingPower
                else:
                    # partial charge
                    powerSource.chargeUp(step *
                                         powerAvailable / chargingPower)
                    break
        # Consume PowerSource
        super().run(step)



class GasEngine(Engine):
    def __init__(self,  name, weight, powerSourceList, powerRefillList=[]):
        super(GasEngine, self).__init__(
            name, weight, powerSourceList, powerRefillList)
        for powerSource in self.powerSourceList:
            if not isinstance(powerSource, GasTank):
                raise PowerSourceMismatchException
        pass
