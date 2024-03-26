from math import *
import numpy as np
from attraktion import *

class Looping(Attraktion):
    def __init__(self):
        super().__init__()
        
        # Vektor der ersten Bewegung und Ebenenvektor
        self.start = np.array([1,0,0])
        self.startS = np.array([0,0,1])
        
        #Gewichtskraft und vektor
        self.fGb = self.g
        self.fG = np.array([0,-1,0]) *self.fGb
        self.fGn = np.array([1,0,0]) *self.fGb

        #Normalkraft und Vektor
        self.fNb = self.maxG
        self.fN = np.array([0,1,0])
        self.fNn = np.array([-1,0,0])
        
        #geschwindigtkeit und vektor des wagens
        self.vb = 25.0
        self.v = np.array([1,0,0]) * self.vb
        self.vn = self.fN * self.vb

        # Seitenführungsvektor -> macht den looping dreidimensional
        self.s = np.array([0,0,1])
        self.fS = np.array([0,0,1])

        #Luftwiderstands- und Reibungskraft und Vektor
        self.fRb = (0.5 * self.cwA * self.d * self.vb**2) + (self.mue * self.fNb)
        self.fR = np.array([0,0,0])
        self.fRn = np.array([0,0,0])

        #Berechnungseinheiten der Zeit
        self.t = 0.01

        # Berechnet Winkel zwischen zwei Vektoren
    def getAlpha(self,vektor1,vektor2):
        return degrees(acos((np.dot(vektor1,vektor2)/((np.linalg.norm(vektor1))*(np.linalg.norm(vektor2))))))
    
        # Gibt Seitenführungskraft abhängig vom Winkel zurück
    def getfSb(self,alpha):
        return  sin(radians(alpha/2)) * self.vb/12

        # Normalisiert einen Vektor
    def norm(self,vektor):
        return vektor/np.linalg.norm(vektor)

        # Projiziert Vektor auf vorgegebene Ebene und berechnet Winkel zum Startvektor
    def projAlpha(self,vektor,ebene):
        return vektor - (np.dot(vektor,ebene)/(np.linalg.norm(ebene)**2))*ebene
        
        # berechnet doe Normalkraft abhängig vom Winkel
    def getfN(self,delta):
        return abs(cos(radians(delta/2))) * (self.maxG-self.minG)

        # berechnet die Reibungs- und Luftwiderstandskraft
    def getfR(self):
        return (0.5 * self.cwA * self.d * np.linalg.norm(self.v)**2)/self.m + (self.mue * self.fNb)
    
    def rotVektor(self, vektor, achse, beta):
        achse = self.norm(achse)
        beta = radians(beta)

        kreuzMatrix = np.array([[0, -achse[2], achse[1]],[achse[2], 0, -achse[0]],[-achse[1], achse[0], 0]])
        rotMatrix = (cos(beta) * np.eye(3)) + ((1 - cos(beta)) * np.outer(achse, achse)) + sin(beta) * kreuzMatrix

        rotated_vector = np.dot(rotMatrix, vektor)
        return rotated_vector

        # kalkuliert alles
    def calculate(self):
        delta,alpha,beta = 0,0,0
        
        while delta <= 360:
            # Kräfte werden berechnet
            self.fS  = self.getfSb(delta) * self.s
            self.fNb = self.getfN(delta)
            self.fRb = self.getfR()
            
            # Vekoren der Kräfte werden berechnet
            self.fR  = -self.norm(self.v)  * self.fRb
            self.fRn = -self.norm(self.vn) * self.fRb
            self.fN  =  self.norm(self.vn) * self.fNb
            self.fNn = -self.norm(self.v)  * self.fNb
            
            # Änderung in der Bewegung wird berechnet
            newV = (self.fG + self.fN + self.fR)*self.t
            newVn = (self.fGn + self.fNn + self.fRn)*self.t
            achse1 = np.cross(self.v,self.vn)
            achse2 = np.cross(newV,newVn)
            print(self.getAlpha(achse1,achse2))
            self.v  += (self.fG + self.fN + self.fR)*self.t
            self.vn += (self.fGn + self.fNn + self.fRn)*self.t
            # print(self.getAlpha(self.v,self.vn))
            
            # Winkel für Bezug wird berechnet
            delta += abs(self.getAlpha(self.projAlpha(self.v,self.startS),self.start) - alpha)
            alpha =  abs(self.getAlpha(self.projAlpha(self.v,self.startS),self.start))
            
            # Neue Koordinaten werden Liste hinzugefügt
            self.coords.append(self.coords[-1] + self.v*self.t + self.fS*self.t)
        return self.coords