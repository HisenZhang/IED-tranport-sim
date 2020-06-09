from classes.cargo import Cargo
from classes.engine import EletricEngine, GasEngine
from classes.vehicle import Vehicle
from classes.powersource import Battery, GasTank, SolarPanel
from classes.path import Coordinate, Path


class Model:

    # This class manages world models

    def __init__(self):
        # make instances
        # power source
        self.battery = Battery(90, 1200, 1, chargingPower=600)  # kWh,lb,qty,w
        # gal,lb,qty,pound per gallon
        self.gastank = GasTank(25, 24, 1, gasWeight=6)
        # lb,w
        self.solarPanel = SolarPanel(44.5, 315)

        # TODO engine
        self.electricEngine = EletricEngine(
            'EE1', 150, [self.battery], [self.solarPanel])
        self.gasEngine = GasEngine('GE1', 449, [self.gastank])

        # TODO vehicle

        # cargo
        self.mask = Cargo('Mask', 0.525, [5.625, 5.625, 8])
        self.ventilator = Cargo('ventilator', 25, [24, 12, 24])

        # TODO path
        departure = Coordinate(32.71573611111111, -117.161086111111120)
        destination = Coordinate(42.65258055555555, -73.75623333333333)
        monument = Coordinate(36.998980555555555, -109.04518611111111)

        self.pathA = Path([departure, destination])
        self.pathB = Path([departure, monument, destination])
        self.PathC = Path()  # TODO leave blank until inclined road implementation's ready

        pass
