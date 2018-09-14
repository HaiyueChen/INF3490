import csv, sys, time, random
from TSPsolver import TSPsolver

def evolve(individuals):
    pass













def main():
    if(len(sys.argv) == 4):
        try:
            numb_cities = int(sys.argv[1])
        except ValueError:
            print("Please write an integer as the argument for the number of cities ")
            sys.exit(-1)
        
        if(numb_cities < 1 or numb_cities > 24):
            print("Please write a integer between 1 and 24 for the number of cities")
            sys.exit(-1)
        
        try:
            numb_generations = int(sys.argv[2])        
        except ValueError:
            print("Please write an positive integer as the argument for number of generations")
            sys.exit(-1)

        if(numb_generations < 1):
            print("Please write an positive integer as the argument for number of generations")
            sys.exit(-1)

        try:
            population_size = int(sys.argv[3])
        except ValueError:
            print("Please write an positive integer as the arguemnt for population size")
            sys.exit(-1)

        if(population_size < 1):
            print("Please write an positive integer as the argument for population size")
        
        with open("european_cities.csv", "r") as f:
            data = list(csv.reader(f, delimiter=';'))

        cities = data[0]
        sub_cities = cities[0:numb_cities]


        population = []
        for i in range(population_size):
            rand_route = sub_cities.copy()
            random.shuffle(rand_route)
            population.append(TSPsolver(rand_route, data))

        for i in range(numb_generations):
            evolve(population)


        for individual in population:
            print(individual)








    else:
        print("""Correct way to use this program:\npython3 genetic_algorithm.py [number_of_cities] [number_of_generations] [population_size]
        """)




start_time = time.time()
main()
print("\nRunning time: ", (time.time() - start_time), "seconds")
print("\n----------------------------")