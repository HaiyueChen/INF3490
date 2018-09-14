import csv, sys, time, random


def get_distance(from_c, to_c, data):
    from_index = data[0].index(from_c)
    to_index = data[0].index(to_c)
    values = data[1:]
    distance = values[from_index][to_index]
    #print("From:", from_c, " To:", to_c, "Distance:", distance)
    return float(distance)


def get_sum_distance(cities, data):
    sum_distance = 0

    for i in range(len(cities) - 1):
        sum_distance += get_distance(cities[i], cities[i + 1], data)

    sum_distance += get_distance(cities[-1], cities[0], data)
    return sum_distance


def randomize(route):
    index_1 = 0
    index_2 = 0
    while(index_1 == index_2):
        index_1 = random.randint(0, len(route)-1)
        index_2 = random.randint(0, len(route)-1)

    print("index1:", index_1, " index2:", index_2)
    new_route = route.copy()
    new_route[index_1], new_route[index_2] = new_route[index_2], new_route[index_1]
    return new_route


def hill_climbing(starting_route, data):
    current_best_route = starting_route
    current_best_distance = get_sum_distance(starting_route, data)

    itertations = 0
    iter_without_improvement = 0
    while(iter_without_improvement < 100):
        new_route = current_best_route.copy()
        random.shuffle(new_route)
        new_distance = get_sum_distance(new_route, data)
        if(new_distance < current_best_distance):
            current_best_route = new_route
            current_best_distance = new_distance
            iter_without_improvement = 0
        else:
            iter_without_improvement += 1

        itertations += 1

    return [current_best_distance, current_best_route]

def standard_deviation(all_routes, mean):
    square_deviations = 0
    for route in all_routes:
        square_deviations += (route[0] - mean)**2

    return (square_deviations/len(all_routes))**0.5

def calc_mean(all_routes):
    summ = 0
    for route in all_routes:
        summ += route[0]

    return summ / len(all_routes)

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

            for i in range(100):
                route = sub_cities.copy()
                random.shuffle(route)
                route.append(route[0])
                acc_solutions.append(hill_climbing(route, data))

            acc_solutions.sort(key=lambda x: x[0])

            print("----------------------------\n")
            print("Total attempts: 100\n")
            print("Shortest path:", acc_solutions[0][1])
            print("Distance:", acc_solutions[0][0])
            print()
            print("Longest path:", acc_solutions[-1][1])
            print("Distance:", acc_solutions[-1][0])
            print()
            mean = calc_mean(acc_solutions)
            print("Average distance:", mean)
            print("Standard deviation:", standard_deviation(acc_solutions, mean))




    else:
        print('''Correct way to use this program
        python3 exhaustive_search.py [number_of_cities]''')
        sys.exit(-1)


start_time = time.time()
main()
print("Running time: ", (time.time() - start_time), "seconds")
print("\n----------------------------")