import random
def pmx_crossover(p1, p2):
    child = [None] * len(p1)
    used_index = []
    #should be randomly chosen
    #starting_index = random.randint(0, len(p1) - 1)
    #segment_length = random.randint(1, len(p1) - starting_index)
    ############################
    starting_index = 2
    segment_length = 4

    ending_index = starting_index + segment_length
    segment_p1 = p1[starting_index : ending_index]

    for i in range(segment_length):
        child[starting_index] = segment_p1[i]
        used_index.append(starting_index)
        starting_index += 1


    for index in used_index:
        if p2[index] not in child:

            val_p2 = p2[index]
            val_p1 = p1[index]

            index_itt = p2.index(val_p1)
            while (index_itt in used_index):
                val_p1=p1[index_itt]
                index_itt = p2.index(val_p1)

            child[index_itt] = val_p2

    for i in range(len(child)):
        if(child[i] == None):
            child[i] = p2[i]

    return child


parent1 = [8, 4 ,7, 3, 6, 2, 5, 1, 9, 0]
parent2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(pmx_crossover(parent1, parent2))