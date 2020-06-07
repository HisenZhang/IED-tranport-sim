from classes.PowerSource import GasTank, Battery
from classes.exceptions import PowerSourceMismatchException, PowerSourceDepletion


class Engine:

    # Engine and PowerSource management

    def __init__(self, name, weight, PowerSourceList):
        self.name = name
        self.weight = weight
        self.chargingPower = float()
        self.outputPower = float()
        self.PowerSourceList = PowerSourceList
        pass

    def update(self, step):
        self.run(step)
        pass

    def run(self, step):
        # Consume PowerSource
        isPowerSufficent = False
        for PowerSource in self.PowerSourceList:
            try:
                PowerSource.consume(self.outputPower, step)
                isPowerSufficent = True
            except PowerSourceDepletion:
                continue
        if not isPowerSufficent:
            raise PowerSourceDepletion
        pass


class EletricEngine(Engine):
    def __init__(self):
        super(EletricEngine, self).__init__()
        for PowerSource in self.PowerSourceList:
            if type(PowerSource) != Battery:
                raise PowerSourceMismatchException
        pass

    def run(self, step):
        # Consume PowerSource
        super().run(step)
        # Charge up (if supported)
        for PowerSource in self.PowerSourceList:
            if type(PowerSource) == Battery:
                PowerSource.chargeUp(self.chargingPower, step)


class GasEngine(Engine):
    def __init__(self):
        super(GasEngine, self).__init__()
        for PowerSource in self.PowerSourceList:
            if type(PowerSource) != GasTank:
                raise PowerSourceMismatchException
        pass
