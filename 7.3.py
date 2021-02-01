import random
parz = [random.randrange(0,100, 2) for i in range(100)]
nieparz = [random.randrange(1,100, 2) for i in range(100)]
x = tuple(parz)
y = tuple(nieparz)
print("miejsce w pamięci przed konkatenacją ",id(x), id(y))
xy = x + y
print(xy)
print(id(xy))
print(len(xy))

