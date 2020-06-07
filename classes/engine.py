from classes.powersource import GasTank, Battery


class Engine:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        pass


class EletricEngine(Engine):
    def __init__(self):
        super(EletricEngine, self).__init__()
        pass


class GasEngine(Engine):
    def __init__(self):
        super(GasEngine, self).__init__()
        pass
