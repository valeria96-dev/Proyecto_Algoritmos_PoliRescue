

from drones import registrar_dron, mostrar_drones, eliminar_dron
from misiones import registrar_mision, mostrar_misiones, eliminar_mision
from zonas import registrar_zona, registrar_ruta, mostrar_grafo, eliminar_zona
from cola_misiones import agregar_mision_cola, atender_mision, mostrar_siguiente_mision, mostrar_cola
from arbol_bst import insertar_bst, buscar_bst, preorden, inorden, postorden
from ordenamientos import (ordenar_burbuja_prioridad, ordenar_insercion_bateria,
                            merge_sort_velocidad, quick_sort_distancia)
from busquedas import busqueda_lineal, busqueda_binaria
from grafo_algoritmos import bfs_verificar_camino, dijkstra_ruta_minima
from simulacion import simular_rescate

# ESTRUCTURAS PRINCIPALES DEL SISTEMA
drones = []
misiones = []
grafo = {}
cola_pendientes = []
raiz_bst = None


def cargar_datos_de_ejemplo():

    global raiz_bst

    print("Cargando datos de ejemplo...\n")

    # Drones
    registrar_dron(drones, "D01", "Phantom X1", 60, 5, 90)
    registrar_dron(drones, "D02", "SkyHawk", 80, 3, 45)
    registrar_dron(drones, "D03", "Aguila V2", 50, 8, 70)
    registrar_dron(drones, "D04", "RescueBot", 70, 6, 20)

    # Zonas y rutas (grafo)
    registrar_ruta(grafo, "Base", "Hospital", 4)
    registrar_ruta(grafo, "Base", "Parque", 3)
    registrar_ruta(grafo, "Hospital", "Escuela", 5)
    registrar_ruta(grafo, "Escuela", "Zona Roja", 2)
    registrar_ruta(grafo, "Parque", "Zona Roja", 6)

    # Misiones iniciales
    m1 = registrar_mision(misiones, "M001", "Hospital", "Incendio", 2, 15, 4)
    m2 = registrar_mision(misiones, "M002", "Escuela", "Inundacion", 1, 30, 9)
    m3 = registrar_mision(misiones, "M003", "Zona Roja", "Terremoto", 3, 50, 11)

    for m in (m1, m2, m3):
        agregar_mision_cola(cola_pendientes, m)
        raiz_bst = insertar_bst(raiz_bst, m)

    print("\nDatos de ejemplo cargados correctamente.\n")



