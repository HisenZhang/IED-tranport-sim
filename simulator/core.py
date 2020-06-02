from classes.cargo import Cargo
from classes.engine import Engine
from classes.vehicle import Vehicle

from simulator.world import World

class Simulator():
    def __init__(self,step=60000):
        self._counter = 0
        self._step = step
        self._clock = 0     # clock = counter * step
        # self._isDaytime = True
        self._run = True
        self.world = World()      
    
    def update(self):
        self._counter += 1
        self._clock += self._step
        # TODO isDaytime
        # TODO setup

    def isRunning(self):
        return self._run

    def getClock(self):
        return self._clock

    def _stop(self):
        self._run = False