x = int(input("Podaj liczbę GB do przeliczenia"))
def gitarka():
    y = x * 1000 * 1000 * 1000
    z = y / 1024 / 1024 / 1024
    print(z)
    return
gitarka()
"""Nie do końca oszukują, tylko producenci używają systemu dziesiątkowego
gdzie 1kb to 1000 bajtów, natomiast system operacyjny używa systemu dwójkowego
w którym 1kb to 1024bajty"""