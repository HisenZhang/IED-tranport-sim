from classes.cargo import Cargo
from classes.engine import EletricEngine,GasEngine
from classes.vehicle import Vehicle
from classes.powersource import Battery,GasTank


class Model:

    # This class manages world models

    def __init__(self):
        # make instances
        # power source
        self.battery = Battery(90,1200,1,chargingPower=600) #kWh,lb,qty,w
        self.gastank = GasTank(25,24,1,gasWeight=6) #gal,lb,qty,pound per gallon

        # TODO engine

        # TODO vehicle

        # cargo
        self.mask = Cargo('Mask',0.525,[5.625,5.625,8],1)
        self.ventilator = Cargo('ventilator',25,[24,12,24],1) 

        # TODO path

        pass
