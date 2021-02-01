suma = 0
sr = 0
while True:
    a = int(input("podaj liczbę "))
    suma = a + suma
    sr = (a+suma)/2
    if suma > 100 or sr == 66:
        break
    else:
        continue