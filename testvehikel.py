import numpy as np
from math import *

def betrag(vektor):
        return np.linalg.norm(vektor)

def getAlpha(vektor1,vektor2):
        return degrees(acos((np.dot(vektor1,vektor2)/((betrag(vektor1))*(betrag(vektor2))))))

def projAlpha(vektor,ebene):
    return vektor - (np.dot(vektor,ebene)/(betrag(ebene)**2))*ebene

x = np.array([1,2,3])
y = np.array([-11,-25,-39])
print(sin(radians(90)))
