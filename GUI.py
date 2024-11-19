class GUI:
    model = 0
    kindOfEgg = 0
    def __init__(self):
        self.instrukcja()
    def change_model(self):
        print("Wybierz jaki model chcesz wyświetlić:")
        print("0. Czajnik")
        print("1. Jajko")
        self.model = int(input())
        if self.model == 0:
            self.change_model()
        else:
            self.choose_kindOfEgg()

    def choose_kindOfEgg(self):
        print("Wybierz jaki rodzaj jajka chcesz wyświrtlić:")
        print("0. Jajko stworzone z samych lini")
        print("1. Jajko stworzone z kolorowych trójkątów")
        print("2. Jajko stworzone z "'Triangle_Strip')

        self.kindOfEgg = int(input())
        self.change_model()

    def instrukcja(self):
        print("Aby obracać obraz wzdłuż osi X użyj przycisków A i D na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Y użyj przycisków W i S na klawiaturze")
        print("Aby obracać obraz wzdłuż osi Z użyj przycisków Q i E na klawiaturze\n")

        print("Aby obracać kamerą należy przytrzyamć LPM na obiekcie i zacząć poruszać myszą.\n")

        print("Aby móc zmienić opcję wyświetlania obrazu nalezy najpierw nacisnąc na okno konsoli tak, aby pojawił się w niej kursor")
        print("Aby zmienić wyświetlany obraz na ekranie wybierz odpowiednią opcję w kosoli wpisując w nowej lini wybrany nuemr opcji a następnie naciśnij ENTER")
        print("Po wybraniu opcji i nacisnieciu enter nalezy nacisnąć okno z wyświetlanym obrazem, aby móc ponownie obracać go przy pomocy klawiszy klawiatury")

    

