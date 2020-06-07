class PowerFailure(Exception):
    pass


class PowerSourceDepletion(PowerFailure):
    pass


class BatteryDepletionException(PowerSourceDepletion):
    pass


class GasDepletionException(PowerSourceDepletion):
    pass


class PowerSourceMismatchException(PowerFailure):
    pass
