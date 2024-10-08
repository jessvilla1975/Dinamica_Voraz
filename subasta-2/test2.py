# Archivo de prueba para las implementaciones del problema de la subasta pública: fuerza bruta, voraz y programación dinámica

from fuerzabruta import subasta_fuerzabruta
from voraz import subasta_voraz
from dinamica import subasta_dinamica

def probar_enfoques(A, ofertas, oferta_gobierno):
    """
    Realiza pruebas comparativas entre la solución de fuerza bruta, la solución voraz y la solución con programación dinámica.
    """
    print("\nPrueba del Enfoque Fuerza Bruta con ofertas2:")
    mejor_asignacion_fuerzabruta, mejor_vr_fuerzabruta = subasta_fuerzabruta(A, ofertas2, oferta_gobierno)
    print(f"Asignación fuerza bruta (ofertas2): {mejor_asignacion_fuerzabruta}")
    print(f"Valor total (vr) fuerza bruta (ofertas2): {mejor_vr_fuerzabruta}")

    print("\nPrueba del Enfoque Voraz:")
    mejor_asignacion_voraz, mejor_vr_voraz, ofertas_ordenadas = subasta_voraz(A, ofertas, oferta_gobierno)
    print(f"Asignación voraz: {mejor_asignacion_voraz}")
    print(f"Valor total (vr) voraz: {mejor_vr_voraz}")

    print("\nPrueba del Enfoque con Programación Dinámica:")
    asignaciones_optimas, valor_maximo = subasta_dinamica(A, ofertas, oferta_gobierno)
    print("Asignaciones programación dinámica:")
    for idx, (asignacion, oferta) in enumerate(zip(asignaciones_optimas[:-1], ofertas)):
        print(f"  Oferente {idx+1} (Precio: {oferta[0]}, Mín: {oferta[1]}, Máx: {oferta[2]}): {asignacion} acciones")
    print(f"  Gobierno (Precio: {oferta_gobierno[0]}): {asignaciones_optimas[-1]} acciones")
    print(f"Valor máximo (vr): {valor_maximo}")

# Datos de entrada
A = 1000  # Total de acciones
ofertas = [
    (500, 100, 600),
    (450, 100, 400),
    (400, 100, 400),
    (200, 50, 200)
]
ofertas2 = [
    (500, 100, 600),  # <precio por acción, mínimo de acciones, máximo de acciones>
    (450, 400, 800)
]
oferta_gobierno = (100, 0, A)  # Oferta del gobierno

if __name__ == "__main__":
    
    # Realizar las pruebas con el conjunto original de ofertas
    probar_enfoques(A, ofertas, oferta_gobierno)