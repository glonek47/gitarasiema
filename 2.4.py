a = int(input("podaj liczbe "))
if a < 0 and a % 2 == 0:
    print("liczba jest ujemna i podzielna przez 2")
elif a < 0 and a % 2 == 1:
    print("liczba jest ujemna i niepodzielna przez 2")
elif a > 0 and a % 2 == 0:
    print("liczba jest dodatnia i podzielna przez 2")
elif a > 0 and a % 2 == 1:
    print("liczba jest dodatnia i niepodzielna przez 2")