from classes.exceptions import BatteryDepletionException, GasDepletionException

class PowerSource():
    def __init__(self,capacity,weight,qty):
        self.quantity = qty
        self.weight = weight * qty
        self.capacity = capacity * qty
        self.remaining = capacity * qty
        pass


class Battery(PowerSource):
    # battery weight includes solar panel
    def __init__(self, *args,chargingPower):
        super(Battery, *args, self).__init__()
        self.isCharging = False
        self.chargingPower = chargingPower
        pass

    def chargeUp(self,charingTime): 
        # charingTime = step 
        if (self.remaining + self.chargingPower * charingTime) > self.capacity:
            self.remaining = self.capacity
        else:
            self.remaining += (self.chargingPower * charingTime)

    def comsume(self,outputPower,comsumingTime):
        # comsumingTime = step 
        if self.remaining > (outputPower * comsumingTime):
            self.remaining -= (outputPower * comsumingTime)
        else:
            raise BatteryDepletionException

class GasTank(PowerSource):
    # gasWeight: pound per gallon
    def __init__(self, *args, gasWeight):
        super(GasTank, *args, self).__init__()
        self.weight += gasWeight * self.capacity
        pass 

    def comsume(self,outputPower,comsumingTime):
        # comsumingTime = step 
        if self.remaining > (outputPower * comsumingTime):
            self.remaining -= (outputPower * comsumingTime)
        else:
            raise GasDepletionException
