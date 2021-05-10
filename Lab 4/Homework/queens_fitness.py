import random

p_mutation = 0.4
num_of_generations = 5



def fitness_fn_negative(individual):
    '''
    Compute the number of conflicting pairs, negated.
    For a solution with 5 conflicting pairs the return value is -5, so it can
    be maximized to 0.
    '''

    n = len(individual)
    fitness = 0
    for column, row in enumerate(individual):
        contribution = 0

        # Horizontal
        for other_column in range(column + 1, n):
            if individual[other_column] == row:
                contribution += 1

        # Diagonals
        for other_column in range(column + 1, n):
            row_a = row + (column - other_column)
            row_b = row - (column - other_column)
            if 0 <= row_a < n and individual[other_column] == row_a:
                contribution += 1
            if 0 <= row_b < n and individual[other_column] == row_b:
                contribution += 1

        fitness += contribution

    return - fitness


def fitness_fn_positive(state):
    '''
    Compute the number of non-conflicting pairs.
    '''

    def conflicted(state, row, col):
        for c in range(col):
            if conflict(row, col, state[c], c):
                return True

        return False

    def conflict(row1, col1, row2, col2):
        return (
            row1 == row2 or
            col1 == col2 or
            row1 - col1 == row2 - col2 or
            row1 + col1 == row2 + col2
        )

    fitness = 0
    for col in range(len(state)):
        for pair in range(1, col + 1):
            if not conflicted(state, state[pair], pair):
                fitness = fitness + 1
    return fitness



def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            for c in child:
                if random.uniform(0, 1) < p_mutation:
                    c = mutate(c)
                new_population.add(c)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    child1 = []
    child2 = []
    crossover_bit = random.randint(0, 8)
    for i in range(0, crossover_bit):
        child1.append(mother[i])
    for i in range(crossover_bit, 8):
        child1.append(father[i])
    child1 = (child1[0], child1[1], child1[2], child1[3], child1[4], child1[5], child1[6], child1[7])
    
    for i in range(0, crossover_bit):
        child2.append(father[i])
    for i in range(crossover_bit, 8):
        child2.append(mother[i])
    child2 = (child2[0], child2[1], child2[2], child2[3], child2[4], child2[5], child2[6], child2[7])
    
    return [child1, child2]


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    m = []
    for i in individual:
        m.append(i)
    m[random.randint(0,7)] = random.randint(1,8)
    mutation = (m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7])
    return mutation


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    total_fitness = 0
    for i in ordered_population:
        total_fitness += fitness_fn_positive(i)
    current_sum = 0
    motherNum = random.randint(0, total_fitness)
    fatherNum = random.randint(0, total_fitness)

    mother = 0
    father = 0
    for i in ordered_population:
        current_sum += fitness_fn_positive(i)
        if current_sum >= motherNum:
            mother = i
            break
    current_sum = 0
    for i in ordered_population:
        current_sum += fitness_fn_positive(i)
        if current_sum >= fatherNum:
            father = i
            break
    
    selected = (mother, father)
    return selected

def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(1, 8) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    
    initial_population = get_initial_population(8, 4)

    fittest = genetic_algorithm(initial_population, fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + ' - fitness: ' + str(fitness_fn_negative(fittest)))

if __name__ == '__main__':
    main()
