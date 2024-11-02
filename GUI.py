class GUI:
    model = 0
    kindOfEgg = 0
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


