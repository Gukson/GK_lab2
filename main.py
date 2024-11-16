import sys
import threading

from OpenGL.raw.GLU import gluPerspective, gluLookAt
from glfw.GLFW import *
from OpenGL.GL import *
from Jajko import Jajko
from Czajnik import Czajnik
from GUI import GUI


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Ustaw kolor tła na czarny
    glEnable(GL_DEPTH_TEST)  # Włącz test głębokości, aby poprawnie renderować obiekty 3D


jajko = Jajko()
czajnik = Czajnik()
czajnik.load()
gui = GUI()

# Inicjalizacja zmiennych globalnych
x_angle = 0.0
y_angle = 0.0
z_angle = 0.0

# Flagi do śledzenia stanu klawiszy
rotate_x_up = False
rotate_x_down = False
rotate_y_left = False
rotate_y_right = False
rotate_z_left = False
rotate_z_right = False

viewer = [0.0, 0.0, 10.0]

theta = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
delta_x = 0

def shutdown():
    pass


def render(time):
    global theta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Wyczyść bufor koloru i bufor głębokości
    glLoadIdentity()  # Załaduj macierz jednostkową, aby zresetować bieżący stan przekształcenia

    gluLookAt(viewer[0]+theta, viewer[1], viewer[2],
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle



    glRotatef(x_angle, 1, 0, 0)  # Obróć scenę wokół osi X o kąt `x_angle`
    glRotatef(y_angle, 0, 1, 0)  # Obróć scenę wokół osi Y o kąt `y_angle`
    glRotatef(z_angle, 0, 0, 1)  # Obróć scenę wokół osi Z o kąt `z_angle`

    if gui.model == 0:
        czajnik.render()  # Renderuj model czajnika, jeśli jest wybrany
    elif gui.model == 1:
        if gui.kindOfEgg == 0:
            jajko.render_line_egg()  # Renderuj jajko za pomocą linii
        elif gui.kindOfEgg == 1:
            jajko.render_egg_with_triangles()  # Renderuj jajko za pomocą trójkątów
        elif gui.kindOfEgg == 2:
            jajko.render_egg_with_triangle_strip()  # Renderuj jajko za pomocą "triangle strip"


def key_callback(window, key, scancode, action, mods):
    global rotate_x_up, rotate_x_down
    global rotate_y_left, rotate_y_right
    global rotate_z_left, rotate_z_right

    if action == GLFW_PRESS:
        if key == GLFW_KEY_W:
            rotate_x_up = True  # Ustaw flagę na TRUE dla "W" (obrót w górę)
        elif key == GLFW_KEY_S:
            rotate_x_down = True  # Ustaw flagę na TRUE dla "S" (obrót w dół)
        elif key == GLFW_KEY_A:
            rotate_y_left = True  # Ustaw flagę na TRUE dla "A" (obrót w lewo)
        elif key == GLFW_KEY_D:
            rotate_y_right = True  # Ustaw flagę na TRUE dla "D" (obrót w prawo)
        elif key == GLFW_KEY_Q:
            rotate_z_left = True  # Ustaw flagę na TRUE dla "Q" (obrót w lewo)
        elif key == GLFW_KEY_E:
            rotate_z_right = True  # Ustaw flagę na TRUE dla "E" (obrót w prawo)

    if action == GLFW_RELEASE:
        if key == GLFW_KEY_W:
            rotate_x_up = False  # Ustaw flagę na FALSE dla "W"
        elif key == GLFW_KEY_S:
            rotate_x_down = False  # Ustaw flagę na FALSE dla "S"
        elif key == GLFW_KEY_A:
            rotate_y_left = False  # Ustaw flagę na FALSE dla "A"
        elif key == GLFW_KEY_D:
            rotate_y_right = False  # Ustaw flagę na FALSE dla "D"
        elif key == GLFW_KEY_Q:
            rotate_z_left = False  # Ustaw flagę na FALSE dla "Q"
        elif key == GLFW_KEY_E:
            rotate_z_right = False  # Ustaw flagę na FALSE dla "E"


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard_key_callback(window, key, scancode, action, mods):
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0

def main():
    global x_angle, y_angle, z_angle
    render_thread = threading.Thread(target=gui.change_model)
    render_thread.start()

    if not glfwInit():  # Inicjalizuj bibliotekę GLFW
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)  # Stwórz okno o rozmiarach 400x400
    if not window:
        glfwTerminate()  # Zakończ GLFW, jeśli okno nie zostało utworzone
        sys.exit(-1)

    glfwMakeContextCurrent(window)  # Ustaw kontekst renderowania na stworzone okno
    glfwSetFramebufferSizeCallback(window, update_viewport)  # Zarejestruj callback do zmiany rozmiaru okna
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)  # Ustaw synchronizację klatek (1 dla V-sync)

    startup()
    glfwSetKeyCallback(window, key_callback)  # Zarejestruj callback dla obsługi klawiszy

    while not glfwWindowShouldClose(window):  # Pętla główna aplikacji
        if rotate_x_up:
            x_angle += 1.0  # Zwiększ kąt obrotu wokół osi X
        if rotate_x_down:
            x_angle -= 1.0  # Zmniejsz kąt obrotu wokół osi X
        if rotate_y_left:
            y_angle -= 1.0  # Zmniejsz kąt obrotu wokół osi Y
        if rotate_y_right:
            y_angle += 1.0  # Zwiększ kąt obrotu wokół osi Y
        if rotate_z_left:
            z_angle += 1.0  # Zwiększ kąt obrotu wokół osi Z
        if rotate_z_right:
            z_angle -= 1.0  # Zmniejsz kąt obrotu wokół osi Z

        render(glfwGetTime())  # Renderuj scenę, przekazując czas jako parametr
        glfwSwapBuffers(window)  # Zamień bufory (double buffering)
        glfwPollEvents()  # Przetwórz zdarzenia systemowe, takie jak naciśnięcia klawiszy i ruch myszy
    shutdown()

    glfwTerminate()  # Zakończ działanie GLFW


if __name__ == '__main__':
    main()
