import csv, sys, time, random
from TSPsolver import TSPsolver

def parent_selection(population):
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

def survivor_selection(population, population_size):
    population.sort(key=lambda x: x.fitness, reverse=True)
    while len(population) > population_size:
        population.pop()



def evolve(population, data):
    population_size = len(population)
    total_distance = sum(itter.distance for itter in population)
    for solver in population:
        solver.set_fitness(total_distance)

    total_fitness = sum(itter.fitness for itter in population)
    for solver in population:
        solver.set_chance(total_fitness)


    for i in range(len(population) // 2):
        parent_1 = parent_selection(population)
        parent_2 = parent_selection(population)


        child_1 = parent_1.pmx_crossover(parent_2)
        child_2 = parent_2.pmx_crossover(parent_1)

        child_1 = child_1.mutate()
        child_2 = child_2.mutate()

        population.append(child_1)
        population.append(child_2)


    total_distance = sum(itter.distance for itter in population)
    for solver in population:
        solver.set_fitness(total_distance)

    total_fitness = sum(itter.fitness for itter in population)
    for solver in population:
        solver.set_chance(total_fitness)
    survivor_selection(population, population_size)





def main():
    if(len(sys.argv) == 3):
        try:
            numb_cities = int(sys.argv[1])
        except ValueError:
            print("Please write an integer as the argument for the number of cities ")
            sys.exit(-1)

        if(numb_cities < 1 or numb_cities > 24):
            print("Please write a integer between 1 and 24 for the number of cities")
            sys.exit(-1)


        try:
            population_size = int(sys.argv[2])
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


        gen_count = 0
        gen_without_improvement = 0
        best_individual = population[0]
        while(gen_without_improvement < 50):
            evolve(population, data)
            gen_count += 1
            if(best_individual.distance > population[0].distance):
                best_individual = population[0]
                gen_without_improvement = 0
            else:
                gen_without_improvement += 1


        print("\nTotal generations:", gen_count)
        print("Best result found in generation:", gen_count - gen_without_improvement)
        print("Fitness:", population[0].fitness)
        print("Distance:", population[0].distance)
        print("Route:", population[0].route)


    else:
        print("""Correct way to use this program:\npython3 genetic_algorithm.py [number_of_cities] [number_of_generations] [population_size]
        """)
        sys.exit(-1)




start_time = time.time()

main()



print("\nRunning time: ", (time.time() - start_time), "seconds")
print("\n----------------------------")
