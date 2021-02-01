def cnaf():
    x = int(input("podaj temperature w stopniach celsjusza "))
    y = x * 1.8 + 32
    if y >= 212:
        print("woda wrze, ma ",round(y, 1)," stopni")
    elif y <= 32:
        print("woda zamarza, ma",round(y, 1)," stopni")
    else:
        print("woda ma ",round(y, 1),"stopni fahrenheita")
cnaf()
def knaf():
    x = int(input("podaj temperature w stopniach Kelwina "))
    y = x * 1.8 - 459.67
    print(x," to ",y," stopni Fahrenhaita")
def fnak():
    x = int(input("podaj temperature w stopniach Fahrenheita "))
    z = 5/9
    y = (x +459.67) * z
    print(x, " to ", y, " stopni Kelwina")
def knac():
    x = int(input("podaj temperature w stopniach Kelwina "))
    y = x - 273.15
    print(x, " to ", y, " stopni Celsjusza")
def cnak():
    x = int(input("podaj temperature w stopniach Celsjusza "))
    y = x + 273.15
    print(x, " to ", y, " stopni Kelwina")
