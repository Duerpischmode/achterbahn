import numpy as np
from math import *
class constructor:
    def _init_(self,attraktionsliste,firstSpeed = [0,25,0]):
        self.liste = attraktionsliste
        self.v = firstSpeed**2
        self.coords = [(0,0,0)]
        
        
    def doStuff(self):
        for i in self.liste:
            print(self.coords[-1])
            i.receive(self.coords[-1],self.v)
            self.coords.extend(i.calculate())
            self.v = i.getSpeed()
        return self.coords
    

x = np.array([1,0,0])
y = np.array([0,1,0])
# print(np.sin(radians(30)))