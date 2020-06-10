from classes.cargo import Cargo
from classes.engine import Engine
from classes.vehicle import Vehicle
from classes.exceptions import DestinationReached

from simulator.world import World

import logging


class Simulator():
    def __init__(self, step=60000, maxIteration=0):
        self._counter = 0
        self._maxIteration = maxIteration
        self._step = step
        self._clock = 0     # clock = counter * step
        self._run = True
        self.world = World()

        # logging
        LOG_FORMAT = "%(levelname)s - %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

    def update(self):
        if self._maxIteration != 0:
            if self._counter >= self._maxIteration:
                logging.warning("Max iteration reached. Stop simulation.")
                self._stop()

        try:
            self.world.update(self._step)
            logging.info("Time " + str(self._clock // 1000) +
                         " sec, Distance traveled " + str(round(self.world.distanceTraveled, 1)) + " miles.")
        except DestinationReached:
            logging.warning("Destination reached after " +
                            str(self._clock) + " cycles of simulation.")
            self._stop()
        except:
            logging.error("Exception on updating world. Stop simulation.")
            self._stop()

        self._counter += 1
        self._clock += self._step

    def isRunning(self):
        return self._run

    def getClock(self):
        return self._clock

    def _stop(self):
        self._run = False
