import numpy as np
import random

# Define la matriz de distancias entre ciudades
distances = np.array([
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
])

# Parámetros del algoritmo de colonia de hormigas
num_ants = 4
num_iterations = 100
pheromone evaporation rate = 0.5
alpha = 1
beta = 1

# Inicialización de feromonas en las aristas
pheromones = np.ones(distances.shape)  # Inicialmente, todas las aristas tienen la misma cantidad de feromonas

# Función para calcular la probabilidad de seleccionar una arista
def calculate_probabilities(pheromone, distance, alpha, beta):
    total = (pheromone ** alpha) * ((1 / distance) ** beta)
    probabilities = total / total.sum()
    return probabilities

# Algoritmo de colonia de hormigas
best_tour = None
best_tour_length = float('inf')

for iteration in range(num_iterations):
    ant_tours = []
    ant_tour_lengths = []

    for ant in range(num_ants):
        current_city = random.randint(0, len(distances) - 1)
        tour = [current_city]
        tour_length = 0

        for _ in range(len(distances) - 1):
            unvisited_cities = [city for city in range(len(distances)) if city not in tour]
            probabilities = calculate_probabilities(pheromones[current_city, unvisited_cities], distances[current_city, unvisited_cities], alpha, beta)
            next_city = random.choices(unvisited_cities, probabilities)[0]
            tour.append(next_city)
            tour_length += distances[current_city, next_city]
            current_city = next_city

        ant_tours.append(tour)
        ant_tour_lengths.append(tour_length)

    # Actualizar feromonas en cada arista
    pheromones *= (1 - pheromone_evaporation_rate)

    for ant, tour_length in enumerate(ant_tour_lengths):
        for i in range(len(ant_tours[ant]) - 1):
            from_city, to_city = ant_tours[ant][i], ant_tours[ant][i + 1]
            pheromones[from_city, to_city] += 1.0 / tour_length
            pheromones[to_city, from_city] += 1.0 / tour_length

    # Actualizar la mejor solución encontrada hasta ahora
    if min(ant_tour_lengths) < best_tour_length:
        best_tour_length = min(ant_tour_lengths)
        best_tour = ant_tours[ant_tour_lengths.index(best_tour_length)]

print("Mejor recorrido:", best_tour)
print("Longitud del mejor recorrido:", best_tour_length)
