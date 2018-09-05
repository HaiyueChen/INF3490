import random

def order_crossover(p1, p2):
    child = [None]*len(p1)
    #should be chosen randomly
    starting_index = random.randint(0, len(p1) - 1)
    segment_length = random.randint(1, len(p1) - starting_index)
    ##########################
    ending_index = starting_index + segment_length
    segment = p1[starting_index : ending_index]

    for i in range(segment_length):
        child[starting_index] = segment[i]
        starting_index += 1

    itt_index = starting_index
    while (None in child):
        if(starting_index > len(p2) -1):
            starting_index = 0

        if(itt_index > len(p2) -1):
            itt_index = 0

        if(not (p2[itt_index] in child)):
            child[starting_index] = p2[itt_index]
            starting_index += 1

        itt_index += 1

    return child





parent1 = [8, 4, 7, 3, 6, 2, 5, 1, 9, 0]
parent2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print(order_crossover(parent1, parent2))