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

    def chargeUp(self, chargingPower, charingTime):
        # charingTime = step
        delta = self.remaining + chargingPower * charingTime
        if delta > self.capacity:
            self.remaining = self.capacity  # fully charged
        else:
            self.remaining += delta

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

