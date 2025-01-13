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
        self.option = int(input())
        if self.option == 0:
            self.model = 0
            self.change_model()
        elif self.option == 1:
            self.model = 1
            self.change_model()


    def instrukcja(self):
        print("Aby obracać obraz wzdłuż osi X użyj przycisków A i D na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Y użyj przycisków W i S na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Z użyj przycisków Q i E na klawiaturze\n")

        print("Aby obracać kamerą należy przytrzyamć LPM na obiekcie i zacząć poruszać myszą.\n")
        print("Aby przybliżyć i oddalić kamerę użyj scrolla.\n")

        print("Aby móc zmienić opcję wyświetlania obrazu nalezy najpierw nacisnąc na okno konsoli tak, aby pojawił się w niej kursor")
        print("Aby zmienić wyświetlany obraz na ekranie wybierz odpowiednią opcję w kosoli wpisując w nowej lini wybrany nuemr opcji a następnie naciśnij ENTER")
        print("Po wybraniu opcji i nacisnieciu enter nalezy nacisnąć okno z wyświetlanym obrazem, aby móc ponownie obracać go przy pomocy klawiszy klawiatury")


