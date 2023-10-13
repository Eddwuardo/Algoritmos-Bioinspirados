import random
import math

# Datos de ventas en un período de 7 días (puedes reemplazar estos valores con los tuyos)
ventas = [240, 210, 180, 120, 50, 0, 0]

# Función objetivo: devuelve la ganancia total para un conjunto de días
def calcular_ganancia(dias_seleccionados):
    return sum(ventas[dia] for dia in dias_seleccionados)

# Función para generar una solución vecina (cambiar un día)
def generar_vecino(solucion_actual):
    vecino = solucion_actual.copy()  # Copia la solución actual
    dia_a_cambiar = random.randint(0, 6)  # Elije un día al azar para cambiar
    nuevo_dia = random.randint(0, 6)  # Elije un nuevo día al azar
    vecino[dia_a_cambiar] = nuevo_dia  # Cambia el día seleccionado en la solución vecina
    return vecino

# Implementación del algoritmo de Recocido Simulado
def recocido_simulado(temperatura_inicial, enfriamiento, iteraciones):
    solucion_actual = [random.randint(0, 6) for _ in range(7)]  # Genera una solución inicial aleatoria
    mejor_solucion = solucion_actual.copy()  # Inicializa la mejor solución con la solución actual
    temperatura = temperatura_inicial  # Inicializa la temperatura con el valor inicial

    for _ in range(iteraciones):
        vecino = generar_vecino(solucion_actual)  # Genera una solución vecina
        diferencia = calcular_ganancia(vecino) - calcular_ganancia(solucion_actual)  # Calcula la diferencia de ganancia

        # Si la nueva solución es mejor o se acepta con probabilidad, actualiza la solución actual
        if diferencia > 0 or random.random() < math.exp(diferencia / temperatura):
            solucion_actual = vecino.copy()

            # Si la nueva solución es mejor que la mejor conocida, actualiza la mejor solución
            if calcular_ganancia(solucion_actual) > calcular_ganancia(mejor_solucion):
                mejor_solucion = solucion_actual.copy()

        temperatura *= enfriamiento  # Reduce la temperatura gradualmente

    ganancia_total = calcular_ganancia(mejor_solucion)

    return mejor_solucion, ganancia_total

# Parámetros del algoritmo
temperatura_inicial = 1000.0
enfriamiento = 0.95
iteraciones = 10000

# Ejecutar el algoritmo y obtener el mejor día de ventas
mejor_solucion, ganancia_total = recocido_simulado(temperatura_inicial, enfriamiento, iteraciones)
mejor_dia = mejor_solucion[0]

print("Mejor día de ventas:", mejor_dia + 1)  # Sumamos 1 para mostrar el día en formato humano (1-7)
print("Ventas en el mejor día:", ventas[mejor_dia])
print("Ganancia total en el mejor día: ", ganancia_total)