# Este codigo implementa un algoritmo de transformación de cadenas utilizando un enfoque
# de fuerza bruta. El objetivo es transformar una cadena de caracteres de un estado inicial
# (origen) a un estado final (destino) mediante una serie de operaciones (avanzar, borrar,
# reemplazar, insertar y eliminar) que tienen costos asociados.
# version: 1.0


from .costos import COSTOS, calcular_costo_total


# Funciones para realizar las operaciones
def advance(cadena, posicion):
    if posicion < len(cadena):
        return cadena, posicion + 1, COSTOS['advance']
    return cadena, posicion, 0  # Sin costo si no hay avance

def delete(cadena, posicion):
    if posicion < len(cadena):
        nueva_cadena = cadena[:posicion] + cadena[posicion + 1:]
        return nueva_cadena, posicion, COSTOS['delete']
    return cadena, posicion, 0  # Sin costo si no hay eliminación

def replace(cadena, posicion, nuevo_char):
    if posicion < len(cadena):
        nueva_cadena = cadena[:posicion] + nuevo_char + cadena[posicion + 1:]
        return nueva_cadena, posicion + 1, COSTOS['replace']
    return cadena, posicion, 0  # Sin costo si no hay reemplazo

def insert(cadena, posicion, nuevo_char):
    nueva_cadena = cadena[:posicion] + nuevo_char + cadena[posicion:]
    return nueva_cadena, posicion + 1, COSTOS['insert']

def kill(cadena, posicion):
    if posicion < len(cadena):
        nueva_cadena = cadena[:posicion]
        return nueva_cadena, posicion, COSTOS['kill']
    return cadena, posicion, 0  # Sin costo si no hay eliminación

# Función para encontrar la mejor secuencia de transformación
def transformar_fuerza_bruta(origen, destino):
    mejor_costo = float('inf')
    mejor_secuencia = []
    
    def backtrack(actual, destino, posicion, costo_actual, secuencia):
        nonlocal mejor_costo, mejor_secuencia
        
        # Si hemos transformado la cadena actual a destino
        if actual == destino:
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                mejor_secuencia = secuencia.copy()
            return
        
        # Si el costo actual supera el mejor costo, salir
        if costo_actual >= mejor_costo:
            return
        
        # Intentar todas las operaciones
        if posicion < len(actual):
            # Advance
            nueva_cadena, nueva_pos, costo = advance(actual, posicion)
            backtrack(nueva_cadena, destino, nueva_pos, costo_actual + costo, secuencia + ['advance'])
            
            # Replace
            if posicion < len(destino):
                nueva_cadena, nueva_pos, costo = replace(actual, posicion, destino[posicion])
                backtrack(nueva_cadena, destino, nueva_pos, costo_actual + costo, secuencia + [f'replace with {destino[posicion]}'])
            # Delete
            nueva_cadena, nueva_pos, costo = delete(actual, posicion)
            backtrack(nueva_cadena, destino, nueva_pos, costo_actual + costo, secuencia + ['delete'])
            
            
            
            # Insert
            if posicion < len(destino):
                nueva_cadena, nueva_pos, costo = insert(actual, posicion, destino[posicion])
                backtrack(nueva_cadena, destino, nueva_pos, costo_actual + costo, secuencia + [f'insert {destino[posicion]}'])
            
            # Kill
            nueva_cadena, nueva_pos, costo = kill(actual, posicion)
            backtrack(nueva_cadena, destino, nueva_pos, costo_actual + costo, secuencia + ['kill'])
    
    backtrack(origen, destino, 0, 0, [])
    return mejor_costo, mejor_secuencia

# Función principal
if __name__ == "__main__":
    cadena_origen = "ingenioso"
    cadena_final = "ingeniero"

    costo_total, operaciones = transformar_fuerza_bruta(cadena_origen, cadena_final)
    resultado_final = calcular_costo_total(operaciones)
    print(f"Costo de la transformacion : {costo_total}")
    print(f"Costo total (5a + d + r + 4i + k): {resultado_final}")
    print(f"Mejor secuencia de operaciones:")
    print(f'Operaciones: {operaciones}')