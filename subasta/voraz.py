def subasta_voraz(A, B, n, ofertas):
    """
    Implementa la solución con un algoritmo voraz para la subasta pública.
    A: Número total de acciones.
    B: Precio mínimo de una oferta para ser considerada.
    n: Número de ofertas a considerar.
    ofertas: Lista de ofertas, cada una es una tripleta (precio, min_acciones, max_acciones).
    """
    # Ordenar las ofertas por precio de manera descendente
    ofertas.sort(reverse=True, key=lambda x: x[0])
    
    mejor_asignacion = [0] * (n + 1)
    acciones_restantes = A
    valor_total = 0

    for i in range(n):
        if ofertas[i][0] >= B:  # Considerar solo las ofertas con precio mayor o igual a B
            max_asignacion = min(ofertas[i][2], acciones_restantes)
            if max_asignacion >= ofertas[i][1]:  # Asignar solo si se cumple el mínimo de acciones
                mejor_asignacion[i] = max_asignacion
                acciones_restantes -= max_asignacion
                valor_total += max_asignacion * ofertas[i][0]
    
    # Asignar las acciones restantes al gobierno
    mejor_asignacion[n] = acciones_restantes
    valor_total += acciones_restantes * ofertas[n][0]
    
    return mejor_asignacion, valor_total
