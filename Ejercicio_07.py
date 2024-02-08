# Ejercicio 7: Algoritmo de Kruskal para Árboles de Expansión Mínima (MST)

def kruskal(grafo):
    mst = []  # Inicializa la lista que contendrá el MST
    aristas = []  # Inicializa una lista para almacenar las aristas del grafo
    # se convierte el grafo en una lista de aristas
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            aristas.append((nodo, vecino, peso))
    # Se rdena las aristas por peso
    aristas.sort(key=lambda x: x[2])
    padre = {nodo: nodo for nodo in grafo}  # Inicializamos un diccionario para almacenar los padres de cada nodo

    def encontrar(nodo):
        while padre[nodo] != nodo:
            nodo = padre[nodo]
        return nodo

    def unir(nodo1, nodo2):
        padre_nodo1 = encontrar(nodo1)
        padre_nodo2 = encontrar(nodo2)
        padre[padre_nodo1] = padre_nodo2  # Unimos los árboles con raíces nodo1 y nodo2

    # Iterar sobre las aristas en orden ascendente de peso
    for arista in aristas:
        nodo1, nodo2, peso = arista
        # Verifica si la inclusión de la arista no forma un ciclo en el MST actual
        if encontrar(nodo1) != encontrar(nodo2):
            mst.append(arista)  # See agrega la arista al MST
            unir(nodo1, nodo2)  # se uni los árboles que contienen los nodos de la arista

    return mst  # Devolvemos el MST

# Ejemplo de uso:
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

mst = kruskal(grafo)
print("Árbol de expansión mínima (MST):", mst)
