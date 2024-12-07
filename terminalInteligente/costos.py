# Este archivo contiene la función que calcula el costo total de las 
# operaciones realizadas en un texto.
# version: 1.0


def calcular_costo(operaciones, a, b, c, d, e):
    """
    Calcula el costo total de las operaciones realizadas en un texto.

    Args:
        operaciones (list): Lista de operaciones realizadas. Las operaciones pueden ser:
            'advance', 'delete', 'replace', 'insert', 'kill'.
        a (int): Costo de la operación 'advance'.
        b (int): Costo de la operación 'delete'.
        c (int): Costo de la operación 'replace'.
        d (int): Costo de la operación 'insert'.
        e (int): Costo de la operación 'kill'.

    Returns:
        int: El costo total de las operaciones.
    """
    costos = {
        'advance': a,
        'delete': b,
        'replace': c,
        'insert': d,
        'kill': e
    }

    costo_total = 0
    for op in operaciones:
        if op == 'advance':
            costo_total += costos['advance']
        elif op == 'delete':
            costo_total += costos['delete']
        elif op.startswith('replace'):
            costo_total += costos['replace']
        elif op.startswith('insert'):
            costo_total += costos['insert']
        elif op == 'kill':
            costo_total += costos['kill']
    return costo_total
