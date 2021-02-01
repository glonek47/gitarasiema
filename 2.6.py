a = int(input("podaj 1szą liczbe "))
b = int(input("podaj 2gą liczbe "))
c = int(input("podaj 3cią liczbe "))
d = int(input("podaj 4tą liczbe "))
if a > b and a > c and a > d:
    print(a)
elif b > a and b > c and b > d:
    print(b)
elif c > a and c > b and c > d:
    print(c)
elif d > a and d > b and d > c:
    print(d)