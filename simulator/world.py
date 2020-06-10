from simulator.model import Model
from simulator.status import GLOBAL
from classes.exceptions import DestinationReached

class World:

    # Define the mechanism of the world

    def __init__(self):
        self.model = Model()
        self.velocity = float()
        self.distanceTraveled = float()
        pass

    def update(self, step):
        self.velocity = 55
        self.model.vehicle.update(self.velocity, step)
        self.distanceTraveled += (self.velocity / 3600 / 1000 * step)
        if self.distanceTraveled > self.model.pathA.getPathLength():
            raise DestinationReached
        pass

    def isDaytime(self):
        # TODO isDaytime
        pass
