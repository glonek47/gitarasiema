from pytanka import pytanka

zadania = [
    "czym jest RAM\n(a) pamięcią do zapisu i odczytu\n(b) zasilaczem awaryjnym\n(c) kartą sieciową\n\n",
    "Jak nazywa się szeregowe łącze do którego można podłączyć urządzenia do komputera\n(a) GPT\n(b) USB\n(c) C++\n(d) gif\n\n",
    "transmisję w zakresie podczerwieni zapewnia\n(a) LAN\n(b) IrDa\n(c) USB\n(d) Karta sieciowa\n\n",
    "jeden kilobajt to\n(a) 1024 bajty\n(b) 1024 bity \n(c) 1000 bajtów\n(d) 1024 bajty\n\n",
    "jak nazywa się prawo do korzystania z oprogramowania\n(a) autoryzacja\n(b) licencja\n(c) prawo autorskie\n\n",
    "oprogramowanie dostępne za darmo, bez żadnych opłat licencyjnych to\n(a) shareware\n(b) freeware\n(c) adware\n(d) trial\n\n",
    "czego nie może zawierać folder\n(a) plików\n(b) folderów\n(c) ścieżek dostępu\n(d) zdjęć\n\n",
    "notatnik to\n(a) edytor prostych tekstów\n(b) folder systemowy\n(c) program do nagrywania głosu\n\n",
    "w jakim języku zrobiony jest ten test\n(a) HTML\n(b) Python\n(c) CSS\n(d) C#\n\n",
    "które z wymienionych urządzeń nie jest urządzeniem wyjściowym\n(a) Monitor\n(b) Głośnik\n(c) drukarka\n(d) myszka\n\n",
]

pytania = [
    pytanka(zadania[0], "a"),
    pytanka(zadania[1], "b"),
    pytanka(zadania[2], "b"),
    pytanka(zadania[3], "a"),
    pytanka(zadania[4], "b"),
    pytanka(zadania[5], "b"),
    pytanka(zadania[6], "c"),
    pytanka(zadania[7], "a"),
    pytanka(zadania[8], "b"),
    pytanka(zadania[9], "d")
]
def test(pytania):
    x = 0
    for pytanka in pytania:
        odp = input(pytanka.pytanie)
        if odp == pytanka.odp:
            x += 1
    if x < 3:
        print("nie zdałeś testu, miałeś ",x,"punktów na ",len(pytania),"możliwych")
    elif x >= 3 and x < 5:
        print("masz ",x,"punktów na",len(pytania),"możliwych, co przekłada się na ocene dopuszczającą")
    elif x >= 5 and x < 7:
        print("masz ",x, "punktów na", len(pytania),"możliwych, co przekłada się na ocene dostateczną")
    elif x >= 7 and x < 9:
        print("masz ",x, "punktów na", len(pytania),"możliwych, co przekłada się na ocene dobrą")
    elif x == 9:
        print("masz ", x, "punktów na", len(pytania), "możliwych, co przekłada się na ocene bardzo dobrą")
    elif x == 10:
        print("gratuluje, masz ocene celującą")
test(pytania)