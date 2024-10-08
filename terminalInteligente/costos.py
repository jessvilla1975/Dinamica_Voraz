# Este archivo contiene la función que calcula el costo total de las 
# operaciones realizadas en un texto.
# version: 1.0
COSTOS = {
    'advance': 1,
    'delete': 2,
    'replace': 3,
    'insert': 2,
    'kill': 1
}

def calcular_costo_total(operaciones):
    costo = 0
    for op in operaciones:
        if op == 'advance':
            costo += 5 * COSTOS['advance']
        elif op == 'delete':
            costo += COSTOS['delete']
        elif op.startswith('replace'):
            costo += COSTOS['replace']
        elif op.startswith('insert'):
            costo += 4 * COSTOS['insert']
        elif op == 'kill':
            costo += COSTOS['kill']
    return costo


def calcular_costo(operaciones):
    costo = 0
    for op in operaciones:
        if op == 'advance':
            costo += COSTOS['advance']
        elif op == 'delete':
            costo += COSTOS['delete']
        elif op.startswith('replace'):
            costo += COSTOS['replace']
        elif op.startswith('insert'):
            costo += COSTOS['insert']
        elif op == 'kill':
            costo += COSTOS['kill']
    return costo