from terminalInteligente.dinamica import calcular_solucion_optima
from terminalInteligente.voraz import algoritmo_voraz
from terminalInteligente.bruta import transformar_fuerza_bruta
from terminalInteligente.costos import calcular_costo_total


def ejecutar_ejemplos():
    print("Ejecutando terminal inteligente...")
    ejemplos = [
        ("algorithm", "altruistic"),
        ("ingenioso", "ingeniero"),
        ("francesa", "ancestro"),
    ]

    output = ""  # Variable para acumular el contenido

    for origen, destino in ejemplos:
        # Fuerza Bruta
        secuencia_bruta = []
        
        costo_bruta, secuencia_bruta = transformar_fuerza_bruta(origen, destino)
        
        # Calcular el costo total usando las operaciones devueltas
        costo_total_bruta = calcular_costo_total(secuencia_bruta)
        output += "----------------------FUERZA BRUTA----------------------\n"
        output += f"Fuerza Bruta - Transformar '{origen}' en '{destino}':\n"
        output += f"Costo total: {costo_total_bruta}\n"
        output += f"Mejor secuencia de operaciones: {secuencia_bruta}\n\n"
 
        # Programación Dinámica
        output += "----------------------PROGRAMACION DINAMICA----------------------\n"
        costo_dinamica, operaciones_dinamica, matriz = calcular_solucion_optima(origen, destino)
        
        output += f"Programación Dinámica - Transformar '{origen}' en '{destino}':\n"
        output += f"Costo total: {costo_dinamica}\n"
        output += f"Secuencia de operaciones: {operaciones_dinamica}\n\n"
        output += f"Matriz de costos (dp)\n"
        for fila in matriz:
            output += f"{fila}\n\n"
            
        
        # Programación Voraz
        output += "----------------------PROGRAMACION VORAZ----------------------\n"
        costo_voraz, operaciones_voraz = algoritmo_voraz(origen, destino)
        output += f"Programación Voraz - Transformar '{origen}' en '{destino}':\n"
        output += f"Costo total: {costo_voraz}\n"
        output += f"Secuencia de operaciones: {operaciones_voraz}\n\n"

    return output  # Retornar todo el contenido acumulado

ejecutar_ejemplos()