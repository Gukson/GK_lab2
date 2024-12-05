import Light
from OpenGL.GL import *
from OpenGL.GLU import *
class GUI:
    model = 0
    option = 0
    kindOfEgg = 0
    light_list = []
    def __init__(self):
        self.instrukcja()


    def change_model(self):
        print("Wybierz opcję:")
        print("0. Czajnik")
        print("1. Jajko")
        print("2. Światło")
        self.option = int(input())
        if self.option == 0:
            self.model = 0
            self.change_model()
        elif self.option == 1:
            self.model = 1
            self.choose_kindOfEgg()
        elif self.option == 2:
            self.light_menu()

    def choose_kindOfEgg(self):
        print("Wybierz jaki rodzaj jajka chcesz wyświrtlić:")
        print("0. Jajko stworzone z samych lini")
        print("1. Jajko stworzone z kolorowych trójkątów")
        print("2. Gładkie kolorowe jajko")

        self.kindOfEgg = int(input())
        self.change_model()

    def instrukcja(self):
        print("Aby obracać obraz wzdłuż osi X użyj przycisków A i D na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Y użyj przycisków W i S na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Z użyj przycisków Q i E na klawiaturze\n")

        print("Aby obracać kamerą należy przytrzyamć LPM na obiekcie i zacząć poruszać myszą.\n")
        print("Aby przybliżyć i oddalić kamerę użyj scrolla.\n")

        print(
            "Aby móc zmienić opcję wyświetlania obrazu nalezy najpierw nacisnąc na okno konsoli tak, aby pojawił się w niej kursor")
        print(
            "Aby zmienić wyświetlany obraz na ekranie wybierz odpowiednią opcję w kosoli wpisując w nowej lini wybrany nuemr opcji a następnie naciśnij ENTER")
        print(
            "Po wybraniu opcji i nacisnieciu enter nalezy nacisnąć okno z wyświetlanym obrazem, aby móc ponownie obracać go przy pomocy klawiszy klawiatury")

    def light_menu(self):
        for x in range(len(self.light_list)):
            print(x, ". ", self.light_list[x].light_id)
        print("9. powrót")
        i = int(input("wybor: "))
        if i == 9:
            self.change_model()
        else:
            if i >= len(self.light_list):
                print("Nie ma światla o takim indeksie")
                self.light_menu()
            self.light_option(i - 1)

    def light_option(self, x):
        print("1. kolor")
        print("2. kąt światła")
        print("3. diffuse")
        print("4. specular")
        print("5. ambient")

        i = int(input("Wybierz opcje: "))
        if i == 1:
            light_color = [
                float(input("Podaj kolor światła (0-1) [R]: ")),
                float(input("Podaj kolor światła (0-1) [G]: ")),
                float(input("Podaj kolor światła (0-1) [B]: ")),
                1.0  # Alfa
            ]
            self.light_list[x].light_color = light_color
        elif i == 2:
            light_angle = float(input("Podaj kąt stożka światła (light angle) w stopniach: "))
            self.light_list[x].light_angle = light_angle
        elif i == 3:
            diffuse_intensity = float(input("Podaj intensywność światła diffuse (0-1): "))
            self.light_list[x].diffuse_intensity = diffuse_intensity
        elif i == 4:
            specular_intensity = float(input("Podaj intensywność światła specular (0-1): "))
            self.light_list[x].specular_intensity = specular_intensity
        elif i == 5:
            ambient = float(input("Podaj ambient (0-1): "))
            self.light_list[x].ambient = ambient
        self.change_model()
