# Ejercicio 6: Implementación de Algoritmos Avanzados


from collections import deque  # Importar la clase deque desde el módulo collections
def bfs(grafo, inicio):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    cola = deque([inicio])  # Crear una cola utilizando deque con el nodo inicial
    visitados.add(inicio)  # Marcar el nodo inicial como visitado
    while cola:  # Mientras la cola no esté vacía
        nodo = cola.popleft()  # Sacar el primer elemento de la cola (nodo actual)
        for vecino in grafo[nodo]:  # Iterar sobre los vecinos del nodo actual
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                visitados.add(vecino)  # Marcar el vecino como visitado
                cola.append(vecino)  # Agrega el vecino a la cola para explorarlo más tarde
    return list(visitados)  # Convertir el conjunto de nodos visitados en una lista y devolverla

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
inicio = 'A'  # Nodo de inicio para la búsqueda en amplitud
nodos_alcanzables = bfs(grafo, inicio)  # Llama a la función bfs para encontrar los nodos alcanzables desde el nodo de inicio

print("Nodos alcanzables desde", inicio + ":", nodos_alcanzables)  # Imprime los nodos alcanzables
