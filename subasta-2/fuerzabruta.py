# Este archivo implementa la solucion de fuerza bruta para el problema de la subasta publica
# Calcula todas las posibles asignaciones de acciones para maximizar el valor total(vr)
# Utiliza todas las combinaciones posibles de asignaciones y selecciona la mejor
# Complejidad: O(n^m) donde n es el numero de ofertas y m es el numero de acciones totales
# Version 1.0
from itertools import product

def calcular_vr(asignacion, ofertas, oferta_gobierno):
    """Calcula el valor vr dado una asignación y las ofertas"""
    vr = 0
    for x_i, oferta in zip(asignacion, ofertas):
        p_i, m_i, M_i = oferta
        vr += x_i * p_i
    # Añadir la oferta del gobierno (acciones sobrantes a precio B)
    acciones_restantes = A - sum(asignacion)
    if acciones_restantes > 0:
        vr += acciones_restantes * oferta_gobierno[0]
    return vr

def subasta_fuerzabruta(A, ofertas, oferta_gobierno):
    """
    Implementa la solución ingenua para la subasta.
    A: Número total de acciones.
    ofertas: Lista de ofertas, cada una es una tripleta (p_i, m_i, M_i).
    oferta_gobierno: Oferta del gobierno, tripleta (B, 0, A).
    """
    mejor_vr = float('-inf')
    mejor_asignacion = None
    
    # Generar todas las posibles asignaciones de acciones
    posibles_asignaciones = product(*[range(m_i, M_i + 1) for _, m_i, M_i in ofertas])
    
    # Evaluar cada asignación
    for asignacion in posibles_asignaciones:
        acciones_asignadas = sum(asignacion)
        if acciones_asignadas <= A:
            # Asignar las acciones restantes al gobierno si es necesario
            acciones_restantes = A - acciones_asignadas
            vr = calcular_vr(asignacion + (acciones_restantes,), ofertas, oferta_gobierno)
            if vr > mejor_vr:
                mejor_vr = vr
                mejor_asignacion = asignacion + (acciones_restantes,)
                
    return mejor_asignacion, mejor_vr

# Datos de entrada (ejemplo con 2 ofertas. Esto despues va en test.py de esta misma carpeta)
A = 1000  # Total de acciones
ofertas = [
    (500, 100, 600),  # <precio por acción, mínimo de acciones, máximo de acciones>
    (450, 400, 800)
]
oferta_gobierno = (100, 0, A)  # Oferta del gobierno

# Llamada a la función
mejor_asignacion, mejor_vr = subasta_fuerzabruta(A, ofertas, oferta_gobierno)

# Salida de la mejor asignación y el valor vr
print(f"Mejor asignación: {mejor_asignacion}")
print(f"Valor máximo (vr): {mejor_vr}")