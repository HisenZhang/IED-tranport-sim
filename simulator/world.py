from simulator.model import Model
from simulator.status import GLOBAL
from classes.exceptions import DestinationReached

from datetime import timedelta


class World:

    # Define the mechanism of the world

    def __init__(self):
        self.model = Model()
        self.velocity = float()
        self.distanceTraveled = float()

        self.path = self.model.pathA
        self.vehicle = self.model.vehicle
        self.time = self.model.departDatetime
        pass

    def update(self, step):
        self.velocity = 55
        self.distanceTraveled += (self.velocity / 3600 / 1000 * step)
        self.path.update(self.distanceTraveled)
        self.vehicle.update(
            self.velocity, self.path.getIncline(), step)

        if self.distanceTraveled > self.path.getPathLength():
            raise DestinationReached

        self.time += (timedelta(milliseconds=step))
        pass

    def isDaytime(self):
        # TODO isDaytime
        pass
