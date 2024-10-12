# Este archivo implementa una solución voraz para el problema de la subasta pública.
# La solución voraz asigna las acciones de manera prioritaria a los oferentes que ofrezcan el precio más alto,
# respetando los límites mínimos y máximos de cada oferente.
# El objetivo es maximizar el valor total (vr) de la subasta siguiendo un enfoque simple y eficiente.
# Complejidad del algoritmo: O(n log n), donde n es el número de oferentes. La complejidad está dominada por la ordenación de las ofertas.
# Version 1.0
def subasta_voraz(A, ofertas, oferta_gobierno):
    """
    Implementa la solución voraz para la subasta.
    A: Número total de acciones.
    ofertas: Lista de ofertas, cada una es una tripleta (p_i, m_i, M_i).
    oferta_gobierno: Oferta del gobierno, tripleta (B, 0, A).
    """
    # Ordenar las ofertas por el precio (p_i) de mayor a menor
    ofertas_ordenadas = sorted(ofertas, key=lambda x: -x[0])
    
    asignaciones = [0] * len(ofertas_ordenadas)
    acciones_asignadas = 0

    # Asignar acciones a los oferentes según el algoritmo voraz
    for i, (p_i, m_i, M_i) in enumerate(ofertas_ordenadas):
        acciones_disponibles = A - acciones_asignadas  # Las acciones que quedan por asignar

        # Si no quedan acciones disponibles, detener
        if acciones_disponibles <= 0:
            break

        # Asignar la cantidad de acciones que respete el mínimo y máximo
        if acciones_disponibles >= m_i:
            acciones_a_asignar = min(M_i, acciones_disponibles)
            asignaciones[i] = acciones_a_asignar
            acciones_asignadas += acciones_a_asignar

    # Si quedan acciones, el gobierno las compra
    acciones_restantes = A - acciones_asignadas
    asignaciones_gobierno = acciones_restantes if acciones_restantes > 0 else 0

    # Calcular el valor total (vr)
    vr_total = 0
    for asignacion, oferta in zip(asignaciones, ofertas_ordenadas):
        p_i = oferta[0]
        vr_total += asignacion * p_i

    # Sumar la oferta del gobierno
    vr_total += acciones_restantes * oferta_gobierno[0]
    
    return asignaciones, vr_total, ofertas_ordenadas


def mostrar_resultados(asignaciones, vr_total, ofertas_ordenadas, oferta_gobierno):
    """
    Función para mostrar los resultados de la asignación de acciones de manera detallada.
    """
    print("Mejor asignación:")
    # Mostrar las asignaciones de cada oferente (en el orden ya ordenado)
    for idx, (asig, oferta) in enumerate(zip(asignaciones, ofertas_ordenadas)):
        print(f"  Oferente {idx+1} (Precio: {oferta[0]}, Mín: {oferta[1]}, Máx: {oferta[2]}): {asig} acciones")
    
    # Mostrar la asignación del gobierno
    print(f"  Gobierno (Precio: {oferta_gobierno[0]}): {A - sum(asignaciones)} acciones")
    
    # Mostrar el valor total (vr)
    print(f"Valor máximo (vr): {vr_total}")


#Pruebas
""" # Nuevas ofertas proporcionadas (desorganizadas para probar la ordenación)
nuevas_ofertas = [
    (500, 400, 600),
    (450, 100, 400),
    (400, 100, 400),
    (200, 50, 200)
]

# Datos de entrada
A = 1000  # Total de acciones
oferta_gobierno = (100, 0, A)  # Oferta del gobierno

# Llamada a la función con las nuevas ofertas
mejor_asignacion_nueva, mejor_vr_nueva, ofertas_ordenadas = subasta_voraz(A, nuevas_ofertas, oferta_gobierno)

# Mostrar los resultados detallados
mostrar_resultados(mejor_asignacion_nueva, mejor_vr_nueva, ofertas_ordenadas, oferta_gobierno) """
