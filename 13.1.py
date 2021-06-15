class Samochod:
    def __init__(self, marka, rocznik, typ, kolor, pojemność):
        self.marka = marka
        self.rocznik = rocznik
        self.typ = typ
        self.kolor = kolor
        self.pojemność = pojemność
    def zatankuj_do_pelna(self):
        print("wlasnie zatankowałeś {} litrów".format(self.pojemność))
    def cozafura(self):
        print("marka {}, rocznik {}, typ{}, kolor{}, pojemność{}".format(self.marka, self.rocznik, self.typ, self.kolor, self.pojemność))
    def prędkość(self):
        print("ale szybko jedziesz kolego swoim {}".format(self.marka))
    def prawo(self):
        print("skręcam w prawo")
    def lewo(self):
        print("skręcam w lewo")
ferrari = Samochod("Ferrari", 3, "kabriolet", "czerwony", 47)
fiat = Samochod("Fiat", 10, "kombi", "srebrny", 35)
renault = Samochod("Renault", 6, "sedan", "niebieski", 47)

ferrari.zatankuj_do_pelna()
ferrari.cozafura()
fiat.prędkość()
renault.prawo()
renault.lewo()