from classes.cargo import Cargo
from classes.engine import Engine
from classes.vehicle import Vehicle

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

    def update(self):
        if self._maxIteration != 0:
            if self._counter >= self._maxIteration:
                logging.info("Max iteration reached. Stop simulation.")
                self._stop()

        try:
            self.world.update()
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
