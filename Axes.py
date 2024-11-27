from OpenGL.GL import *

def draw_axes():
    glBegin(GL_LINES)

    # Oś X (czerwona)
    glColor3f(5.0, 0.0, 0.0)  # Czerwony
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    # Oś Y (zielona)
    glColor3f(0.0, 5.0, 0.0)  # Zielony
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    # Oś Z (niebieska)
    glColor3f(0.0, 0.0, 5.0)  # Niebieski
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()
