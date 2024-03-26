import sys,pygame,time,numpy
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from looping import *
from helixup import *
from constructor import *

pygame.init()
screen = pygame.display.set_mode((1280,800))
refresh = False
# fps = pygame.time.Clock()
x = 5

# con = HelixUp()
con = Looping()
# con.calculate()
# cunten = []
# vektoren = con.doStuff()
# for i in range(len(vektoren)-1):
#     cunten.append([i,i+1])

for c in con.calculate():
    pygame.draw.circle(screen,(255,255,255),(100+c[0]*x,600-c[1]*x),1)
    pygame.draw.circle(screen,(255,255,255),(500+c[0]*x,600-c[2]*x),1)
    pygame.draw.circle(screen,(255,255,255),(800+c[2]*x,600-c[1]*x),1)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()