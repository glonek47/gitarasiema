import random
a = random.randint(0,100)
b = 0
while b != 3:
    c=int(input("Zgaduj liczbe od 1 do 100 "))
    if c > a:
        print("podałeś za dużą wartość")
        b += 1
    elif c < a:
        print("podałeś za małą wartość")
        b += 1
    else:
        print("gratulacje")
        break
else:
    print("haha przegrałeś")