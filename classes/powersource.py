from classes.exceptions import PowerSourceDepletion, BatteryDepletionException, GasDepletionException


class PowerSource():
    def __init__(self, capacity, weight):
        self.weight = weight
        self.capacity = capacity
        self.remaining = capacity
        pass

    def consume(self, outputPower, consumingTime):
        # consumingTime = step
        if self.remaining > (outputPower * consumingTime):
            self.remaining -= (outputPower * consumingTime)
        else:
            raise PowerSourceDepletion


class Battery(PowerSource):
    # battery weight includes solar panel
    def __init__(self, *args, chargingPower):
        super(Battery, *args, self).__init__()
        self.isCharging = False
        self.chargingPower = chargingPower
        pass

    def getChargingPower(self):
        return self.chargingPower

    def chargeUp(self, charingTime):
        # charingTime = step
        energyAvailable = self.chargingPower * charingTime
        if energyAvailable > self.capacity:
            self.remaining = self.capacity  # fully charged
        else:
            self.remaining += energyAvailable

    def consume(self, outputPower, consumingTime):
        try:
            super().consume(outputPower, consumingTime)
        except PowerSourceDepletion:
            raise BatteryDepletionException


class GasTank(PowerSource):
    # gasWeight: pound per gallon
    def __init__(self, *args, gasWeight):
        super(GasTank, *args, self).__init__()
        self.weight += gasWeight * self.capacity
        pass

    def consume(self, outputPower, consumingTime):
        try:
            super().consume(outputPower, consumingTime)
        except PowerSourceDepletion:
            raise GasDepletionException


class PowerRefill():
    def __init__(self, weight, maxOutputPower):
        self.weight = weight
        self.isAvailable = bool()
        self.maxOutputPower = maxOutputPower

    def getOutputPower(self):
        pass


class SolarPanel(PowerRefill):
    def __init__(self, *args):
        super(SolarPanel, *args, self).__init__()
        self.outputPower = float()

    def update(self, isDayTime):
        if isDayTime:
            # power may vary depending on light condition
            self.outputPower = self.maxOutputPower
        else:
            self.outputPower = 0.0

    def getOutputPower(self):
        if self.outputPower < self.maxOutputPower:
            return self.outputPower
        else:
            return self.maxOutputPower
