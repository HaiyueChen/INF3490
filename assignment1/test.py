import random

liste = [1, 2, 3, 4, 5, 6, 0]
print(liste)

segment = liste[1:4]

segment = list(reversed(segment))
print(type(segment))
liste[1:4] = segment
print(liste)