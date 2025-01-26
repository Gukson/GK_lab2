import numpy as np
import random
from OpenGL.GL import *


class Jajko:
    # Parametr N określa liczbę punktów w siatce (większe N zwiększa liczbę linii) ale i bardziej obciąży komputer
    N = 40
    tab = np.array([])
    texture_coords = np.zeros((N, N, 2))

    def __init__(self):
        self.colors = None
        self.generate_nodes()
        self.compute_normals()
          # Współrzędne tekstury (u, v)

    def compute_normals(self):
        self.normals = np.zeros((self.N, self.N, 3))  # Tablica na normalne
        for i in range(self.N):
            for j in range(self.N):
                # Punkt na powierzchni jajka
                x, y, z = self.tab[i, j]

                # Normalizacja wektora normalnego (prosty wektor skierowany na zewnątrz)
                length = np.sqrt(x ** 2 + y ** 2 + z ** 2)
                self.normals[i, j] = [x / length, y / length, z / length]

    def generate_nodes(self):
        self.tab = np.zeros((self.N, self.N, 3))
        self.colors = np.zeros((self.N, self.N, 3))
        self.texture_coords = np.zeros((self.N, self.N, 2))

        __u_values = np.linspace(0.0, 1.0, self.N)  # U współrzędne tekstury
        __v_values = np.linspace(0.0, 1.0, self.N)  # V współrzędne tekstury

        for i, u in enumerate(__u_values):
            for j, v in enumerate(__v_values):
                x = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.cos(2 * np.pi * v)
                y = 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2 - 5
                z = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.sin(2 * np.pi * v)

                self.tab[i, j] = [x, y, z]
                self.colors[i, j] = [random.random(), random.random(), random.random()]
                self.texture_coords[i, j] = [u,v]


    # Funkcja odpowiedzialna za generowanie jajka przy pomocy trójkątów
    def render_egg_with_triangles(self):
        glBegin(GL_TRIANGLES)
        for i in range(self.N - 1):  # Iteracja po wierszach
            for j in range(self.N):  # Iteracja po kolumnach (cała siatka)
                # Pierwszy trójkąt
                glTexCoord2f(*self.texture_coords[i, j])  # Punkt 1
                glNormal3f(*self.normals[i, j])
                glVertex3f(*self.tab[i, j])

                glTexCoord2f(*self.texture_coords[(i + 1) % self.N, j])  # Punkt 2
                glNormal3f(*self.normals[(i + 1) % self.N, j])
                glVertex3f(*self.tab[(i + 1) % self.N, j])

                glTexCoord2f(*self.texture_coords[i, (j + 1) % self.N])  # Punkt 3
                glNormal3f(*self.normals[i, (j + 1) % self.N])
                glVertex3f(*self.tab[i, (j + 1) % self.N])

                # Drugi trójkąt
                glTexCoord2f(*self.texture_coords[i, (j + 1) % self.N])  # Punkt 1
                glNormal3f(*self.normals[i, (j + 1) % self.N])
                glVertex3f(*self.tab[i, (j + 1) % self.N])

                glTexCoord2f(*self.texture_coords[(i + 1) % self.N, j])  # Punkt 2
                glNormal3f(*self.normals[(i + 1) % self.N, j])
                glVertex3f(*self.tab[(i + 1) % self.N, j])

                glTexCoord2f(*self.texture_coords[(i + 1) % self.N, (j + 1) % self.N])  # Punkt 3
                glNormal3f(*self.normals[(i + 1) % self.N, (j + 1) % self.N])
                glVertex3f(*self.tab[(i + 1) % self.N, (j + 1) % self.N])
        glEnd()

    def increase_n(self):
        self.N += 1
        self.generate_nodes()
        self.compute_normals()

    def reduce_n(self):
        self.N -= 1
        self.generate_nodes()
        self.compute_normals()
