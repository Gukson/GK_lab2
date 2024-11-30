from glfw.GLFW import *


def mouse_motion_callback(window, x_pos, y_pos):
    global mouse_x_pos_old, mouse_y_pos_old, angle, elevation, left_mouse_button_pressed
    if left_mouse_button_pressed:
        delta_x = x_pos - mouse_x_pos_old
        delta_y = y_pos - mouse_y_pos_old
        angle += delta_x * 0.5
        elevation += delta_y * 0.5
        elevation = max(-89.0, min(89.0, elevation))
    mouse_x_pos_old = x_pos
    mouse_y_pos_old = y_pos

def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed
    if button == GLFW_MOUSE_BUTTON_LEFT:
        left_mouse_button_pressed = (action == GLFW_PRESS)

def scroll_callback(window, x_offset, y_offset):
    global radius
    radius = max(2.0, min(50.0, radius - y_offset * 0.5))

def key_callback(window, key, scancode, action, mods):
    global rotate_x_up, rotate_x_down, rotate_y_left, rotate_y_right, rotate_z_left, rotate_z_right
    if action == GLFW_PRESS:
        if key == GLFW_KEY_W:
            rotate_x_up = True
        elif key == GLFW_KEY_S:
            rotate_x_down = True
        elif key == GLFW_KEY_A:
            rotate_y_left = True
        elif key == GLFW_KEY_D:
            rotate_y_right = True
        elif key == GLFW_KEY_Q:
            rotate_z_left = True
        elif key == GLFW_KEY_E:
            rotate_z_right = True
    elif action == GLFW_RELEASE:
        if key == GLFW_KEY_W:
            rotate_x_up = False
        elif key == GLFW_KEY_S:
            rotate_x_down = False
        elif key == GLFW_KEY_A:
            rotate_y_left = False
        elif key == GLFW_KEY_D:
            rotate_y_right = False
        elif key == GLFW_KEY_Q:
            rotate_z_left = False
        elif key == GLFW_KEY_E:
            rotate_z_right = False
