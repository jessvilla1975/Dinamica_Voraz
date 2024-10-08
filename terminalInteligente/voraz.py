# descripcion: Este archivo contiene la implementación de la solución voraz para el
# problema de terminal inteligente. El algoritmo voraz se basa en tomar la mejor
# decisión en cada paso, sin considerar las consecuencias a largo plazo. En este caso,
# el algoritmo voraz se enfoca en minimizar el costo total de transformar una cadena
# de texto `origen` en otra cadena `destino` mediante una serie de operaciones (avanzar,
# borrar, reemplazar, insertar y eliminar) que tienen costos específicos asociados.
# version: 1.0

from costos import COSTOS, calcular_costo_total, calcular_costo

def algoritmo_voraz(x, y, costos=COSTOS):
    m, n = len(x), len(y)
    i, j = 0, 0
    operaciones = []
    costo_total = 0
    
    while i < m or j < n:
        if i < m and j < n and x[i] == y[j]:
            # Si los caracteres coinciden, avanzamos
            operaciones.append('advance')
            costo_total += costos['advance']
            i += 1
            j += 1
        elif i < m and j < n:
            # Si no coinciden, hacemos un reemplazo
            operaciones.append(f'replace {x[i]} with {y[j]}')
            costo_total += costos['replace']
            i += 1
            j += 1
        elif i < m:
            # Si hay más caracteres en x, eliminamos
            operaciones.append(f'delete {x[i]}')
            costo_total += costos['delete']
            i += 1
        elif j < n:
            # Si hay más caracteres en y, insertamos
            operaciones.append(f'insert {y[j]}')
            costo_total += costos['insert']
            j += 1

    return costo_total, operaciones

# Usamos las cadenas dadas
if __name__ == '__main__':
    cadena_origen = "algorithm"
    cadena_final = "altruistic"
    
    # Llamar al algoritmo voraz
    costo, operaciones = algoritmo_voraz(cadena_origen, cadena_final, COSTOS)
    
    # Imprimir el costo y la secuencia de operaciones
    print(f'Costo total (5a + d + r + 4i + k): {costo}')
    print(f"Mejor secuencia de operaciones:")
    print(f'Operaciones: {operaciones}')