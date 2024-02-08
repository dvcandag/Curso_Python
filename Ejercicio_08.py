# Ejercicio 8: Algoritmo de Búsqueda en Amplitud (BFS)

from collections import deque  # se importa la clase deque desde el módulo collections

def bfs(grafo, inicio):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    cola = deque([inicio])  # se crea una cola utilizando deque con el nodo inicial
    visitados.add(inicio)  # Marcando el nodo inicial como visitado
    while cola:  # Mientras la cola no esté vacía
        nodo = cola.popleft()  # se sacaa el primer elemento de la cola (nodo actual)
        for vecino in grafo[nodo]:  # Iterar sobre los vecinos del nodo actual
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                visitados.add(vecino)  # se  marca el vecino como visitado
                cola.append(vecino)  # Agregando el vecino a la cola para explorarlo más tarde
    return list(visitados)  # Se convierte el conjunto de nodos visitados en una lista y devolverla

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
print("Nodos alcanzables desde", inicio + ":", nodos_alcanzables)  # Se imprime los nodos alcanzables
