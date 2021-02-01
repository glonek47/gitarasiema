"""kalkulator bez tej zaliczki na pit bo nie rozumiem o co z tym chodzi """
x = str(input("jaką płace chcesz obliczyć. b = brutto / n = netto "))
def bton():
    y = int(input("Podaj kwotę brutto do przeliczenia "))
    ue = y * 0.1952
    ur = y * 0.08
    uc = y * 0.0245
    uz = y * 0.09
    b = ue + ur + uc + uz
    wynik = y - b
    print(y," to jest ",wynik,"netto")
def ntob():
    y = int(input("Podaj kwotę netto do przeliczenia "))
    ue = y * 0.1952
    ur = y * 0.08
    uc = y * 0.0245
    uz = y * 0.09
    b = ue + ur + uc + uz
    wynik = y + b
    print(y, " to jest ", wynik, "brutto")
if x == "b":
    bton()
elif x == "n":
    ntob()

