
def busqueda_lineal(lista, codigo, tipo="elemento"):
    comparaciones = 0

    for elemento in lista:
        comparaciones += 1
        print(f"Elemento comparado: {elemento['codigo']}")

        if elemento['codigo'] == codigo:
            print(f"Comparaciones realizadas: {comparaciones}")
            print(f"{tipo} encontrado: {elemento['codigo']}")
            return elemento

    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"No se encontro el {tipo} con codigo '{codigo}'.")
    return None

def _ordenar_por_codigo(drones):

    for i in range(1, len(drones)):
        actual = drones[i]
        j = i - 1
        while j >= 0 and drones[j]['codigo'] > actual['codigo']:
            drones[j + 1] = drones[j]
            j -= 1
        drones[j + 1] = actual
    return drones


def busqueda_binaria(drones, codigo):
    drones_ordenados = _ordenar_por_codigo(drones[:])

    low = 0
    high = len(drones_ordenados) - 1

    while low <= high:
        mid = (low + high) // 2
        valor_medio = drones_ordenados[mid]['codigo']
        print(f"low: {low}, high: {high}, mid: {mid}, valor medio: {valor_medio}")

        if valor_medio == codigo:
            print(f"Dron encontrado: {codigo}")
            return drones_ordenados[mid]
        elif valor_medio < codigo:
            low = mid + 1
        else:
            high = mid - 1

    print(f"No se encontro el dron con codigo '{codigo}'.")
    return None
