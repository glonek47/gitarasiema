tekst = "Magia jest w opinii niektórych ucieleśnieniem Chaosu. " \
        "Jest kluczem zdolnym otworzyć zakazane drzwi. " \
        "Drzwi, za którymi czai się koszmar, " \
        "zgroza i niewyobrażalna okropność, " \
        "za którymi czyhają wrogie, destrukcyjne siły," \
        "moce czystego zła, mogące unicestwić nie tylko tego," \
        "kto drzwi te uchyli, ale i cały świat. A ponieważ nie brakuje takich," \
        "którzy przy owych drzwiach manipulują, kiedyś ktoś popełni błąd," \
        "a wówczas zagłada świata będzie przesądzona i nieuchronna." \
        "Magia jest zatem zemstą i orężem Chaosu. " \
        "To, że po Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata. " \
        "Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się."

print(f"lower = {tekst.lower()}")
print(f"swapcase = {tekst.swapcase()}")
print(f"capitalize = {tekst.capitalize()}")
print(f"replace = {tekst.replace('j', 'w')}")
print(f"lstrip = {tekst.lstrip()}")
print(f"rstrip = {tekst.rstrip()}")
print(f"reversed = {''.join(reversed(tekst))}")
print(f"count = {tekst.count('a')}")
print(f"find = {tekst.find('ia')}")
print(f"isalnum = {tekst.isalnum()}")
print(f"startswith = {tekst.startswith('Ma')}")
print(f"endswith = {tekst.endswith('su')}")
