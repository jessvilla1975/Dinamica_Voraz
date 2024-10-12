# Archivo de prueba para las implementaciones del problema de la subasta pública: fuerza bruta, voraz y programación dinámica

from subasta.fuerzabruta import subasta_fuerzabruta
from subasta.voraz import subasta_voraz
from subasta.dinamica import subasta_dinamica

def probar_enfoques(A, ofertas, oferta_gobierno):
    output = ""  # Variable para acumular el contenido
    """
    Realiza pruebas comparativas entre la solución de fuerza bruta, la solución voraz y la solución con programación dinámica.
    """
    output +="\nPrueba del Enfoque Fuerza Bruta con ofertas2: \n"
    mejor_asignacion_fuerzabruta, mejor_vr_fuerzabruta = subasta_fuerzabruta(A, ofertas2, oferta_gobierno)
    output += f"Asignación fuerza bruta (ofertas2): {mejor_asignacion_fuerzabruta} \n"
    output += f"Valor total (vr) fuerza bruta (ofertas2): {mejor_vr_fuerzabruta} \n"

    output +="\nPrueba del Enfoque Voraz: \n"
    mejor_asignacion_voraz, mejor_vr_voraz, ofertas_ordenadas = subasta_voraz(A, ofertas, oferta_gobierno)
    output += f"Asignación voraz: {mejor_asignacion_voraz} \n"
    output += f"Valor total (vr) voraz: {mejor_vr_voraz} \n"

    output += "\nPrueba del Enfoque con Programación Dinámica: \n"
    asignaciones_optimas, valor_maximo = subasta_dinamica(A, ofertas, oferta_gobierno)
    output += "Asignaciones programación dinámica: \n"
    for idx, (asignacion, oferta) in enumerate(zip(asignaciones_optimas[:-1], ofertas)):
        output += f"  Oferente {idx+1} (Precio: {oferta[0]}, Mín: {oferta[1]}, Máx: {oferta[2]}): {asignacion} acciones \n"
    output += f"  Gobierno (Precio: {oferta_gobierno[0]}): {asignaciones_optimas[-1]} acciones \n"
    output += f"Valor máximo (vr): {valor_maximo} \n"
    return output

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