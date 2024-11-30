import math
from OpenGL.GL import *
from OpenGL.raw.GLU import gluPerspective, gluLookAt
from Axes import draw_axes
from Czajnik import Czajnik
from Jajko import Jajko

czajnik = Czajnik()
jajko = Jajko()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    czajnik.load()

def shutdown():
    pass

def render(time, gui, x_angle, y_angle, z_angle, rotate_x_up, rotate_x_down, rotate_y_left, rotate_y_right, rotate_z_left, rotate_z_right):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position
    radius = 10.0
    angle = 0.0
    elevation = 0.0
    cx, cy, cz = 0.0, 0.0, 0.0
    eyeX = cx + radius * math.cos(math.radians(elevation)) * math.cos(math.radians(angle))
    eyeY = cy + radius * math.sin(math.radians(elevation))
    eyeZ = cz + radius * math.cos(math.radians(elevation)) * math.sin(math.radians(angle))

    gluLookAt(eyeX, eyeY, eyeZ, cx, cy, cz, 0.0, 1.0, 0.0)
    draw_axes()

    glRotatef(x_angle, 1, 0, 0)
    glRotatef(y_angle, 0, 1, 0)
    glRotatef(z_angle, 0, 0, 1)

    if gui.model == 0:
        czajnik.render()
    elif gui.model == 1:
        if gui.kindOfEgg == 0:
            jajko.render_line_egg()
        elif gui.kindOfEgg == 1:
            jajko.render_egg_with_triangles()
        elif gui.kindOfEgg == 2:
            jajko.render_egg_with_triangle_strip()

def update_viewport(window, width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
