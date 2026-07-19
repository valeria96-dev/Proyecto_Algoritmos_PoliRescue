#Modulo de Algoritmos de Ordenamiento

def ordenar_burbuja_prioridad(misiones):
    n = len(misiones)
    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"Comparando: '{misiones[j]['codigo']}' (prioridad {misiones[j]['prioridad']}) "
                  f"con '{misiones[j+1]['codigo']}' (prioridad {misiones[j+1]['prioridad']})")

            if misiones[j]['prioridad'] > misiones[j + 1]['prioridad']:
                print(f"Intercambiando: '{misiones[j]['codigo']}' <-> '{misiones[j+1]['codigo']}'")
                misiones[j], misiones[j + 1] = misiones[j + 1], misiones[j]

        print(f"Lista actual: {[m['codigo'] for m in misiones]}")

    print("Ordenamiento burbuja finalizado.\n")


def ordenar_insercion_bateria(drones):
    for i in range(1, len(drones)):
        actual = drones[i]
        print(f"Insertando: '{actual['codigo']}' (bateria {actual['bateria']}%)")

        j = i - 1
        while j >= 0 and drones[j]['bateria'] > actual['bateria']:
            print(f"Moviendo: '{drones[j]['codigo']}' una posicion a la derecha")
            drones[j + 1] = drones[j]
            j -= 1

        drones[j + 1] = actual
        print(f"Lista actual: {[d['codigo'] for d in drones]}")

    print("Ordenamiento por insercion finalizado.\n")



def merge_sort_velocidad(drones):
    if len(drones) <= 1:
        return drones

    medio = len(drones) // 2
    izquierda = drones[:medio]
    derecha = drones[medio:]

    print(f"Dividiendo: {[d['codigo'] for d in drones]} -> "
          f"{[d['codigo'] for d in izquierda]} | {[d['codigo'] for d in derecha]}")

    izquierda = merge_sort_velocidad(izquierda)
    derecha = merge_sort_velocidad(derecha)

    resultado = _mezclar(izquierda, derecha)
    print(f"Resultado parcial: {[d['codigo'] for d in resultado]}")
    return resultado


def _mezclar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['velocidad'] <= derecha[j]['velocidad']:
            print(f"Mezclando: tomando '{izquierda[i]['codigo']}' (velocidad {izquierda[i]['velocidad']})")
            resultado.append(izquierda[i])
            i += 1
        else:
            print(f"Mezclando: tomando '{derecha[j]['codigo']}' (velocidad {derecha[j]['velocidad']})")
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado



def quick_sort_distancia(misiones, bajo=0, alto=None):
    if alto is None:
        alto = len(misiones) - 1

    if bajo < alto:
        pos_pivote = _particionar(misiones, bajo, alto)
        quick_sort_distancia(misiones, bajo, pos_pivote - 1)
        quick_sort_distancia(misiones, pos_pivote + 1, alto)

    if bajo == 0 and alto == len(misiones) - 1:
        print(f"Resultado: {[m['codigo'] for m in misiones]}")
        print("Ordenamiento quicksort finalizado.\n")


def _particionar(misiones, bajo, alto):

    pivote = misiones[alto]
    print(f"Pivote: '{pivote['codigo']}' (distancia {pivote['distancia']} km)")

    i = bajo - 1
    for j in range(bajo, alto):
        if misiones[j]['distancia'] <= pivote['distancia']:
            i += 1
            misiones[i], misiones[j] = misiones[j], misiones[i]

    misiones[i + 1], misiones[alto] = misiones[alto], misiones[i + 1]
    print(f"Particion: {[m['codigo'] for m in misiones[bajo:alto+1]]}")
    return i + 1
