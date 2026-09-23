import time

from ga_logic import (
    TARGET_WORD, 
    WORD_LENGTH, 
    POPULATION_SIZE, 
    generate_random_genome, 
    calculate_fitness, 
    evolve
)

def main():
    print("Target Word: " + TARGET_WORD)
    
    # Initialize the very first generation
    population = [generate_random_genome() for _ in range(POPULATION_SIZE)]
    generation = 1
    
    while True:
        # Sort the population so the highest scoring genomes are at the top
        population.sort(key=calculate_fitness, reverse=True)

        # Take the best scoring genome of the current population
        best_fitness = calculate_fitness(population[0])
        
        print("")
        print("Generation " + str(generation) + "(Best Score: " + str(best_fitness) + " / " + str(WORD_LENGTH) + ")")
        print("")

        # Loop through the top 5 genomes in the population and print the full strings
        for i in range(5):
            current_genome = population[i]
            current_score = calculate_fitness(current_genome)
            print("Rank " + str(i + 1) + ": " + current_genome + "(Score: " + str(current_score) + ")")
        
        # Check to see if the amount of correct chars from the best genome matches the exact length of the target word
        if best_fitness == WORD_LENGTH:
            print("Evolution complete! Target reached in " + str(generation) + " generations.")
            
            break
            
        # If the best genome does not match the target word, continue to evolve the population and increase the generation by 1
        population = evolve(population)
        generation += 1
        
        # Create a 0.5 second delay so that it's possible to see each generation
        time.sleep(0.5)

if __name__ == "__main__":
    main()
