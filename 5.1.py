while True:
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę liczbę: "))
    if a < 0 or b < 0:
        continue
    else:
        print("Średnia to: ", (a+b)/2)