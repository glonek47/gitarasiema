import math
a = int(input("podaj współczynnik stojący przy x2 "))
b = int(input("podaj współczynnik stojący przy x "))
c = int(input("podaj współczynnik c "))
delta = (b*b) - (4 * a * c)
print(math.sqrt(delta))
if delta < 0:
    print("równanie nie ma wyniku")
elif delta == 0:
    print("x jest równy ",-b/(2*a))
else:
    x1 = (-b - math.sqrt(delta)) / (a * 2)
    x2 = (-b + math.sqrt(delta)) / (a * 2)
    print("x1 jest równy ",x1)
    print("x2 jest równy ",x2)
