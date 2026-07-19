#Modulo de gestion de Misiones

def registrar_mision(misiones, codigo, zona, tipo_emergencia, prioridad, personas_afectadas, distancia):

    mision = {
        'codigo': codigo,
        'zona': zona,
        'tipo_emergencia': tipo_emergencia,
        'prioridad': prioridad,
        'personas_afectadas': personas_afectadas,
        'distancia': distancia,
        'estado': 'Pendiente'
    }
    misiones.append(mision)
    print(f"Mision '{codigo}' registrada en la zona '{zona}' ({tipo_emergencia}).")
    return mision


def mostrar_misiones(misiones):
    if len(misiones) == 0:
        print("No hay misiones registradas.")
        return

    print("--- LISTA DE MISIONES ---")
    for m in misiones:
        print(f"Codigo: {m['codigo']} | Zona: {m['zona']} | Emergencia: {m['tipo_emergencia']} | "
              f"Prioridad: {m['prioridad']} | Afectados: {m['personas_afectadas']} | "
              f"Distancia: {m['distancia']} km | Estado: {m['estado']}")


def eliminar_mision(misiones, codigo):
    for i in range(len(misiones)):
        if misiones[i]['codigo'] == codigo:
            misiones.pop(i)
            print(f"Mision '{codigo}' eliminada.")
            return
    print(f"No se encontro la mision '{codigo}'.")
