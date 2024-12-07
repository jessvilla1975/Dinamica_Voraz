
from .costos import calcular_costo

def algoritmo_voraz(x, y, a, b, c, d):
    """
    Implementa el algoritmo voraz para transformar la cadena `x` en la cadena `y`
    utilizando una serie de operaciones (avanzar, borrar, reemplazar, insertar) con costos asociados.

    Args:
        x (str): Cadena de texto origen.
        y (str): Cadena de texto destino.
        a (int): Costo de la operación 'advance'.
        b (int): Costo de la operación 'delete'.
        c (int): Costo de la operación 'replace'.
        d (int): Costo de la operación 'insert'.

    Returns:
        tuple: (costo total, lista de operaciones)
    """
    m, n = len(x), len(y)
    i, j = 0, 0
    operaciones = []
    costo_total = 0
    
    while i < m or j < n:
        if i < m and j < n and x[i] == y[j]:
            # Si los caracteres coinciden, avanzamos
            operaciones.append('advance')
            costo_total += a
            i += 1
            j += 1
        elif i < m and j < n:
            # Si no coinciden, hacemos un reemplazo
            operaciones.append(f'replace {x[i]} with {y[j]}')
            costo_total += c
            i += 1
            j += 1
        elif i < m:
            # Si hay más caracteres en x, eliminamos
            operaciones.append(f'delete {x[i]}')
            costo_total += b
            i += 1
        elif j < n:
            # Si hay más caracteres en y, insertamos
            operaciones.append(f'insert {y[j]}')
            costo_total += d
            j += 1

    return costo_total, operaciones

# Usamos las cadenas dadas
if __name__ == '__main__':
    cadena_origen = "algorithm"
    cadena_final = "altruistic"
    
    # Definir los costos
    costos = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2}

    # Llamar al algoritmo voraz
    costo, operaciones = algoritmo_voraz(
        cadena_origen, cadena_final,
        a=costos['advance'],
        b=costos['delete'],
        c=costos['replace'],
        d=costos['insert']
    )
    
    # Imprimir el costo y la secuencia de operaciones
    print(f'Costo total: {costo}')
    print(f"Mejor secuencia de operaciones:")
    print(f'Operaciones: {operaciones}')
