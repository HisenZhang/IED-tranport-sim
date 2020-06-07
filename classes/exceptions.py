class PowerFailure(Exception):
    pass


class PowersourceDepletion(PowerFailure):
    pass


class BatteryDepletionException(PowersourceDepletion):
    pass


class GasDepletionException(PowersourceDepletion):
    pass


class PowersourceMismatchException(PowerFailure):
    pass
