# PoliRescue — Sistema de Gestión de Misiones de Rescate con Drones

Proyecto final del curso de **Algoritmos y Estructuras de Datos**. Simula un sistema de gestión de emergencias (terremotos, incendios, inundaciones, deslizamientos) para la empresa ficticia **PoliRescue Technologies**, que organiza misiones, asigna drones y calcula rutas mínimas hacia las zonas afectadas.

## Descripción

El sistema permite registrar drones, misiones y zonas, y aplica sobre esos datos los algoritmos de ordenamiento, búsqueda, colas, árboles binarios de búsqueda y grafos vistos durante el semestre. Todos los algoritmos están **implementados manualmente**, sin usar `sort()`, `sorted()` ni `index()`.

## Funcionalidades

- **Registro de información**: alta, consulta y eliminación de drones, misiones y zonas.
- **Ordenamiento**: burbuja (prioridad), inserción (batería), mergesort (velocidad) y quicksort (distancia).
- **Búsqueda**: lineal (drones y misiones) y binaria (drones por código).
- **Cola FIFO**: gestión de misiones pendientes.
- **Árbol Binario de Búsqueda (BST)**: organización de misiones por código, con recorridos preorden, inorden y postorden.
- **Grafo de zonas**: verificación de caminos con BFS y cálculo de rutas mínimas con Dijkstra.
- **Simulación completa de rescate**: ejecuta automáticamente el flujo de 9 pasos ante una nueva emergencia.

## Estructura del proyecto

\`\`\`
PoliRescue_Proyecto/
├── main.py                 # Punto de entrada; menú interactivo
├── drones.py                # Registro y gestión de drones
├── misiones.py               # Registro y gestión de misiones
├── zonas.py                  # Grafo de zonas y rutas
├── cola_misiones.py           # Cola FIFO de misiones pendientes
├── arbol_bst.py               # Árbol Binario de Búsqueda
├── ordenamientos.py            # Burbuja, inserción, mergesort, quicksort
├── busquedas.py                 # Búsqueda lineal y binaria
├── grafo_algoritmos.py          # BFS y Dijkstra
└── simulacion.py                 # Simulación completa de rescate
\`\`\`

## Requisitos

- Python
- No requiere librerías externas (solo usa `heapq`, incluido en la librería estándar de Python)

## Cómo ejecutar

\`\`\`bash
git clone https://github.com/valeria96-dev/Proyecto_Algoritmos_PoliRescue.git
cd tu-repositorio
python3 main.py
\`\`\`

Al iniciar, el sistema carga datos de ejemplo (drones, zonas y misiones) para poder probarlo de inmediato.

## Menú principal

| Opción | Función |
|---|---|
| 1 | Registro de información (drones, misiones, zonas) |
| 2 | Organización de misiones (ordenamientos) |
| 3 | Algoritmos de búsqueda |
| 4 | Cola de misiones |
| 5 | Árbol Binario de Búsqueda (BST) |
| 6 | Grafo de zonas (BFS y Dijkstra) |
| 7 | Simulación completa de rescate |
| 0 | Salir |

## Tecnologías

- **Lenguaje:** Python 3
- **Estructuras de datos:** listas, diccionarios, colas, árboles binarios y grafos
- **Librería estándar utilizada:** `heapq` (cola de prioridad para Dijkstra)

## Autores

- Jaime Cusco
- Emily Paguanquiza
- Sheccid Verdezoto
## Licencia

Proyecto académico, de uso educativo.