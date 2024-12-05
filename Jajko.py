import numpy as np
import random
from OpenGL.GL import *


class Jajko:
    # Parametr N określa liczbę punktów w siatce (większe N zwiększa liczbę linii) ale i bardziej obciąży komputer
    N = 5
    tab = np.array([])
    color = np.array([])

    def __init__(self):
        self.colors = None
        self.generate_nodes()
        self.compute_normals()

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
        self.tab = np.array([])
        self.color = np.array([])
        # if self.N % 2 == 0:
        #     self.N += 1

        # Tablica NxNx3 przechowująca współrzędne punktów (x, y, z)
        self.tab = np.zeros((self.N, self.N, 3))
        # Tablica NxNx3 przechowująca losowe kolory dla każdego punktu
        self.colors = np.zeros((self.N, self.N, 3))

        # Generowanie wartości u i v dla parametrów
        __u_values = np.linspace(0.0, 0.5, self.N)
        __v_values = np.linspace(0.0, 2.0, self.N+1)

        # Wypełnianie tablicy współrzędnymi dla każdego punktu (i, j)
        for i, u in enumerate(__u_values):
            for j, v in enumerate(__v_values[:-1]):
                # Równania wyznaczające współrzędne x, y, z, bazujące na równaniu piątego stopnia
                x = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.cos(np.pi * v)
                y = 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2 - 5
                z = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.sin(np.pi * v)

                self.tab[i, j] = [x, y, z]  # Przechowywanie współrzędnych punktu w tablicy
                self.colors[i, j] = [random.random(), random.random(), random.random()]  # Przypisanie losowego koloru


    # Funkcja odpowiedzialna za generowanie jajka z samych linii
    def render_line_egg(self):
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glColor3f(1.0, 1.0, 1.0)
        for j in range(self.N):
            for i in range(self.N):
                glVertex3f(*self.tab[j, i])
        glEnd()

    # Funkcja odpowiedzialna za generowanie jajka przy pomocy trójkątów
    def render_egg_with_triangles(self):
        glBegin(GL_TRIANGLES)
        for i in range(self.N):
            for j in range(self.N):
                # Pierwszy trójkąt
                glColor(1, 1, 1)
                # glColor3f(*self.colors[i,j+1])  # Ustawienie koloru na biały
                glNormal3f(*self.normals[i, (j + 1)%self.N])
                glVertex3f(*self.tab[i, (j + 1)%self.N])

                glNormal3f(*self.normals[i, j])
                glVertex3f(*self.tab[i, j])

                glNormal3f(*self.normals[(i + 1)%self.N, j])
                glVertex3f(*self.tab[(i + 1)%self.N, j])

                # Drugi trójkąt
                # glColor3f(*self.colors[i+1,j])  # Ustawienie koloru na biały
                glColor(1, 1, 1)
                glNormal3f(*self.normals[(i + 1)%self.N, j])
                glVertex3f(*self.tab[(i + 1)%self.N, j])

                glNormal3f(*self.normals[(i + 1) % self.N, (j + 1) % self.N])
                glVertex3f(*self.tab[(i + 1) % self.N, (j + 1) % self.N])

                glNormal3f(*self.normals[i, (j + 1)%self.N])
                glVertex3f(*self.tab[i, (j + 1)%self.N])

        glEnd()

    # Funkcja odpowiedzialna za generowanie jajka przy pomocy siatki trójkątów
    def render_egg_with_triangle_strip(self):
        for i in range(self.N - 1):
            glShadeModel(GL_SMOOTH)
            glBegin(GL_TRIANGLE_STRIP)  # Rozpocznij rysowanie siatki trójkątów
            for j in range(self.N):
                glColor3f(*self.colors[i][j])  # Ustaw kolor dla pierwszego wierzchołka
                glVertex3f(*self.tab[i, j])  # Pierwszy wierzchołek trójkąta
                glNormal3f(*self.normals[i, j])
                glColor3f(*self.colors[i + 1][j])  # Ustaw kolor dla drugiego wierzchołka
                glVertex3f(*self.tab[i + 1, j])  # Drugi wierzchołek trójkąta
                glNormal3f(*self.normals[(i + 1) % self.N, j])

            glEnd()  # Zakończ rysowanie siatki trójkątów
        glFlush()  # Wymuś wykonanie wszystkich komend OpenGL

    def increase_n(self):
        self.N += 1
        self.generate_nodes()
        self.compute_normals()

    def reduce_n(self):
        self.N -= 1
        self.generate_nodes()
        self.compute_normals()
