import main as m


def scroll_callback(window, x_offset, y_offset):
    m.radius -= y_offset * 0.5  # Zmiana promienia w zależności od scrolla
    radius = max(2.0, min(50.0, m.radius))  # Ogranicz odległość od centrum
