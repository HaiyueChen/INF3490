import csv
import sys
import time
import random

def get_distance(from_c, to_c, data):
    from_index = data[0].index(from_c)
    to_index = data[0].index(to_c)
    values = data[1:]
    distance = values[from_index][to_index]
    return float(distance)


def get_sum_distance(cities, data):
    sum_distance = 0

    for i in range(len(cities) - 1):

        sum_distance += get_distance(cities[i], cities[i + 1], data)
    return sum_distance


def randomize(route):
    index_1 = 0
    index_2 = 0
    while(index_1 == index_2):
        index_1 = random.randint(0, len(route)-1)
        index_2 = random.randint(0, len(route)-1)

    new_route = route.copy()
    new_route[index_1], new_route[index_2] = new_route[index_2], new_route[index_1]
    return new_route


def hill_climbing(starting_route, data, max_iteration):
    best_route = starting_route
    best_distance = get_sum_distance(starting_route, data)

    itertations = 0
    iter_without_improvement = 0
    while(itertations < max_iteration and iter_without_improvement < 10 ):
        #print(starting_route)
        new_route = randomize(best_route)
        #print(new_route)
        new_route.append(new_route[0])
        #print(new_route)
        #input()
        new_distance = get_sum_distance(new_route, data)
        if(new_distance < best_distance):
            new_route.pop()
            best_route = new_route
            best_distance = new_distance
        else:
            iter_without_improvement += 1

        itertations += 1

    return [best_distance, best_route]


def main():
    if(len(sys.argv) == 2):
        try:
            numb_cities = int(sys.argv[1])
        except ValueError:
            print("Please write a number as the commandline argument")
            sys.exit(-1)

        if(numb_cities > 24 or numb_cities < 1):
            print("Please write a number between 1 and 24")
            sys.exit(-1)
        else:
            with open("european_cities.csv", "r") as f:
                data = list(csv.reader(f, delimiter=';'))

            cities = data[0]

            sub_cities = cities[0:numb_cities]

            acc_solutions = []
            for i in range(5):
                route = sub_cities.copy()
                random.shuffle(route)
                acc_solutions.append(hill_climbing(route, data, 50))

            for route in acc_solutions:
                print(route)

    else:
        print('''Correct way to use this program
        python3 exhaustive_search.py [number_of_cities]''')
        sys.exit(-1)

main()