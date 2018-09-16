import csv, itertools, sys, time


def get_distance(from_c, to_c, data):
    from_index = data[0].index(from_c)
    to_index = data[0].index(to_c)
    values = data[1:]
    distance = values[from_index][to_index]
    return float(distance)

def get_sum_distance(cities, data):
    sum_distance = 0
    
    for i in range(len(cities) - 1):
        sum_distance += get_distance(cities[i], cities[i + 1],data)
    
    sum_distance += get_distance(cities[-1], cities[0], data)
    return sum_distance

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
            permutations = itertools.permutations(sub_cities)

            best_path = []
            best_distance = -1
            path_count = 0
            best_numb = 0
            for path in permutations:
                cities = list(path)
                curr_distance = get_sum_distance(cities, data)
                if(curr_distance < best_distance or best_distance == -1):
                    best_numb = path_count
                    best_distance = curr_distance
                    best_path = cities
                print("Current:", path_count, " Best:", best_numb)
                path_count += 1


            print("----------------------------\n")
            print("Total possible paths:" , path_count)
            print()
            print("Shortest path:" , best_path)
            print("Distance:" , best_distance)

    else:
        print('''Correct way to use this program
        python3 exhaustive_search.py [number_of_cities]''')
        sys.exit(-1)

start_time = time.time()
main()
print()
print("Running time: ", (time.time()- start_time) , "seconds")
print("\n----------------------------")
