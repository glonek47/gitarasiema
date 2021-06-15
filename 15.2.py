class Beer:
    def __init__(self, nazwa, procenty, cena):
        self.nazwa = nazwa
        self.procenty = procenty
        self.cena = cena

    def print(self):
        print("\n" + self.nazwa)

    def procent(self):
        print("Piwko ma " + str(self.procenty) + "%")
        print("Kosztuje " + str(self.cena) + " zł")
        if (self.procenty >=5):
            print("Ma dużo %, więc jest pysznym piwkiem")
        else:
            print("Ma mało %, więc, jak ty możesz to pić")

    def info(self):
        if (self.cena >=5) and (self.procenty < 5):
            print("I jeszcze jakie drogie")
        elif (self.cena >=5) and (self.procenty >= 5):
            print("Ale dużo kosztuje, więc jak ci nie szkoda pieniędzy to smacznego")
        elif (self.cena <5) and (self.procenty >= 5):
            print("I do tego w jakiej cenie!!!")
        elif (self.cena <5) and (self.procenty < 5):
            print("Ale chociaż tanie")

def Main():
    print("Witaj!")
    Piwko(Beer)
    while True:
        choice = input("\nCzy chcesz zobaczyć jeszcze jakies piwo? tak / nie ")
        if choice == "tak":
            Piwko(Beer)
        else:
            print("\nTo na razie!")
            break

def Piwko(Beer):
    wybor = input("\nKtóre piwo wybierasz? Perła Export(1), Tatra(2), Somersby(3), harnaś(4) ")
    if wybor == "1":
        piwo1.print()
        piwo1.procent()
        piwo1.info()
    if wybor == "2":
        piwo2.print()
        piwo2.procent()
        piwo2.info()
    if wybor == "3":
        piwo3.print()
        piwo3.procent()
        piwo3.info()
    if wybor == "4":
        piwo4.print()
        piwo4.procent()
        piwo4.info()

piwo1 = Beer("Perła Export", 6, 10)
piwo2 = Beer("Tatra", 6, 8)
piwo3 = Beer("Somersby", 4, 6)
piwo4 = Beer("harnaś", 6, 12)

Main()