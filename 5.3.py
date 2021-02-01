a = list(input("podaj liczbe której kolejność chcesz obrócić "))
b = a[::-1]
if b == a:
    print("ta liczba jest palindromem")
else:
    print(b)