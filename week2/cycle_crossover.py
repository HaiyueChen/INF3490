import random


def cycle_crossover(p1, p2):
    child = [None] * len(p1)
    p1_itt = p1
    p2_itt = p2
    while None in c:
        index = child.index(None)
        indices = []
        values = []
        while index not in indices:
            val = p1[index]
            indices.append(index)
            values.append(val)
            index = p1.index(p2[index])
        for index, val in zip(indices, values):
            child[index] = val
        if(p1_itt == p1):
            p1_itt = p2
        else:
            p1_itt = p1

        if(p2_itt == p2):
            p2_itt = p1
        else:
            p2_itt = p2
    return child