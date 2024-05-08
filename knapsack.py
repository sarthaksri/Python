import random
MAX_CAPACITY=100
POPULATION_SIZE=4
ITERATIONS=10
MUTATION_BITS=[0,1,2,3]
items=[
    {"name":"A","weight":45,"value":3},
    {"name":"B","weight":40,"value":5},
    {"name":"C","weight":50,"value":8},
    {"name":"D","weight":90,"value":10},
]


def calculate_fitness(chromosome):
    total_weight=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    total_value=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    if total_weight>MAX_CAPACITY:
        total_value=0
    return total_value

def selection(population):
    sorted_population=sorted(population,key=calculate_fitness, reverse=True)
    return sorted_population

def crossover(parent1, parent2):
    crossover_point=len(parent1)//2
    child=parent1[:crossover_point]+parent2[crossover_point:]
    return child

def mutation(chromosome):
    mutated_choromosome=chromosome.copy()
    for bit in MUTATION_BITS:
        mutated_choromosome[bit]=1-mutated_choromosome[bit]
    return mutated_choromosome

population=[[1,1,1,1],[1,0,0,0],[1,0,1,0],[1,0,0,1]]

for iteration in range(ITERATIONS):
    print(f"Iterantion {iteration+1}:")
    print("Population: ",population)
    selected=selection(population)
    print("Selected: ",selected[:2])
    offspring=crossover(selected[2],selected[3])
    print("Offspring: ",offspring)
    mutated_offspring=mutation(offspring)
    print("Mutated Offspring: ",mutated_offspring)
    index = population.index(selected[3])
    population[index]=mutated_offspring
    print()
best_chromosome=max(population, key = calculate_fitness)
print("Final Best Chromosome: ",best_chromosome)
print("Final Fitness Value: ", calculate_fitness(best_chromosome))