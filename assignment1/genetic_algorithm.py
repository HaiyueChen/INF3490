import csv, sys, time, random
from TSPsolver import TSPsolver

def selection(population):
    selected = None
    index = random.randint(0, len(population) - 1)
    while selected == None:
        if index == len(population):
            index = 0

        selector = random.uniform(0, 1)
        if(selector < population[index].chance):
            selected = population[index]
        index += 1

    return selected


def evolve(population, data):
    total_distance = sum(itter.distance for itter in population)
    for solver in population:
        solver.set_fitness(total_distance)

    total_fitness = sum(itter.fitness for itter in population)
    for solver in population:
        solver.set_chance(total_fitness)

    new_population = []

    for i in range(len(population)):
        parent_1 = selection(population)
        parent_2 = selection(population)

        child_1 = parent_1.pmx_crossover(parent_2, data)
        child_2 = parent_2.pmx_crossover(parent_1, data)

        child_1 = child_1.mutate()
        child_2 = child_2.mutate()

        new_population.append(child_1)
        new_population.append(child_2)

    population = new_population








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
            evolve(population, data)


            for individual in population:
                print(individual)

            print()







    else:
        print("""Correct way to use this program:\npython3 genetic_algorithm.py [number_of_cities] [number_of_generations] [population_size]
        """)



"""
start_time = time.time()
main()
print("\nRunning time: ", (time.time() - start_time), "seconds")
print("\n----------------------------")
"""


def test():
    with open("european_cities.csv", "r") as f:
        data = list(csv.reader(f, delimiter=';'))

    cities = data[0][0:6]
    population = []
    population_size = 4
    route = cities.copy()
    solver = TSPsolver(route, data)
    print(solver)
    for i in range(9999999):
        solver = solver.mutate()
    print(solver)


"""
    for i in range(population_size):
        rand_route = cities.copy()
        random.shuffle(rand_route)
        population.append(TSPsolver(rand_route, data))

    for itt in population:
        print(itt)

    for i in range(numb_generations):
        evolve(population, data)

        for individual in population:
            print(individual)
"""

test()