import random
teams = ["FC Katowice", "Brda Bydgoszcz", "Cisy Nałęczów","Czarni Sosnowiec", "Gol Częstochowa", "Kolejarz Łódź",
         "Medyk Konin","Olimpia Szczecin","Zamłynie Radom", "Kłos Moskorzyn", "Zagłębie Lubin","Kalina Sobin","KS Polkowice",
         "Chrobry Głogów", "FC Legnica", "Legia Warszawa", "Cracovia Kraków", "Pogoń Szczeciń", "Lech Poznań"]

a1 = set([])
a2 = set([])
a3 = set([])
a4 = set([])
a1.add("FC Legnica")
while len(a1) != random.randint(10,20):
    a1.add(random.choice(teams))
while len(a2) != random.randint(10, 20):
    a2.add(random.choice(teams))
while len(a3) != random.randint(10, 20):
    a3.add(random.choice(teams))
while len(a4) != random.randint(10, 20):
    a4.add(random.choice(teams))
print(a1)
print(a2)
print(a3)
print(a4)
a1.remove("FC Legnica")
print(a1)
print(a1 >= a2)
a1.add("FC Legnica")
lista_z_a1 = list(a1)
lista_z_a1.append("FC Legnica")
#po przekonwertowaniu na liste mogą być duplikaty
print(lista_z_a1)
