from classes.powersource import GasTank, Battery
from classes.exceptions import PowersourceMismatch


class Engine:

    # Engine and powersource management

    def __init__(self, name, weight, powersourceList):
        self.name = name
        self.weight = weight
        self.powersourceList = powersourceList
        pass


class EletricEngine(Engine):
    def __init__(self):
        super(EletricEngine, self).__init__()
        for powersource in self.powersourceList:
            if type(powersource) != Battery:
                raise PowersourceMismatch
        pass


class GasEngine(Engine):
    def __init__(self):
        super(GasEngine, self).__init__()
        for powersource in self.powersourceList:
            if type(powersource) != GasTank:
                raise PowersourceMismatch
        pass
