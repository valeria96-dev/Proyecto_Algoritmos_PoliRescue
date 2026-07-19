# Arbol
def crear_nodo(mision):
    return {
        'codigo': mision['codigo'],
        'mision': mision,
        'izquierda': None,
        'derecha': None
    }


def insertar_bst(raiz, mision):
    if raiz is None:
        return crear_nodo(mision)

    if mision['codigo'] < raiz['codigo']:
        raiz['izquierda'] = insertar_bst(raiz['izquierda'], mision)
    elif mision['codigo'] > raiz['codigo']:
        raiz['derecha'] = insertar_bst(raiz['derecha'], mision)
    else:
        print(f"La mision '{mision['codigo']}' ya existe en el arbol.")

    return raiz


def buscar_bst(raiz, codigo):
    if raiz is None:
        print("Recorrido finalizado: mision no encontrada.")
        return None

    print(f"Visitando nodo: {raiz['codigo']}")

    if codigo == raiz['codigo']:
        print("Encontrado")
        return raiz['mision']
    elif codigo < raiz['codigo']:
        return buscar_bst(raiz['izquierda'], codigo)
    else:
        return buscar_bst(raiz['derecha'], codigo)


def preorden(raiz):
    if raiz is None:
        return
    print(raiz['codigo'], end=" ")
    preorden(raiz['izquierda'])
    preorden(raiz['derecha'])


def inorden(raiz):
    if raiz is None:
        return
    inorden(raiz['izquierda'])
    print(raiz['codigo'], end=" ")
    inorden(raiz['derecha'])


def postorden(raiz):
    if raiz is None:
        return
    postorden(raiz['izquierda'])
    postorden(raiz['derecha'])
    print(raiz['codigo'], end=" ")
