
def registrar_zona(grafo, zona):
    if zona not in grafo:
        grafo[zona] = []
        print(f"Zona '{zona}' registrada.")
    else:
        print(f"La zona '{zona}' ya existe.")


def registrar_ruta(grafo, zona1, zona2, distancia):
    if zona1 not in grafo:
        registrar_zona(grafo, zona1)
    if zona2 not in grafo:
        registrar_zona(grafo, zona2)

    grafo[zona1].append((zona2, distancia))
    grafo[zona2].append((zona1, distancia))
    print(f"Ruta registrada: {zona1} <----{distancia}km----> {zona2}")


def mostrar_grafo(grafo):

    if len(grafo) == 0:
        print("No hay zonas registradas.")
        return

    print("--- MAPA DE ZONAS ---")
    for zona in grafo:
        conexiones = ""
        for vecino, distancia in grafo[zona]:
            conexiones = conexiones + f"{vecino}({distancia}km) "
        if conexiones == "":
            conexiones = "sin conexiones"
        print(f"{zona} -> {conexiones}")


def eliminar_zona(grafo, zona):
    if zona not in grafo:
        print(f"No se encontro la zona '{zona}'.")
        return

    del grafo[zona]
    for z in grafo:
        nueva_lista = []
        for vecino, distancia in grafo[z]:
            if vecino != zona:
                nueva_lista.append((vecino, distancia))
        grafo[z] = nueva_lista
    print(f"Zona '{zona}' eliminada junto con sus conexiones.")