def menu_registro():
    print("\n--- REGISTRO DE INFORMACION ---")
    print("1. Registrar dron")
    print("2. Mostrar drones")
    print("3. Eliminar dron")
    print("4. Registrar mision")
    print("5. Mostrar misiones")
    print("6. Eliminar mision")
    print("7. Registrar zona")
    print("8. Registrar ruta entre zonas")
    print("9. Mostrar mapa de zonas")
    print("10. Eliminar zona")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        codigo = input("Codigo del dron: ")
        modelo = input("Modelo: ")
        velocidad = int(input("Velocidad (km/h): "))
        capacidad = float(input("Capacidad (kg): "))
        bateria = int(input("Bateria (%): "))
        registrar_dron(drones, codigo, modelo, velocidad, capacidad, bateria)
    elif opcion == "2":
        mostrar_drones(drones)
    elif opcion == "3":
        codigo = input("Codigo del dron a eliminar: ")
        eliminar_dron(drones, codigo)
    elif opcion == "4":
        codigo = input("Codigo de la mision: ")
        zona = input("Zona: ")
        tipo = input("Tipo de emergencia: ")
        prioridad = int(input("Prioridad (1 = critica, 2 = alta, 3 = media, 4 = baja): "))
        afectados = int(input("Personas afectadas: "))
        distancia = float(input("Distancia (km): "))
        registrar_mision(misiones, codigo, zona, tipo, prioridad, afectados, distancia)
    elif opcion == "5":
        mostrar_misiones(misiones)
    elif opcion == "6":
        codigo = input("Codigo de la mision a eliminar: ")
        eliminar_mision(misiones, codigo)
    elif opcion == "7":
        zona = input("Nombre de la zona: ")
        registrar_zona(grafo, zona)
    elif opcion == "8":
        zona1 = input("Zona 1: ")
        zona2 = input("Zona 2: ")
        distancia = float(input("Distancia (km): "))
        registrar_ruta(grafo, zona1, zona2, distancia)
    elif opcion == "9":
        mostrar_grafo(grafo)
    elif opcion == "10":
        zona = input("Zona a eliminar: ")
        eliminar_zona(grafo, zona)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_ordenamientos():
    print("\n--- ORGANIZACION DE MISIONES ---")
    print("1. Burbuja: ordenar misiones por prioridad")
    print("2. Insercion: ordenar drones por bateria")
    print("3. MergeSort: ordenar drones por velocidad")
    print("4. QuickSort: ordenar misiones por distancia")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        ordenar_burbuja_prioridad(misiones)
    elif opcion == "2":
        ordenar_insercion_bateria(drones)
    elif opcion == "3":
        resultado = merge_sort_velocidad(drones)
        drones[:] = resultado
    elif opcion == "4":
        quick_sort_distancia(misiones)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_busquedas():
    print("\n--- ALGORITMOS DE BUSQUEDA ---")
    print("1. Busqueda lineal de dron")
    print("2. Busqueda lineal de mision")
    print("3. Busqueda binaria de dron (por codigo)")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        codigo = input("Codigo del dron a buscar: ")
        busqueda_lineal(drones, codigo, "dron")
    elif opcion == "2":
        codigo = input("Codigo de la mision a buscar: ")
        busqueda_lineal(misiones, codigo, "mision")
    elif opcion == "3":
        codigo = input("Codigo del dron a buscar: ")
        busqueda_binaria(drones, codigo)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_cola():
    print("\n--- COLA DE MISIONES PENDIENTES ---")
    print("1. Mostrar cola")
    print("2. Mostrar siguiente mision")
    print("3. Atender mision")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        mostrar_cola(cola_pendientes)
    elif opcion == "2":
        mostrar_siguiente_mision(cola_pendientes)
    elif opcion == "3":
        atender_mision(cola_pendientes)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_arbol():
    global raiz_bst
    print("\n--- ARBOL BINARIO DE BUSQUEDA (BST) ---")
    print("1. Buscar mision por codigo")
    print("2. Mostrar recorrido Preorden")
    print("3. Mostrar recorrido Inorden")
    print("4. Mostrar recorrido Postorden")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        codigo = input("Codigo de la mision a buscar: ")
        buscar_bst(raiz_bst, codigo)
    elif opcion == "2":
        print("Preorden:", end=" ")
        preorden(raiz_bst)
        print()
    elif opcion == "3":
        print("Inorden:", end=" ")
        inorden(raiz_bst)
        print()
    elif opcion == "4":
        print("Postorden:", end=" ")
        postorden(raiz_bst)
        print()
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_grafo():
    print("\n--- BFS Y DIJKSTRA ---")
    print("1. Verificar camino (BFS)")
    print("2. Calcular ruta minima (Dijkstra)")
    print("0. Volver")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        destino = input("Zona afectada (destino): ")
        bfs_verificar_camino(grafo, "Base", destino)
    elif opcion == "2":
        destino = input("Zona afectada (destino): ")
        if bfs_verificar_camino(grafo, "Base", destino):
            dijkstra_ruta_minima(grafo, "Base", destino)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def menu_simulacion():
    global raiz_bst
    print("\n--- SIMULACION COMPLETA DE RESCATE ---")
    codigo = input("Codigo de la nueva mision: ")
    zona = input("Zona afectada: ")
    tipo = input("Tipo de emergencia: ")
    prioridad = int(input("Prioridad (1 = mas urgente): "))
    afectados = int(input("Personas afectadas: "))
    distancia = float(input("Distancia estimada (km): "))

    datos_mision = {
        'codigo': codigo, 'zona': zona, 'tipo_emergencia': tipo,
        'prioridad': prioridad, 'personas_afectadas': afectados, 'distancia': distancia
    }

    raiz_bst = simular_rescate(drones, misiones, cola_pendientes, raiz_bst, grafo, datos_mision)


# ---------------------------------------------------------
# MENU PRINCIPAL
# ---------------------------------------------------------
def menu_principal():
    while True:
        print("\n" + "=" * 45)
        print(" SISTEMA DE GESTION DE RESCATE - PoliRescue")
        print("=" * 45)
        print("1. Registro de informacion (drones, misiones, zonas)")
        print("2. Organizacion de misiones (ordenamientos)")
        print("3. Algoritmos de busqueda")
        print("4. Cola de misiones")
        print("5. Arbol Binario de Busqueda (BST)")
        print("6. Grafo de zonas (BFS y Dijkstra)")
        print("7. Simulacion completa de rescate")
        print("0. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_ordenamientos()
        elif opcion == "3":
            menu_busquedas()
        elif opcion == "4":
            menu_cola()
        elif opcion == "5":
            menu_arbol()
        elif opcion == "6":
            menu_grafo()
        elif opcion == "7":
            menu_simulacion()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    cargar_datos_de_ejemplo()
    menu_principal()
