a = int(input("podaj pierwszą długość trójkąta "))
b = int(input("podaj drugą długość trójkąta "))
c = int(input("podaj trzecią długość trójkąta "))
if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("trójkąt jest prostokątny")
else:
    print("trójkąt nie jest prostokątny")