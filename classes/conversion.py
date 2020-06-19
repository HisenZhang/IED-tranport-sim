from classes.exceptions import ConversionFailure


def MPHtoMPG_Gas(speed):
    return 18  # TODO MPG as a function of speed in mph

def MPHtoMPG_Electric(speed):
    return 65

def MPGtoMPKWh(mpg):
    return 0.029669 * mpg # 1/33.705