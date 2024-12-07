# descripcion: Este archivo contiene la implementación de la solución óptima para el 
# problema de transformación de cadenas de texto. Se utiliza programación dinámica
# para encontrar la secuencia de operaciones que minimiza el costo total de transformación. 
# version: 2.0

from .costos import calcular_costo

def calcular_solucion_optima(origen, destino, a, b, c, d, e):
    """
    Calcula la solución óptima para transformar una cadena en otra con el menor costo posible.

    Args:
        origen (str): Cadena de texto original.
        destino (str): Cadena de texto objetivo.
        a (int): Costo de la operación 'advance'.
        b (int): Costo de la operación 'delete'.
        c (int): Costo de la operación 'replace'.
        d (int): Costo de la operación 'insert'.
        e (int): Costo de la operación 'kill'.

    Returns:
        tuple: (costo total, lista de operaciones, matriz de costos)
    """
    m, n = len(origen), len(destino)
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    operations = [[None] * (n + 1) for _ in range(m + 1)]  # Para almacenar las operaciones

    # Inicializar la matriz dp
    dp[0][0] = 0
    operations[0][0] = []
    for i in range(1, m + 1):  # Inicializar la primera columna
        dp[i][0] = dp[i - 1][0] + b  # Costo de eliminar
        operations[i][0] = operations[i - 1][0] + ['delete']  # Operación de eliminar

    for j in range(1, n + 1):  # Inicializar la primera fila
        dp[0][j] = dp[0][j - 1] + d  # Costo de insertar
        operations[0][j] = operations[0][j - 1] + [f'insert {destino[j-1]}']  # Operación de insertar

    # Llenar la matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if origen[i - 1] == destino[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a
                operations[i][j] = operations[i - 1][j - 1] + ['advance']
                print(f"dp[{i}][{j}] = {dp[i][j]} (advance)")
            else:
                # Reemplazar
                if dp[i][j] > dp[i - 1][j - 1] + c:
                    dp[i][j] = dp[i - 1][j - 1] + c
                    operations[i][j] = operations[i - 1][j - 1] + [f'replace with {destino[j-1]}']
                    print(f"dp[{i}][{j}] = {dp[i][j]} (replace)")
                # Insertar
                if dp[i][j] > dp[i][j - 1] + d:
                    dp[i][j] = dp[i][j - 1] + d
                    operations[i][j] = operations[i][j - 1] + [f'insert {destino[j-1]}']
                    print(f"dp[{i}][{j}] = {dp[i][j]} (insert)")

                # Eliminar
                if dp[i][j] > dp[i - 1][j] + b:
                    dp[i][j] = dp[i - 1][j] + b
                    operations[i][j] = operations[i - 1][j] + ['delete']
                    print(f"dp[{i}][{j}] = {dp[i][j]} (delete)")

            # Considerar la operación "kill"
            for k in range(i):
                if dp[i][j] > dp[k][j] + e:
                    dp[i][j] = dp[k][j] + e
                    operations[i][j] = operations[k][j] + ['kill']
                    print(f"dp[{i}][{j}] = {dp[i][j]} (kill)")

    # Calcular el costo total de las operaciones
    costo = calcular_costo(operations[m][n], a, b, c, d, e)
    print("Costo de la transformación: ", costo)  # Aquí tengo el costo de las operaciones

    return costo, operations[m][n], dp  # Retorna el costo y la lista de operaciones


def imprimirmatriz(matriz):
    for fila in matriz:
        print(fila)


# Pruebas
if __name__ == '__main__':
    origen = 'ingenioso'
    destino = 'ingeniero'
    # Valores de costos personalizados
    costos = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}

    costo, operaciones, m = calcular_solucion_optima(
        origen, destino,
        a=costos['advance'],
        b=costos['delete'],
        c=costos['replace'],
        d=costos['insert'],
        e=costos['kill']
    )
    print(f'Costo total: {costo}')
    print(f"Mejor secuencia de operaciones:")
    print(f'Operaciones: {operaciones}')
    imprimirmatriz(m)
