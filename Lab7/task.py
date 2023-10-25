import random
import math

# Define the list of cities and their coordinates
cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (9, 1),
}

# Create a random initial population of routes
def create_population(city_list, population_size):
    population = [list(city_list.keys()) for _ in range(population_size)]
    for route in population:
        random.shuffle(route)
    return population

# Calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += math.dist(cities[city1], cities[city2])
    return total_distance

# Select two parents from the population using tournament selection
def select_parents(population, k=3):
    tournament = random.sample(population, k)
    return min(tournament, key=calculate_total_distance)

# Apply ordered crossover to create a new route
def ordered_crossover(parent1, parent2):
    n = len(parent1)
    start = random.randint(0, n - 1)
    end = random.randint(start, n)
    offspring = [None] * n

    # Copy a slice from parent1 to the offspring
    offspring[start:end] = parent1[start:end]

    # Fill in the rest of the offspring with elements from parent2
    for city in parent2:
        if city not in offspring:
            for i in range(n):
                if offspring[i] is None:
                    offspring[i] = city
                    break

    return offspring

# Apply mutation by swapping two cities in the route
def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

# Genetic Algorithm
def genetic_algorithm(city_list, population_size, generations):
    population = create_population(city_list, population_size)

    for generation in range(generations):
        new_population = []

        for _ in range(population_size // 2):
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            offspring1 = ordered_crossover(parent1, parent2)
            offspring2 = ordered_crossover(parent2, parent1)

            if random.random() < 0.1:
                mutate(offspring1)
            if random.random() < 0.1:
                mutate(offspring2)

            new_population.extend([offspring1, offspring2])

        population = new_population

    best_route = min(population, key=calculate_total_distance)
    return best_route, calculate_total_distance(best_route)

# Example usage
best_route, best_distance = genetic_algorithm(cities, population_size=100, generations=1000)
print(f"Best Route: {best_route}")
print(f"Total Distance: {best_distance}")