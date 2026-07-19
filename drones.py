#Modulo de gestion de Drones

def registrar_dron(drones, codigo, modelo, velocidad, capacidad, bateria):
    dron = {
        'codigo': codigo,
        'modelo': modelo,
        'velocidad': velocidad,
        'capacidad': capacidad,
        'bateria': bateria,
        'estado': 'Disponible'
    }
    drones.append(dron)
    print(f"Dron '{codigo}' registrado correctamente.")
    return dron


def mostrar_drones(drones):
    if len(drones) == 0:
        print("No hay drones registrados.")
        return

    print("--- LISTA DE DRONES ---")
    for d in drones:
        print(f"Codigo: {d['codigo']} | Modelo: {d['modelo']} | "
              f"Velocidad: {d['velocidad']} km/h | Capacidad: {d['capacidad']} kg | "
              f"Bateria: {d['bateria']}% | Estado: {d['estado']}")


def eliminar_dron(drones, codigo):
    for i in range(len(drones)):
        if drones[i]['codigo'] == codigo:
            drones.pop(i)
            print(f"Dron '{codigo}' eliminado.")
            return
    print(f"No se encontro el dron '{codigo}'.")


def buscar_dron_disponible(drones):
    for dron in drones:
        if dron['estado'] == 'Disponible':
            return dron
    return None
