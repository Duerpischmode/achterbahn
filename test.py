import sys,pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from looping import *
from constructor import *

con = constructor([Helix()],25)
edges = []
vertices = con.doStuff()
for i in range(len(vertices)-1):
    edges.append([i,i+1])
# Define the vertices of the cube


# Define the colors for each vertex
colors = []
for i in vertices:
    colors.append((1,1,1))

# Initialize Pygame
pygame.init()
display = (1800, 1000)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up perspective projection
gluPerspective(120, (display[0] / display[1]), 0.1, 50.0)

# Set initial position and rotation angle
glTranslatef(0.0, 0.0, -5)
glRotatef(0, 0, 0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Draw the cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    # Rotate the cube
    # glRotatef(1,1,0,0)

    pygame.display.flip()
    pygame.time.wait(10)
