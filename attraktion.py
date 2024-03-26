from math import *
import numpy as np

class Attraktion:
    def __init__(self):
        self.g = 9.81
        self.maxG = self.g * 4.5
        self.minG = self.g * 1.0
        self.m = 2000
        self.cwA = 0.7
        self.d = 1.2
        self.mue = 0.0001
        self.coords = [(0,0,0)]