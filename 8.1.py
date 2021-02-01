import operator

menu = {}
counter = 0
while counter != 10:
    nazwa = input("podaj nazwe rzeczy z menu ")
    cena = int(input("podaj cene rzeczy którą wpisałeś przed chwilą"))
    menu[nazwa] = cena
    counter += 1
for nazwa, cena in menu.items():
    print(nazwa, cena)
del menu [max(menu, key=menu.get)]
del menu [min(menu, key=menu.get)]
print(menu)
nazwa = input("podaj nazwe nowej rzeczy ")
cena = input("podaj cene nowej rzeczy ")
menu[nazwa] = cena
print(menu)
