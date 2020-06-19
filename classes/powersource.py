from classes.simobject import SimObject
from classes.exceptions import PowerSourceDepletion, BatteryDepletionException, GasDepletionException
from classes.conversion import *
from simulator.status import GLOBAL


class PowerSource(SimObject):
    def __init__(self, capacity, weight):
        self.containerWeight = weight
        self.weight = self.containerWeight
        self.capacity = capacity
        self.remaining = capacity
        pass

    def consume(self, consumeRate, consumingTime):
        # consumingTime = step
        if self.remaining > (consumeRate * consumingTime):
            self.remaining -= (consumeRate * consumingTime)
            self._updateWeight()
        else:
            raise PowerSourceDepletion

    def _updateWeight(self):
        pass


class Battery(PowerSource):
    # battery weight includes solar panel
    def __init__(self, capacity, weight, chargingPower):
        super(Battery, self).__init__(capacity, weight)
        self.isCharging = False
        self.chargingPower = chargingPower
        pass

    def getChargingPower(self):
        return self.chargingPower

    def chargeUp(self, charingTime):
        # charingTime = step
        energyAvailable = self.chargingPower * charingTime / 3600 / 1000
        if energyAvailable > self.capacity:
            self.remaining = self.capacity  # fully charged
        else:
            self.remaining += energyAvailable

    def consume(self, outputPower, consumingTime):
        try:
            super().consume(outputPower, consumingTime)
        except PowerSourceDepletion:
            raise BatteryDepletionException

    def _updateWeight(self):
        pass


class GasTank(PowerSource):
    # gasWeight: pound per gallon
    def __init__(self, capacity, weight, gasWeight):
        super(GasTank, self).__init__(capacity, weight)
        self.gasWeight = gasWeight
        self._updateWeight()
        pass

    def consume(self, consumeRate, consumingTime):
        try:
            super().consume(consumeRate, consumingTime)
        except PowerSourceDepletion:
            raise GasDepletionException

    def _updateWeight(self):
        self.weight = self.containerWeight + self.gasWeight * self.remaining


class PowerRefill(SimObject):
    def __init__(self, weight, maxOutputPower):
        self.weight = weight
        self.isAvailable = bool()
        self.maxOutputPower = maxOutputPower

    def getOutputPower(self):
        pass


class SolarPanel(PowerRefill):
    def __init__(self, weight, maxOutputPower):
        super(SolarPanel, self).__init__(weight, maxOutputPower)
        self.outputPower = float()

    def update(self, step):
        if GLOBAL['isDayTime']:
            # power may vary depending on light condition
            self.outputPower = self.maxOutputPower
        else:
            self.outputPower = 0.0

    def getOutputPower(self):
        if self.outputPower < self.maxOutputPower:
            return self.outputPower
        else:
            return self.maxOutputPower
