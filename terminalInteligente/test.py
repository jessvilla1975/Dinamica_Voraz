from fuerza_bruta import transformar_fuerza_bruta
from dinamica import calcular_solucion_optima
from costos import calcular_costo_total

def ejecutar_ejemplos():
    ejemplos = [
        ("algorithm", "altruistic"),
        ("ingenioso", "ingeniero"),
        ("francesa", "ancestro"),
    ]

    for origen, destino in ejemplos:
        # Fuerza Bruta
        secuencia_bruta = []
        costo_bruta, secuencia_bruta = transformar_fuerza_bruta(origen, destino)
        
        # Calcular el costo total usando las operaciones devueltas
        costo_total_bruta = calcular_costo_total(secuencia_bruta)

        print(f"Fuerza Bruta - Transformar '{origen}' en '{destino}':")
        print(f"Costo total: {costo_total_bruta}")
        print(f"Mejor secuencia de operaciones: {secuencia_bruta}")
        print('-' * 40)

        # Programación Dinámica
        costo_dinamica, operaciones_dinamica = calcular_solucion_optima(origen, destino)
        print(f"Programación Dinámica - Transformar '{origen}' en '{destino}':")
        print(f"Costo total: {costo_dinamica}")
        print(f"Secuencia de operaciones: {operaciones_dinamica}")
        print('-' * 40)

if __name__ == "__main__":
    ejecutar_ejemplos()
