class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def printgatunek(self):
        print("Tutaj:" + self.gatunek)

class kot(Zwierze):
    def miaucze(self):
        print("miaucze")

class pies(Zwierze):
    def szczekam(self):
        print("szczekam")

class ptak(Zwierze):
    def latam(self):
        print("latam")

class ryba(Zwierze):
    def oddycham(self):
        print("oddycham pod wodą")

kot1 = kot("kot")
pies1 = pies("pies")
ptak1 = ptak("ptak")
ryba1 = ryba("ryba")
kot1.miaucze()
pies1.szczekam()
ptak1.latam()
ryba1.oddycham()