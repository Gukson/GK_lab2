import sys
import threading

from OpenGL.raw.GLU import gluPerspective, gluLookAt
from PIL import Image
from glfw.GLFW import *

from Jajko import Jajko
from Czajnik import Czajnik
from GUI import GUI
from Axes import *
from Camera import Camera


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Ustaw kolor tła na czarny
    glEnable(GL_DEPTH_TEST)  # Włącz test głębokości, aby poprawnie renderować obiekty 3D


jajko = Jajko()
czajnik = Czajnik("teapot.obj")

camera = Camera()
light_mode = False
# light_number = 1
gui = GUI()

# Inicjalizacja zmiennych globalnych
x_angle = 0.0
y_angle = 0.0
z_angle = 0.0
rotate_x_up = False
rotate_x_down = False
rotate_y_left = False
rotate_y_right = False
rotate_z_left = False
rotate_z_right = False
n_up = False
n_down = False
change_light = False
texture = 1
change_texture = False

def shutdown():
    pass

# Mysz
mouse_x_pos_old = 0
mouse_y_pos_old = 0
left_mouse_button_pressed = False

def render(time):
    global angle, elevation, radius
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Wyczyść bufor koloru i bufor głębokości
    glLoadIdentity()  # Załaduj macierz jednostkową, aby zresetować bieżący stan przekształcenia

    camera.render()
    draw_axes()


    glRotatef(x_angle, 1, 0, 0)  # Obróć obiekt wokół osi X o kąt `x_angle`
    glRotatef(y_angle, 0, 1, 0)  # Obróć obiekt wokół osi Y o kąt `y_angle`
    glRotatef(z_angle, 0, 0, 1)  # Obróć obiekt wokół osi Z o kąt `z_angle`

    if gui.model == 0:
        czajnik.render()  # Renderuj model czajnika, jeśli jest wybrany
    elif gui.model == 1:
        jajko.render_egg_with_triangles()  # Renderuj jajko za pomocą trójkątów

def mouse_motion_callback(window, x_pos, y_pos):
    global mouse_x_pos_old, mouse_y_pos_old
    global angle, elevation
    global left_mouse_button_pressed

    if left_mouse_button_pressed:  # Obracaj kamerę tylko, gdy lewy przycisk myszy jest wciśnięty
        delta_x = x_pos - mouse_x_pos_old
        delta_y = y_pos - mouse_y_pos_old

        angle += delta_x * 0.5  # Obrót w poziomie (wokół osi Y)
        elevation += delta_y * 0.5  # Obrót w pionie (wokół osi X)

        elevation = max(-89.0, min(89.0, elevation))  # Ogranicz kąt pionowy, aby uniknąć problemów z "flipem"

    mouse_x_pos_old = x_pos
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT:
        if action == GLFW_PRESS:
            left_mouse_button_pressed = True
        elif action == GLFW_RELEASE:
            left_mouse_button_pressed = False


def scroll_callback(window, x_offset, y_offset):
    global radius
    radius -= y_offset * 0.5  # Zmiana promienia w zależności od scrolla
    radius = max(2.0, min(50.0, radius))  # Ogranicz odległość od centrum



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


def mouse_motion_callback(window, x_pos, y_pos):
    global mouse_x_pos_old, mouse_y_pos_old
    global angle, elevation
    global left_mouse_button_pressed

    if left_mouse_button_pressed:  # Obracaj kamerę tylko, gdy lewy przycisk myszy jest wciśnięty
        delta_x = x_pos - mouse_x_pos_old
        delta_y = y_pos - mouse_y_pos_old


        camera.angle += delta_x * 0.5  # Obrót w poziomie (wokół osi Y)
        camera.elevation += delta_y * 0.5  # Obrót w pionie (wokół osi X)


    mouse_x_pos_old = x_pos
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT:
        if action == GLFW_PRESS:
            left_mouse_button_pressed = True
        elif action == GLFW_RELEASE:
            left_mouse_button_pressed = False


def scroll_callback(window, x_offset, y_offset):
    camera.radius -= y_offset * 0.5  # Zmiana promienia w zależności od scrolla


def key_callback(window, key, scancode, action, mods):
    global rotate_x_up, rotate_x_down
    global rotate_y_left, rotate_y_right
    global rotate_z_left, rotate_z_right
    global n_up, n_down
    global change_light, light_number, change_texture, texture

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
        elif key == GLFW_KEY_1:
            texture = 1
            change_texture = True
        elif key == GLFW_KEY_2:
            texture = 2
            change_texture = True
        elif key == GLFW_KEY_3:
            texture = 3
            change_texture = True



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



def main():
    global x_angle, y_angle, z_angle, n_up, n_down, change_light, light_mode, gui, light_number, change_texture
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
    glfwSetCursorPosCallback(window, mouse_motion_callback)  #zarejestruj pozycję kursora
    glfwSetMouseButtonCallback(window, mouse_button_callback)  #zarejestruj kliknięcie myszki
    glfwSetScrollCallback(window, scroll_callback)  # Obsługa scrolla myszy
    glfwSetKeyCallback(window, key_callback)  # Zarejestruj callback dla obsługi klawiszy
    glfwSwapInterval(1)  # Ustaw synchronizację klatek (1 dla V-sync)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_CULL_FACE)

    image = Image.open("P6_t.tga").convert("RGB")
    rotated_image = image.rotate(0, expand=True)
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB, rotated_image.size[0], rotated_image.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, rotated_image.tobytes("raw", "RGB", 0, -1)
    )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glDisable(GL_LIGHTING)

    startup()

    while not glfwWindowShouldClose(window):  # Pętla główna aplikacji
        if change_texture:
            if texture == 1:
                image = Image.open("D2_t.tga").convert("RGB")
            elif texture == 2:
                image = Image.open("P4_t.tga").convert("RGB")
            else:
                image = Image.open("P6_t.tga").convert("RGB")
            rotated_image = image.rotate(90, expand=True)
            glTexImage2D(
                GL_TEXTURE_2D, 0, GL_RGB, rotated_image.size[0], rotated_image.size[1], 0,
                GL_RGB, GL_UNSIGNED_BYTE, rotated_image.tobytes("raw", "RGB", 0, -1)
            )
            change_texture = False
        # Obracanie obiektu na podstawie wciśniętych klawiszy
        if rotate_x_up:
            if light_mode:
                gui.light_list[light_number-1].elevation += 1
                gui.light_list[light_number - 1].calculate_position()
            else:
                x_angle += 1.0  # Zwiększ kąt obrotu wokół osi X
        if rotate_x_down:
            if light_mode:
                gui.light_list[light_number - 1].elevation -= 1
                gui.light_list[light_number - 1].calculate_position()
            else:
                x_angle -= 1.0  # Zwiększ kąt obrotu wokół osi X
        if rotate_y_left:
            if light_mode:
                gui.light_list[light_number - 1].azimuth -= 1
                gui.light_list[light_number - 1].calculate_position()
            else:
                y_angle -= 1.0  # Zwiększ kąt obrotu wokół osi X
        if rotate_y_right:
            if light_mode:
                gui.light_list[light_number - 1].azimuth += 1
                gui.light_list[light_number - 1].calculate_position()
            else:
                y_angle += 1.0  # Zwiększ kąt obrotu wokół osi X
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
