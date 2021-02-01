a = int(input("podaj liczbe "))
for i in range(a):
    if i % 6 == 0 and i % 9 == 0:
        print(i)