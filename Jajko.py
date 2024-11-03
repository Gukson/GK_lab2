import numpy as np
import random
from OpenGL.GL import *

class Jajko:
    # Parametr N określa liczbę punktów w siatce (większe N zwiększa liczbę linii) ale i bardziej obciąży komputer
    N = 30
    # Tablica NxNx3 przechowująca współrzędne punktów (x, y, z)
    tab = np.zeros((N, N, 3))
    # Tablica NxNx3 przechowująca losowe kolory dla każdego punktu
    colors = np.zeros((N, N, 3))

    def __init__(self):
        # Generowanie wartości u i v dla parametrów
        __u_values = np.linspace(0.0, 1.0, self.N)
        __v_values = np.linspace(0.0, 1.0, self.N)

        # Wypełnianie tablicy współrzędnymi dla każdego punktu (i, j)
        for i, u in enumerate(__u_values):
            for j, v in enumerate(__v_values):
                # Równania wyznaczające współrzędne x, y, z, bazujące na równaniu piątego stopnia
                x = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.cos(np.pi * v)
                y = 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2 - 5
                z = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.sin(np.pi * v)
                self.tab[i, j] = [x, y, z]  # Przechowywanie współrzędnych punktu w tablicy
                self.colors[i, j] = [random.random(), random.random(), random.random()]  # Przypisanie losowego koloru

    # Funkcja odpowiedzialna za generowanie jajka z samych linii
    def render_line_egg(self):
        glBegin(GL_LINES)  # Rozpocznij rysowanie linii
        for i in range(Jajko.N - 1):
            for j in range(self.N - 1):
                # Rysowanie linii poziomych
                glVertex3f(*self.tab[i, j])  # Początek linii
                glVertex3f(*self.tab[i + 1, j])  # Koniec linii

                # Rysowanie linii pionowych
                glVertex3f(*self.tab[i, j])  # Początek linii
                glVertex3f(*self.tab[i, j + 1])  # Koniec linii
        glEnd()  # Zakończ rysowanie linii

    # Funkcja odpowiedzialna za generowanie jajka przy pomocy trójkątów
    def render_egg_with_triangles(self):
        glBegin(GL_TRIANGLES)  # Rozpocznij rysowanie trójkątów
        for i in range(self.N - 1):
            for j in range(self.N - 1):
                glColor3f(*self.colors[i, j])  # Ustaw kolor dla pierwszego trójkąta
                glVertex3f(*self.tab[i, j + 1])  # Pierwszy wierzchołek trójkąta
                glVertex3f(*self.tab[i, j])  # Drugi wierzchołek trójkąta
                glVertex3f(*self.tab[i + 1, j])  # Trzeci wierzchołek trójkąta

                glColor3f(*self.colors[i + 1, j + 1])  # Ustaw kolor dla kolejnego trójkąta
                glVertex3f(*self.tab[i, j + 1])  # Pierwszy wierzchołek drugiego trójkąta
                glVertex3f(*self.tab[i + 1, j + 1])  # Drugi wierzchołek
                glVertex3f(*self.tab[i + 1, j])  # Trzeci wierzchołek
        glEnd()  # Zakończ rysowanie trójkątów

    # Funkcja odpowiedzialna za generowanie jajka przy pomocy siatki trójkątów
    def render_egg_with_triangle_strip(self):
        for i in range(self.N - 1):
            glBegin(GL_TRIANGLE_STRIP)  # Rozpocznij rysowanie siatki trójkątów
            for j in range(self.N):
                glColor3f(*self.colors[i][j])  # Ustaw kolor dla pierwszego wierzchołka
                glVertex3f(*self.tab[i, j])  # Pierwszy wierzchołek trójkąta
                glColor3f(*self.colors[i + 1][j])  # Ustaw kolor dla drugiego wierzchołka
                glVertex3f(*self.tab[i + 1, j])  # Drugi wierzchołek trójkąta
            glEnd()  # Zakończ rysowanie siatki trójkątów
        glFlush()  # Wymuś wykonanie wszystkich komend OpenGL
