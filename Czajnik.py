import numpy as np
from OpenGL.GL import *

class Czajnik:
    nodes = []

    def load(self):
        f = open("czajnik.txt", "r")
        lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            if line[0] == 'v':
                self.nodes.append([float(line[1]), float(line[2]), float(line[3])])

        f.close()

    def render(self):
        n = np.array(self.nodes)
        glBegin(GL_POINTS)
        for i in range(len(n)):
            glVertex3f(*n[i])

        glEnd()
