#Modulo de Algoritmos de Grafo: BFS y Dijkstra
import heapq

def bfs_verificar_camino(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        print(f"No existe un camino entre '{inicio}' y '{destino}' (zona no registrada).")
        return False

    visitados = [inicio]
    cola = [inicio]

    print(f"Iniciando BFS desde '{inicio}' hacia '{destino}'")

    while len(cola) > 0:
        nodo_actual = cola[0]

        for i in range(len(cola) - 1):
            cola[i] = cola[i + 1]
        cola.pop()

        print(f"Visitando: {nodo_actual}")
        print(f"Cola actual: {cola}")
        print(f"Nodos visitados: {visitados}")

        if nodo_actual == destino:
            print(f"Camino encontrado hacia '{destino}'.\n")
            return True

        for vecino, distancia in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    print(f"No existe un camino entre '{inicio}' y '{destino}'.\n")
    return False



def dijkstra_ruta_minima(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}

    cola_prioridad = [(0, inicio)]
    visitados = []

    print(f"Calculando ruta minima desde '{inicio}' hasta '{destino}'")

    while len(cola_prioridad) > 0:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in visitados:
            continue
        visitados.append(nodo_actual)

        print(f"Nodo actual: {nodo_actual}")
        print(f"Distancias: {distancias}")

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                print(f"Ruta parcial actualizada hacia '{vecino}': distancia {nueva_distancia} km")

    if distancias[destino] == float('inf'):
        print(f"No existe ruta hacia '{destino}'.\n")
        return None, float('inf')


    ruta = []
    nodo = destino
    while nodo is not None:
        ruta.append(nodo)
        nodo = predecesores[nodo]
    ruta.reverse()

    print(f"Ruta final: {' -> '.join(ruta)}")
    print(f"Distancia total: {distancias[destino]} km\n")

    return ruta, distancias[destino]
