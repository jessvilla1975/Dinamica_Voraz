# descripcion: Este archivo contiene la implementación de la solución óptima para el 
# problema de terminal inteligente
# La función `calcular_solucion_optima` utiliza un enfoque de programación dinámica 
# para determinar el costo mínimo de transformar una cadena de texto `origen` en otra 
# cadena `destino` mediante una serie de operaciones (avanzar, borrar, reemplazar, 
# insertar y eliminar) que tienen costos específicos asociados.
# Dado que el costo de reemplazo (3 unidades) es menor que la suma del costo de
# insertar (4 unidades) y borrar (2 unidades) (que da un total de 6 unidades), se 
# da prioridad a la operación de reemplazo cuando los caracteres de las cadenas 
# no coinciden. Esto se traduce en una estrategia más eficiente para minimizar 
# el costo total de la transformación.
# version: 2.0

from costos import COSTOS, calcular_costo

def calcular_solucion_optima(origen, destino):
    m, n = len(origen), len(destino)
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    operations = [[None] * (n + 1) for _ in range(m + 1)]  # Para almacenar las operaciones
    
    # Inicialización
    for i in range(m + 1):
        dp[i][0] = i * COSTOS['delete']
        operations[i][0] = ['delete'] * i  # Al eliminar, las operaciones son solo deletes
    for j in range(n + 1):
        dp[0][j] = j * 4 * COSTOS['insert']
        operations[0][j] = ['insert'] * j  # Al insertar, las operaciones son solo inserts
    
    # Llenar la matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if origen[i - 1] == destino[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 5 * COSTOS['advance']
                operations[i][j] = operations[i - 1][j - 1] + ['advance']
            else:
                # Reemplazar
                if dp[i][j] > dp[i - 1][j - 1] + COSTOS['replace']:
                    dp[i][j] = dp[i - 1][j - 1] + COSTOS['replace']
                    operations[i][j] = operations[i - 1][j - 1] + [f'replace with {destino[j-1]}']

                # Insertar
                if dp[i][j] > dp[i][j - 1] + 4 * COSTOS['insert']:
                    dp[i][j] = dp[i][j - 1] + 4 * COSTOS['insert']
                    operations[i][j] = operations[i][j - 1] + [f'insert {destino[j-1]}']

                # Eliminar
                if dp[i][j] > dp[i - 1][j] + COSTOS['delete']:
                    dp[i][j] = dp[i - 1][j] + COSTOS['delete']
                    operations[i][j] = operations[i - 1][j] + ['delete']

            # Considerar la operación "kill"
            for k in range(i):
                if dp[i][j] > dp[k][j] + COSTOS['kill']:
                    dp[i][j] = dp[k][j] + COSTOS['kill']
                    operations[i][j] = operations[k][j] + ['kill']
    
    # Imprimir la matriz dp
    print("Matriz de costos (dp)")
    for fila in dp:
        print(fila)
        
    #imprimir el costo dp
    costo = calcular_costo(operations[m][n]) 
    #print("Costo de la transformacion: ", costo) # Aqui tengo el costo de las operaciones

    return dp[m][n], operations[m][n]  # Retorna el costo y la lista de operaciones


# Pruebas
if __name__ == '__main__':
    origen = 'ingenioso'
    destino = 'ingeniero'
    costo, operaciones = calcular_solucion_optima(origen, destino)
    print(f'Costo total (5a + d + r + 4i + k): {costo}')
    print(f"Mejor secuencia de operaciones:")
    print(f'Operaciones: {operaciones}')

