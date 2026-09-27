# Genetic Algorithm: Target Word Evolution

<img align="right" width="404" height="662" style="border: none;" alt="Image" src="https://github.com/user-attachments/assets/e697771a-43f4-4dd4-824e-b00380430ecb">

A small Python demonstration of a genetic algorithm that evolves strings through generations until one matches a target phrase. Each generation ranks candidate strings by how many characters match the target at the same positions, preserves the strongest candidates, and creates new candidates through crossover and random mutation.

## How it works

- **Population:** starts with 250 randomly generated strings.
- **Fitness:** scores one point for each character that matches the target at the same position.
- **Elitism:** carries the top 10% of each generation forward unchanged.
- **Parent selection:** chooses parents from the top 50 candidates.
- **Crossover:** combines two parent strings at a randomly selected position.
- **Mutation:** gives each character a 5% chance of changing to a random uppercase letter or space.
- **Progress display:** prints the five highest scoring candidates each generation and stops when the target is reached.

## Run

```bash
python display.py
```

Edit `TARGET_WORD` in `ga_logic.py` to choose the phrase the population should evolve toward. The target is converted to uppercase.



## Files



- `ga_logic.py` contains the genetic algorithm operations and configuration.

- `display.py` runs the evolution loop and prints generation progress in the terminal.



The project uses only Python's standard library.
