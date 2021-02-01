a = int(input("podaj liczbe "))
b = 1
tab = []
while b <= a:
    if a % b == 0:
        tab.append(b)
    b += 1
print(tab)
