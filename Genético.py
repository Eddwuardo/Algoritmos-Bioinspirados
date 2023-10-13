import random

# Función para calcular la aptitud
def fitness_function(x):
    return x**2 + 2

# Generar población inicial de 30 individuos aleatorios de 4 bits
population = [random.randint(0, 15) for _ in range(30)]

# Calcular la aptitud de cada individuo y almacenarla en un diccionario
fitness_scores = {}
for individual in population:
    fitness_scores[individual] = fitness_function(individual)

# Encontrar al individuo más apto
fittest_individual = max(fitness_scores, key=fitness_scores.get)
fittest_fitness = fitness_scores[fittest_individual]

print("Población inicial:", population)
print("Aptitud de cada individuo:", fitness_scores)
print("Individuo más apto:", fittest_individual)
print("Aptitud del individuo más apto:", fittest_fitness)