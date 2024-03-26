from attraktion import *
from math import *
import numpy as np

class HelixUp(Attraktion):
    def __init__(self):
        super().__init__()
        
        # Vektor der ersten Bewegung und Ebenenvektor
        self.start = np.array([1,0,0])
        self.startS = np.array([0,1,0])
        
        # Gewichtskraft und vektor
        self.fGb = self.g
        self.fG = np.array([0,-1,0]) *self.fGb
        self.fGn = np.array([0,0,-1]) *self.fGb

        # Normalkraft und Vektor
        self.fNb = self.maxG
        self.fN = np.array([0,0,1])
        self.fNn = np.array([-1,0,0])
        
        # Geschwindigtkeit und vektor des wagens
        self.vb = 25.0
        self.v = np.array([1,0,0]) * self.vb
        self.vn = self.fN * self.vb

        # Seitenführungsvektor -> macht den looping dreidimensional
        self.s = np.array([1,0,0])
        self.fS = np.array([1,0,0])

        # Luftwiderstands- und Reibungskraft und Vektor
        self.fRb = (0.5 * self.cwA * self.d * self.betrag(self.v**2))/self.m + (self.mue * self.fNb)
        self.fR = np.array([0,0,0])
        self.fRn = np.array([0,0,0])

        # Berechnungseinheiten der Zeit
        self.t = 0.01

        # gibt den Betrag eines Vektors zurück
    def betrag(self,vektor):
        return np.linalg.norm(vektor)
    
        # Berechnet Winkel zwischen zwei Vektoren
    def getAlpha(self,vektor1,vektor2):
        return degrees(acos((np.dot(vektor1,vektor2)/((self.betrag(vektor1))*(self.betrag(vektor2))))))
    
        # Gibt Seitenführungskraft abhängig vom Winkel zurück
    def getfSb(self,alpha):
        return  sin(radians(alpha/2)) * self.vb/12

        # Normalisiert einen Vektor
    def norm(self,vektor):
        return vektor/self.betrag(vektor)

        # Projiziert Vektor auf vorgegebene Ebene und berechnet Winkel zum Startvektor
    def projAlpha(self,vektor,ebene):
        return vektor - (np.dot(vektor,ebene)/(self.betrag(ebene)**2))*ebene
    
        # berechnet doe Normalkraft abhängig vom Winkel
    def getfN(self):
        return self.maxG

        # berechnet die Reibungs- und Luftwiderstandskraft
    def getfR(self):
        return (0.5 * self.cwA * self.d * self.betrag(self.v)**2)/self.m + (self.mue * self.fNb)
    
    def getBeta(self,vektor):
        return np.around(cos(radians(self.getAlpha(vektor,self.startS))),decimals=8)

        # kalkuliert alles
    def calculate(self):
        delta,alpha = 0,0
        
        while delta <= 720:
            # Kräfte werden berechnet
            self.fS  = self.getfSb(delta) * self.s
            self.fNb = self.getfN()
            self.fRb = self.getfR()
            
            # Vekoren der Kräfte werden berechnet
            self.fR  = -self.norm(self.v)  * self.fRb
            self.fRn = -self.norm(self.vn) * self.fRb
            self.fN  =  self.norm(self.vn) * self.fNb
            self.fNn = -self.norm(self.v)  * self.fNb * self.getBeta(self.fN)
            self.fGn =  self.norm(self.v)  * self.fGb * self.getBeta(self.fN)

            # Änderung in der Bewegung wird berechnet
            print(self.getAlpha((((self.fG + self.fN + self.fR ))*self.t),(((self.fGn + self.fNn + self.fRn))*self.t)))
            self.v  += (self.fG*0 + self.fN + self.fR)*self.t
            self.vn += (self.fGn*0 + self.fNn + self.fRn)*self.t
            # print(np.around(self.getAlpha(self.v,self.vn),decimals=2))

            # Winkel für Bezug wird berechnet
            delta += abs(self.getAlpha(self.projAlpha(self.v,self.startS),self.start) - alpha)
            alpha =  abs(self.getAlpha(self.projAlpha(self.v,self.startS),self.start))
            
            # Neue Koordinaten werden Liste hinzugefügt
            self.coords.append(self.coords[-1] + self.v*self.t + self.fS*self.t)
        return self.coords