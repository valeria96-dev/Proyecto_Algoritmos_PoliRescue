#Simulacion completa de rescate

from misiones import registrar_mision
from cola_misiones import agregar_mision_cola, atender_mision
from arbol_bst import insertar_bst
from ordenamientos import ordenar_burbuja_prioridad
from drones import buscar_dron_disponible
from grafo_algoritmos import bfs_verificar_camino, dijkstra_ruta_minima


def simular_rescate(drones, misiones, cola_pendientes, raiz_bst, grafo, datos_mision):

    print("==================================")
    print(f"NUEVA EMERGENCIA REPORTADA EN: {datos_mision['zona'].upper()}")
    print("==================================" )

    print("\n--- Paso 1: Registro de la mision ---")
    mision = registrar_mision(
        misiones,
        datos_mision['codigo'],
        datos_mision['zona'],
        datos_mision['tipo_emergencia'],
        datos_mision['prioridad'],
        datos_mision['personas_afectadas'],
        datos_mision['distancia']
    )

    print("\n--- Paso 2: Insercion en la cola de pendientes ---")
    agregar_mision_cola(cola_pendientes, mision)

    print("\n--- Paso 3: Insercion en el Arbol Binario de Busqueda ---")
    raiz_bst = insertar_bst(raiz_bst, mision)

    print("\n--- Paso 4: Ordenamiento de misiones por prioridad (Burbuja) ---")
    ordenar_burbuja_prioridad(misiones)

    print("--- Paso 5: Busqueda de un dron disponible ---")
    dron_asignado = buscar_dron_disponible(drones)
    if dron_asignado is None:
        print("No hay drones disponibles en este momento. La mision queda en espera.\n")
        return raiz_bst
    print(f"Dron seleccionado: {dron_asignado['codigo']}\n")

    print("--- Paso 6: Verificacion de ruta con BFS ---")
    existe_camino = bfs_verificar_camino(grafo, "Base", mision['zona'])
    if not existe_camino:
        print("No es posible llegar a la zona afectada. Mision cancelada.\n")
        return raiz_bst

    print("--- Paso 7: Calculo de la ruta minima con Dijkstra ---")
    ruta, distancia_total = dijkstra_ruta_minima(grafo, "Base", mision['zona'])


    print("--- Paso 8: Asignacion del dron ---")
    dron_asignado['estado'] = 'En mision'
    print(f"Dron '{dron_asignado['codigo']}' asignado a la mision '{mision['codigo']}'.\n")

    print("--- Paso 9: Actualizacion de estados ---")
    atender_mision(cola_pendientes)
    mision['estado'] = 'En curso'
    ruta_texto = ' -> '.join(ruta) if ruta else 'N/A'
    print(f"Mision '{mision['codigo']}' actualizada a estado 'En curso'.")
    print(f"Ruta asignada: {ruta_texto} | Distancia total: {distancia_total} km")

    print("\n" + "==================================" )
    print("SIMULACION DE RESCATE FINALIZADA")
    print("==================================" "\n")

    return raiz_bst
