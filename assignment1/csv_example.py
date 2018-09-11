import csv
import itertools

with open("european_cities.csv", "r") as f:
    data = list(csv.reader(f, delimiter=';'))

cities = data[0][0: 3]
permutations = itertools.permutations(cities) 
for perm in permutations: 
    print(list(perm))
