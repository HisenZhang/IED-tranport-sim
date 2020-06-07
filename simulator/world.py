from simulator.model import Model
from simulator.status import Status

class World:
    
    # Define the mechanism of the world
    
    def __init__(self):
        self.model = Model()
        self.status = Status()        
        pass

    def update(self):
        # TODO World update
        pass

    def isDaytime(self):
        # TODO isDaytime
        pass
