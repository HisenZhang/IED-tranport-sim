from simulator.model import Model
from simulator.status import GLOBAL
from classes.exceptions import DestinationReached

from datetime import timedelta
import ephem
import math


class World:

    # Define the mechanism of the world

    def __init__(self):
        self.model = Model()
        self.velocity = float()
        self.distanceTraveled = float()

        self.path = self.model.pathA
        self.vehicle = self.model.vehicle
        self.time = self.model.departDatetime

        self.sun = ephem.Sun()
        self.observer = ephem.Observer()

        self.payloadAllowed = 3510 - self.vehicle.weight
        pass

    def update(self, step):
        self.isDaytime()
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

        # decide is daytime by sun altitude
        # https://stackoverflow.com/questions/43299500/pandas-convert-datetime-timestamp-to-whether-its-day-or-night

        lastWaypoint = self.path.getWaypoint(self.path.getSegment())
        self.observer.lat = str(lastWaypoint.getLatitude())
        self.observer.lon = str(lastWaypoint.getLongtitude())
        self.observer.elevation = 0.0

        self.observer.date = self.time  # self.time.astimezone(tz=pytz.utc)
        self.sun.compute(self.observer)
        sunAltitude = self.sun.alt * 180 / math.pi
        if sunAltitude <= -6:  # civic threshold
            GLOBAL['isDayTime'] = False
            return False
        else:
            GLOBAL['isDayTime'] = True
            return True
        pass
