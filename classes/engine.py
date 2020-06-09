from classes.PowerSource import GasTank, Battery
from classes.exceptions import PowerSourceMismatchException, PowerSourceDepletion


class Engine:

    # Engine and PowerSource management

    def __init__(self, name, weight, powerSourceList, powerRefillList=[]):
        self.name = name
        self.weight = weight
        self.outputPower = float()
        self.powerSourceList = powerSourceList
        self.powerRefillList = powerRefillList
        pass

    def update(self, step):
        self.run(step)
        pass

    def run(self, step):
        # Consume PowerSource
        isPowerSufficent = False
        for powerSource in self.powerSourceList:
            try:
                powerSource.consume(self.outputPower, step)
                isPowerSufficent = True
            except PowerSourceDepletion:
                continue
        if not isPowerSufficent:
            raise PowerSourceDepletion
        pass


class EletricEngine(Engine):
    def __init__(self, *args):
        super(EletricEngine, *args, self).__init__()
        for powerSource in self.powerSourceList:
            if type(powerSource) != Battery:
                raise PowerSourceMismatchException

        self.isDayTime = bool()
        pass

    def update(self, step, isDayTime):
        self.isDayTime = isDayTime
        self.run(step)

    def run(self, step):
        # Consume PowerSource
        super().run(step)
        # Charge up (if supported)
        powerAvailable = float()
        for powerRefill in self.powerRefillList:
            powerRefill.update(self.isDayTime)
            powerAvailable += powerRefill.getOutputPower()

        for powerSource in self.powerSourceList:
            if type(powerSource) == Battery:
                chargingPower = powerSource.getChargingPower()
                if powerAvailable > chargingPower:
                    powerSource.chargeUp(step)
                    powerAvailable -= chargingPower
                else:
                    # partial charge
                    powerSource.chargeUp(step *
                                         powerAvailable / chargingPower)
                    break


class GasEngine(Engine):
    def __init__(self, *args):
        super(GasEngine, *args, self).__init__()
        for powerSource in self.powerSourceList:
            if type(powerSource) != GasTank:
                raise PowerSourceMismatchException
        pass
