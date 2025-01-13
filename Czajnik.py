from OpenGL.GL import *


class Czajnik:
    def __init__(self, plik_obj):
        self.vertices = []
        self.uv_coords = []  # Dodane: Współrzędne tekstury
        self.triangles = []
        self.scale_factor = 0.3
        self.load_model(plik_obj)

    def load_model(self, plik_obj):
        with open(plik_obj, 'r') as f:
            for line in f:
                if line.startswith('v '):  # Wierzchołki
                    parts = line.strip().split()
                    vertex = tuple(map(float, parts[1:]))
                    scaled_vertex = tuple(coord * self.scale_factor for coord in vertex)
                    self.vertices.append(scaled_vertex)
                elif line.startswith('vt '):  # Współrzędne tekstury
                    parts = line.strip().split()
                    uv = tuple(map(float, parts[1:3]))  # Upewnij się, że tylko dwa elementy są wczytywane
                    self.uv_coords.append(uv)
                elif line.startswith('f '):  # Ściany
                    parts = line.strip().split()
                    indices = [tuple(map(int, part.split('/'))) for part in parts[1:]]
                    for i in range(1, len(indices) - 1):
                        self.triangles.append((indices[0], indices[i], indices[i + 1]))

    def render(self, rotate_texture=True, clockwise=True):
        glBegin(GL_TRIANGLES)
        for triangle in self.triangles:
            for vertex_data in triangle:
                vertex_index, uv_index = vertex_data[0] - 1, vertex_data[1] - 1
                if 0 <= uv_index < len(self.uv_coords):
                    u, v = self.uv_coords[uv_index]
                    if rotate_texture:
                        if clockwise:
                            u, v = 1 - v, u  # Obrót o 90 stopni w prawo
                        else:
                            u, v = v, 1 - u  # Obrót o 90 stopni w lewo
                    glTexCoord2f(u, v)
                glVertex3fv(self.vertices[vertex_index])
        glEnd()