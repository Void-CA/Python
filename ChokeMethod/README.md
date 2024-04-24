# Resolvedor del Método de Choque de Programación Lineal

Este script Python (`solver.py`) permite resolver un problema de Programación Lineal utilizando el Método de Choque. Es útil para optimizar recursos y tiempos en proyectos que involucran tareas con diferentes condiciones y restricciones.

## Requisitos
- Python 3.x
- Pandas (instalable con `pip install pandas`)

## Uso
1. Descarga los archivos `helper.py`, `solver.py`, `table.csv` y `net.csv` en tu sistema.
2. Prepara tus datos en dos archivos CSV:
   - `table.csv`: Contiene la información de las tareas, incluyendo los tiempos normales y de choque, así como los costos normales y de choque.
     - Formato: TAREA, T_NORMAL, C_NORMAL, T_CHOQUE, C_CHOQUE
   - `net.csv`: Contiene la información de la red de tareas, especificando las conexiones entre nodos.
     - Formato: ORIGEN, DESTINO, TAREA
3. Importa la clase `Problema` desde `solver.py` y crea una instancia pasando los nombres de los archivos CSV como parámetros:

   ```python
   from helper import Problema

   # Crea una instancia del problema
   problema = Problema(finalizacion_del_proyecto, 'table.csv', 'net.csv')

Utiliza los métodos proporcionados por la clase Problema para resolver el problema y obtener información relevante:

- `calcular_cuch()`: Calcula los coeficientes del método de choque.
- `print_min_function()`: Imprime la función objetivo.
- `print_limit_constraints()`: Imprime las restricciones de límite.
- `print_net_constraints()`: Imprime las restricciones de red.
- `print_no_negativity_constraints()`: Imprime las restricciones de no negatividad.

Ejecuta el script `solver.py` y analiza los resultados obtenidos.

## Recomendación
Se recomienda el uso de Excel para la preparación de los archivos CSV, ya que proporciona una interfaz intuitiva para editar y gestionar datos tabulares.

## Contribuciones
Si encuentras algún problema o deseas contribuir con mejoras, no dudes en abrir un issue o una pull request en el repositorio del proyecto en GitHub.
