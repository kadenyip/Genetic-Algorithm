import random
import string

# Enter the word you want the genetic algorithm to try and solve
TARGET_WORD = "KADEN YIP".upper()
WORD_LENGTH = len(TARGET_WORD)

# Mutation rate set to 5% to prevent being permanently stuck
POPULATION_SIZE = 250
MUTATION_RATE = 0.05
VALID_CHARS = string.ascii_uppercase + " "

def generate_random_genome():
    """
    Generates a random genome string with the same length as the target word.
    """
    return "".join(random.choice(VALID_CHARS) for _ in range(WORD_LENGTH))


def calculate_fitness(genome: str):
    """
    Rewards a specific genome if certain indexes match the same target word indexes.
    """
    score = 0
    for i in range(WORD_LENGTH):
        if genome[i] == TARGET_WORD[i]:
            score += 1
    return score


def crossover(parent1: str, parent2: str):
    """
    Creates a child string by combining parent genes at a random crossover point.
    """
    midpoint = random.randint(0, WORD_LENGTH - 1)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child


def mutation(genome: str): 
    # Take the genome str and make it individual chars
    genome_list = list(genome)

    # Each individual char in a genome has a 5% chance to mutate to new char
    for i in range(WORD_LENGTH):
        if random.random() < MUTATION_RATE:
            genome_list[i] = random.choice(VALID_CHARS)
    return "".join(genome_list)


def evolve(population: list):
    """
    Sorts the population by fitness, preserves the top 10%, and fills the next
    generation with offspring produced by crossover and mutation.
    """

    # key=calculate_fitness sorts the population based on their fitness score. 
    # reverse=True makes the list descending (highest scores at the top)
    population.sort(key=calculate_fitness, reverse=True)

    # Keep the top 10% (25) of each generation's genome to continue evolving.
    # Use int() to convert from float to int to prevent crashing (lists need whole numbers).
    next_generation = population[:int(POPULATION_SIZE * 0.10)]


    # Repopulate if the next_generation has less than the original 250 starting population.
    # We use 2 parents (p1 and p2) chosen randomly from the top 50.
    while len(next_generation) < POPULATION_SIZE:
        p1 = random.choice(population[:50])
        p2 = random.choice(population[:50])

        child = crossover(p1, p2)
        # Give the child a chance to produce a new char, then add to next_generation
        child = mutation(child)
        next_generation.append(child)

    return next_generation

