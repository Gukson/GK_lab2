import math
from OpenGL.raw.GLU import gluLookAt


class Camera:
    def __init__(self, radius=10.0, angle=0.0, elevation=0.0):
        self.radius = radius  # Odległość kamery od środka
        self.angle = angle  # Obrót wokół osi Y (azymut)
        self.elevation = elevation  # Obrót wokół osi X (elewacja)
        self.scroll_speed = 0.5  # Prędkość zmiany promienia
        self.MIN_RADIUS = 5.0  # Minimalna odległość kamery od środka
        self.centerX, self.centerY, self.centerZ = 0.0, 0.0, 0.0  # Punkt patrzenia
        self.forward = [0.0, 0.0, -1.0]  # Domyślny kierunek patrzenia
        self.up = [0.0, 1.0, 0.0]  # Domyślny wektor w górę
        self.is_moving_away_from_center = False  # Flaga kontrolująca, czy kamera oddala się od centrum

    def adjust_radius(self, scroll_offset):
        """Reguluj promień (odległość od centrum) przy pomocy scrolla."""
        self.radius += scroll_offset * self.scroll_speed
        if self.radius < self.MIN_RADIUS:  # Minimalna odległość kamery
            self.radius = self.MIN_RADIUS
            self.is_moving_away_from_center = False  # Przywróć domyślny stan, jeśli kamera dotarła do MIN_RADIUS
        elif self.radius > self.MIN_RADIUS:
            self.is_moving_away_from_center = True  # Kamera oddala się od centrum

    def update_vectors(self):
        """Zaktualizuj wektory kamery na podstawie azymutu i elewacji."""
        # Oblicz kierunek patrzenia (front vector) na podstawie współrzędnych sferycznych
        frontX = math.cos(math.radians(self.elevation)) * math.cos(math.radians(self.angle))
        frontY = math.sin(math.radians(self.elevation))
        frontZ = math.cos(math.radians(self.elevation)) * math.sin(math.radians(self.angle))
        self.forward = [frontX, frontY, frontZ]

        # Oblicz wektor "prawo" (right vector)
        rightX = -math.sin(math.radians(self.angle))
        rightY = 0.0
        rightZ = math.cos(math.radians(self.angle))
        right = [rightX, rightY, rightZ]

        # Oblicz dynamiczny wektor "w górę" (up vector) jako cross product "right" i "front"
        upX = right[1] * self.forward[2] - right[2] * self.forward[1]
        upY = right[2] * self.forward[0] - right[0] * self.forward[2]
        upZ = right[0] * self.forward[1] - right[1] * self.forward[0]
        self.up = [upX, upY, upZ]

    def get_position(self):
        """Oblicz pozycję kamery na podstawie współrzędnych sferycznych."""
        # Współrzędne sferyczne -> kartezjańskie
        x = self.radius * self.forward[0]
        y = self.radius * self.forward[1]
        z = self.radius * self.forward[2]
        return x, y, z

    def render(self):
        """Ustaw kamerę za pomocą gluLookAt."""
        # Zaktualizuj wektory przed renderowaniem
        self.update_vectors()

        # Oblicz pozycję kamery
        eyeX, eyeY, eyeZ = self.get_position()

        # Oblicz kierunek patrzenia
        directionX = self.centerX - eyeX
        directionY = self.centerY - eyeY
        directionZ = self.centerZ - eyeZ
        direction_length = math.sqrt(directionX**2 + directionY**2 + directionZ**2)

        # Przesuwaj punkt patrzenia, gdy kamera jest blisko środka
        if self.radius < self.MIN_RADIUS:
            # Normalizuj wektor kierunku
            directionX /= direction_length
            directionY /= direction_length
            directionZ /= direction_length

            # Przesuń punkt patrzenia wzdłuż tego samego kierunku
            self.centerX = eyeX + directionX * self.MIN_RADIUS
            self.centerY = eyeY + directionY * self.MIN_RADIUS
            self.centerZ = eyeZ + directionZ * self.MIN_RADIUS

        # Zresetuj punkt patrzenia do (0, 0, 0) tylko wtedy, gdy kamera się oddala
        if self.is_moving_away_from_center:
            self.centerX, self.centerY, self.centerZ = 0.0, 0.0, 0.0

        # Ustaw kamerę za pomocą gluLookAt
        gluLookAt(
            eyeX, eyeY, eyeZ,             # Pozycja oka
            self.centerX, self.centerY, self.centerZ,  # Punkt patrzenia
            self.up[0], self.up[1], self.up[2]         # Dynamiczny wektor "w górę"
        )
