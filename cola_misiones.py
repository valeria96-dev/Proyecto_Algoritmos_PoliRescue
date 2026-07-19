#Cola de misiones pendientes (estructura FIFO)

def agregar_mision_cola(cola, mision):
    cola.append(mision)
    print(f"Mision '{mision['codigo']}' agregada a la cola de pendientes.")


def atender_mision(cola):
    if len(cola) == 0:
        print("No hay misiones pendientes en la cola.")
        return None

    mision = cola[0]

    for i in range(len(cola) - 1):
        cola[i] = cola[i + 1]
    cola.pop()

    mision['estado'] = 'Atendida'
    print(f"Mision atendida: {mision['codigo']} (Zona: {mision['zona']})")
    return mision


def mostrar_siguiente_mision(cola):

    if len(cola) == 0:
        print("No hay misiones pendientes.")
        return
    siguiente = cola[0]
    print(f"Siguiente mision a atender: {siguiente['codigo']} - "
          f"Zona: {siguiente['zona']} - Prioridad: {siguiente['prioridad']}")


def mostrar_cola(cola):
    if len(cola) == 0:
        print("La cola de misiones esta vacia.")
        return
    print("--- COLA DE MISIONES PENDIENTES ---")
    for mision in cola:
        print(f"{mision['codigo']} | Zona: {mision['zona']} | "
              f"Prioridad: {mision['prioridad']} | Estado: {mision['estado']}")
