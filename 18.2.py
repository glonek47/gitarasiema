"""text = open("C:/Users/jarek/Desktop/pantadeusz.txt").read()
count = -1
for i, lines in enumerate(text):
    count += 1
    if i == 8 or i ==12 or i ==60 or i == 98 or i ==104:
        print(lines)
        count += 1
    print("ilość wierszy w inwokacji to ", count)"""
import linecache
wiersz1 = linecache.getline('C:/Users/jarek/Desktop/pantadeusz.txt', 8)
wiersz2 = linecache.getline('C:/Users/jarek/Desktop/pantadeusz.txt', 12)
wiersz3 = linecache.getline('C:/Users/jarek/Desktop/pantadeusz.txt', 60)
wiersz4 = linecache.getline('C:/Users/jarek/Desktop/pantadeusz.txt', 98)
wiersz5 = linecache.getline('C:/Users/jarek/Desktop/pantadeusz.txt', 104)
print(wiersz1)
print(wiersz2)
print(wiersz3)
print(wiersz4)
print(wiersz5)
count = len(open('C:/Users/jarek/Desktop/pantadeusz.txt', 'r').readlines())
print(count)