from classes.cargo import Cargo
from classes.engine import EletricEngine, GasEngine
from classes.vehicle import Vehicle
from classes.powersource import Battery, GasTank, SolarPanel
from classes.path import Coordinate, Path

from datetime import datetime
import pytz


class Model:

    # This class manages world models

    def __init__(self):
        # make instances
        # power source
        self.battery = Battery(90, 60, 7.7)  # kWh,lb,kw
        # gal,lb,pound per gallon
        self.gastank = GasTank(25, 24, 6)
        # lb,w
        self.solarPanel = SolarPanel(44.5, 315)

        self.electricEngine = EletricEngine(
            'EE1', 150, [self.battery * 8], [self.solarPanel * 1])
        self.gasEngine = GasEngine('GE1', 449, [self.gastank * 9])

        self.mask = Cargo('Mask', 0.525, (5.625, 5.625, 8))
        self.ventilator = Cargo('Ventilator', 25, (24, 12, 24))

        #self.vehicle = Vehicle(4600-25-449, 1920, 536.4+396, [self.gasEngine])
        self.vehicle = Vehicle(4600-25-449, 1920, 536.4+396, [self.electricEngine])

        departure = Coordinate(32.71573611111111, -117.161086111111120)
        destination = Coordinate(42.65258055555555, -73.75623333333333)
        monument = Coordinate(36.998980555555555, -109.04518611111111)

        self.pathA = Path([departure, destination])
        self.pathB = Path([departure, monument, destination],[.1705,.0528])
        self.pathC = Path([departure, destination], [3, -3] * 22)

        self.tz_PST = pytz.timezone('America/Los_Angeles')
        self.tz_UTC = pytz.utc
        self.departDatetime = datetime(
            2020, 8, 31, 12, 00, tzinfo=self.tz_PST).astimezone(self.tz_UTC)

    pass
