class pojazd:
    def __init__(self, marka, rocznik, typ, kolor, pojemnośćmax, pojemnośćakt, nr_tablica):
        self.marka = marka
        self.rocznik = rocznik
        self.typ = typ
        self.kolor = kolor
        self.pojemnośćmax = pojemnośćmax
        self.pojemnośćakt = pojemnośćakt
        self.nr_tablica = nr_tablica

    def ilepaliwka(self):
        print("masz {} litrów paliwa aktualnie".format(self.pojemnośćakt))
        w = input("chcesz może zatankować? (tak/nie)")
        if w == "tak" or "Tak":
            self.notowdroge()
        else:
            print("no to jedziemy dalej")

    def notowdroge(self):
        x = 4.7
        y = self.pojemnośćmax - self.pojemnośćmax
        z = x * y
        print("zatankowano",y,"litrów za",z,"zł")

    def __del__(self):
        print("juz tego nie ma byku")

class Samochod(pojazd):
    def __init__ (self, marka, rocznik, typ, kolor, pojemnośćmax, pojemnośćakt, liczba_kół, liczba_drzwi, nr_tablica):
        super().__init__(marka, rocznik, typ, kolor, pojemnośćmax, pojemnośćakt, nr_tablica)
        self.liczba_kół = liczba_kół
        self.liczba_drzwi = liczba_drzwi
    def ldrzwi(self):
        print("Twoja furka ma:", self.liczba_kół, "koła")

class Motor(pojazd):
    def __init__(self, marka, rocznik, kolor, pojemnośćmax, pojemnośćakt, liczba_kół, liczba_miejsc, nr_tablica):
        super().__init__(marka, rocznik, kolor, pojemnośćmax, pojemnośćakt, nr_tablica)
        self.liczba_kół = liczba_kół
        self.liczba_miejsc = liczba_miejsc
    def lmiejsc(self):
        print("twój motor ma:", self.liczba_miejsc, "miejsca")
ferrari = Samochod("ferrari", 2005, "kabriolet", "czerwony", 47, 25, 4, 2, "2115")
kawasaki = Motor("kawasaki", 2006, "niebieski", 25, 15, 2, 2, "2116")
ferrari.ilepaliwka()
