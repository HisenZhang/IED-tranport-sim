class PowerFailure(Exception):
    pass

class BatteryDepletionException(PowerFailure):
    pass

class GasDepletionException(PowerFailure):
    pass
