# Ejercicio 5: Implementación de Algoritmos Avanzados

import heapq
def dijkstra(grafo, inicio):
    # Paso 1: Inicialización de variables
    distancia = {nodo: float('inf') for nodo in grafo}  # Distancias más cortas conocidas desde el nodo de inicio
    distancia[inicio] = 0  # La distancia desde el nodo de inicio hasta sí mismo es 0
    cola = [(0, inicio)]  # Cola de prioridad para nodos a explorar, inicializada con el nodo de inicio

    while cola:
        # Paso 2: Extraer nodo con la distancia acumulada más corta de la cola
        dist, nodo = heapq.heappop(cola)

        # Paso 3: Actualización de distancias
        if dist > distancia[nodo]:
            continue  # Ignorar nodo si su distancia acumulada es mayor que la distancia conocida
          
        # Paso 4: Explorar vecinos
        for vecino, peso in grafo[nodo].items():
            nueva_dist = dist + peso  # Calcular nueva distancia acumulada hacia el vecino
            if nueva_dist < distancia[vecino]:
                distancia[vecino] = nueva_dist  # Actualizar distancia conocida hasta el vecino
                heapq.heappush(cola, (nueva_dist, vecino))  # Agregar vecino a la cola con su nueva distancia acumulada

    # Paso 5: Devolver distancias más cortas desde el nodo de inicio hasta cada nodo del grafo
    return distancia

# Ejemplo de uso:
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
inicio = 'B'
distancias = dijkstra(grafo, inicio) 
print("Distancias más cortas desde el nodo", inicio + ":")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")
# LAS Distancias cambia a cada valor de grafo 

inicio = 'D'
distancias = dijkstra(grafo, inicio) 
print("Distancias más cortas desde el nodo", inicio + ":")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")
# LAS Distancias cambia a cada valor de grafo 