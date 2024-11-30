import math
from OpenGL.GL import *
from OpenGL.GLU import *


class Light:
    def __init__(self, light_id):
        self.z = None
        self.y = None
        self.x = None
        self.light_position = None
        print("Tworzenie nowego źródła światła.")

        # Pobranie danych od użytkownika
        self.radius = float(input("Podaj promień (radius) w układzie sferycznym: "))
        self.azimuth = float(input("Podaj azymut (azimuth) w stopniach: "))
        self.elevation = float(input("Podaj elewację (elevation) w stopniach: "))
        self.light_angle = float(input("Podaj kąt stożka światła (light angle) w stopniach: "))

        # Ustawienie koloru światła (intensywność w RGB)
        self.light_color = [
            float(input("Podaj intensywność światła ambient (0-1) [R]: ")),
            float(input("Podaj intensywność światła ambient (0-1) [G]: ")),
            float(input("Podaj intensywność światła ambient (0-1) [B]: ")),
            1.0  # Alfa
        ]

        # Ustawienie intensywności dla komponentów światła
        self.diffuse_intensity = float(input("Podaj intensywność światła diffuse (0-1): "))
        self.specular_intensity = float(input("Podaj intensywność światła specular (0-1): "))

        self.calculate_position()
        self.light_id = light_id

    def calculate_position(self):
        # Przeliczenie pozycji w układzie sferycznym na kartezjański
        azimuth_rad = math.radians(self.azimuth)
        elevation_rad = math.radians(self.elevation)

        self.x = self.radius * math.cos(elevation_rad) * math.sin(azimuth_rad)
        self.y = self.radius * math.cos(elevation_rad) * math.cos(azimuth_rad)
        self.z = self.radius * math.sin(elevation_rad)

        # Ustawienie pozycji światła
        self.light_position = [self.x, self.y, self.z, 1.0]  # 1.0 oznacza światło reflektorowe

    def render(self):
        """
        Renderuje światło i ustawia jego parametry.
        """
        # Ustawianie parametrów światła
        glLightfv(self.light_id, GL_POSITION, self.light_position)

        # Ambient (ogólne tło oświetlenie, z mniejszą intensywnością)
        glLightfv(self.light_id, GL_AMBIENT,
                  [self.light_color[0] * 0.2, self.light_color[1] * 0.2, self.light_color[2] * 0.2, 1.0])

        # Diffuse (światło bezpośrednie, główna część światła)
        glLightfv(self.light_id, GL_DIFFUSE,
                  [self.light_color[0] * self.diffuse_intensity, self.light_color[1] * self.diffuse_intensity,
                   self.light_color[2] * self.diffuse_intensity, 1.0])

        # Specular (odblaski, wpływ na odbicia)
        glLightfv(self.light_id, GL_SPECULAR,
                  [self.light_color[0] * self.specular_intensity, self.light_color[1] * self.specular_intensity,
                   self.light_color[2] * self.specular_intensity, 1.0])

        # Kierunek świecenia
        light_direction = [-self.x, -self.y, -self.z]  # Wektor skierowany do środka (0,0,0)
        glLightfv(self.light_id, GL_SPOT_DIRECTION, light_direction)

        # Kąt stożka światła
        glLightf(self.light_id, GL_SPOT_CUTOFF, self.light_angle)

        # Tłumienie liniowe i kwadratowe (możesz dostosować do potrzeb)
        glLightf(self.light_id, GL_CONSTANT_ATTENUATION, 1.0)  # Brak tłumienia
        glLightf(self.light_id, GL_LINEAR_ATTENUATION, 0.0)  # Brak tłumienia
        glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, 0.0)  # Brak tłumienia

        # Rysowanie kuli reprezentującej pozycję światła
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)  # Przesunięcie do pozycji światła
        glColor3fv(self.light_color[:3])  # Ustawienie koloru kuli
        quadric = gluNewQuadric()
        gluSphere(quadric, 0.2, 10, 10)  # Narysowanie małej kuli
        gluDeleteQuadric(quadric)
        glPopMatrix()

