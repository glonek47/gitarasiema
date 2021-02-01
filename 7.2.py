import random
k = [random.randrange(0,10, 1) for i in range(100)]
x = tuple(k)
parzyste = []
nieparzyste = []
print(x)
print(x.count(0))
print(x.count(1))
print(x.count(2))
for i in x:
    if i % 2 == 0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)
print("parzyste: ", parzyste)
print("liczba parzysta występuje", len(parzyste), "razy")
print("nieparzyste: ", nieparzyste)
print("liczba nieparzysta występuje", len(nieparzyste), "razy")