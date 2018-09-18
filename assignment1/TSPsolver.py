import random, sys, time, csv


class TSPsolver:

    def __init__(self, cities, data):
        self.route = cities.copy()
        self.distance = 0
        self._set_distance(data)
        self.data = data

        self.fitness = -1
        self.chance = -1
    
    def pmx_crossover(self, other_solver):
        parent_1 = self.route
        parent_2 = other_solver.route

        child_route = [None] * len(parent_1)
        used_index = []
        
        starting_index = random.randint(0, len(parent_1) - 1)
        segment_length = random.randint(1, len(parent_1) - starting_index)
        ending_index = starting_index + segment_length
        segment_p1 = parent_1[starting_index : ending_index]

        for i in range(segment_length):
            child_route[starting_index] = segment_p1[i]
            used_index.append(starting_index)
            starting_index += 1


        for index in used_index:
            if parent_2[index] not in child_route:
            
                val_p2 = parent_2[index]
                val_p1 = parent_1[index]
            
                index_itt = parent_2.index(val_p1)
                while (index_itt in used_index):
                    val_p1 = parent_1[index_itt]
                    index_itt = parent_2.index(val_p1)
            
                child_route[index_itt] = val_p2

        for i in range(len(child_route)):
            if(child_route[i] == None):
                child_route[i] = parent_2[i]

        return TSPsolver(child_route, self.data)

    def mutate(self):
        choice = random.uniform(0,1)
        if choice <= 0.25:
            return self._swap_mutate()
        elif 0.25 < choice <= 0.5:
            return self._insert_mutate()
        elif 0.5 < choice <= 0.75:
            return self._scramble_mutate()
        else:
            return self._inversion_mutation()

    def set_fitness(self, total_distance):
        self.fitness = total_distance / self.distance

    def set_chance(self, total_fitness):
        self.chance = self.fitness / total_fitness

    def _swap_mutate(self):
        #print("doing swap mutation")
        index_1 = 0
        index_2 = 0
        child_route = self.route.copy()
        while index_1 == index_2:
            index_1 = random.randint(0, len(child_route) - 1)
            index_2 = random.randint(0, len(child_route) - 1)
        
        child_route[index_1], child_route[index_2] = child_route[index_2], child_route[index_1]
        return TSPsolver(child_route, self.data)


    def _insert_mutate(self):
        #print("doing insert mutation")
        index_1 = 0
        index_2 = 0
        child_route = self.route.copy()
        while index_1 == index_2:
            index_1 = random.randint(0, len(child_route) - 1)
            index_2 = random.randint(0, len(child_route) - 1)
        
        if index_1 < index_2:
            val_to_insert = child_route.pop(index_2)
            child_route.insert(index_1 + 1, val_to_insert)
        else:
            val_to_insert = child_route.pop(index_1)
            child_route.insert(index_2 + 1, val_to_insert)

        return TSPsolver(child_route, self.data)


    def _scramble_mutate(self):
        #print("doing scramble mutation")
        index_1 = 0
        index_2 = 0
        child_route = self.route.copy()
        while index_1 == index_2:
            index_1 = random.randint(0, len(child_route))
            index_2 = random.randint(0, len(child_route))
        
        if index_1 < index_2:
            segment = child_route[index_1:index_2]
            random.shuffle(segment)
            child_route[index_1:index_2] = segment
        else:
            segment = child_route[index_2:index_1]
            random.shuffle(segment)
            child_route[index_2:index_1] = segment
        
        return TSPsolver(child_route, self.data)
    
    def _inversion_mutation(self):
        #print("doing inversion mutation")
        index_1 = 0
        index_2 = 0
        child_route = self.route.copy()
        while index_1 == index_2:
            index_1 = random.randint(0, len(child_route))
            index_2 = random.randint(0, len(child_route))
        
        if index_1 < index_2:
            segment = child_route[index_1:index_2]
            segment = list(reversed(segment))
            child_route[index_1:index_2] = segment
        else:
            segment = child_route[index_2:index_1]
            segment = list(reversed(segment))
            child_route[index_2:index_1] = segment
        
        return TSPsolver(child_route, self.data)
    

    def _set_distance(self, data):
        for i in range(len(self.route) - 1):
            self.distance += self._get_distance(self.route[i], self.route[i+1], data)
        
        self.distance += self._get_distance(self.route[-1], self.route[0], data)



    def _get_distance(self, from_c, to_c, data):
        from_index = data[0].index(from_c)
        to_index = data[0].index(to_c)
        values = data[1:]
        distance = float(values[from_index][to_index])
        return distance

    def __repr__(self):
        rep = [self.fitness , self.distance, self.route]
        return str(rep)