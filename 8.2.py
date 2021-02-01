slownik = {}
counter = 0
liczbaPodjesc = 10
while counter != liczbaPodjesc:
    nazwa = input("podaj nazwe gostka ")
    numer = int(input("podaj numer gostka "))
    slownik[nazwa] = numer
    counter += 1
nowa_nazwa1 = input("podaj nową nazwe dla 1szego gostka ")
nowa_nazwa_1 = input("podaj nową nazwe dla ostatniego gostka ")
nowy_slownik = {}
counter = 0
while counter != liczbaPodjesc:
    print(counter)
    if counter == 0:
        #print("pierwszy if")
        nowy_slownik[nowa_nazwa1] = list(slownik.values())[counter]
    elif counter == liczbaPodjesc-1:
        #print("drugi if")
        nowy_slownik[nowa_nazwa_1] = list(slownik.values())[counter]
    else:
        #print("else")
        nowy_slownik[list(slownik.keys())[counter]] = list(slownik.values())[counter]
    counter += 1


print(nowy_slownik)
del nowy_slownik[list(nowy_slownik.keys())[4]]
del nowy_slownik[list(nowy_slownik.keys())[5]]
print(nowy_slownik)
nowy_slownik.clear()
counter = 0
while counter != 2:
    nazwa = input("podaj nazwe gostka ")
    numer = int(input("podaj numer gostka "))
    nowy_slownik[nazwa] = numer
    counter += 1
print(nowy_slownik)
lista = list(nowy_slownik.items())
print(lista)
lista.sort()
print(lista)
#sortuje po kluczu elementów