def subasta_voraz(A, B, n, ofertas):
    """
    Implementa la solución con un algoritmo voraz para la subasta pública.
    A: Número total de acciones.
    B: Precio mínimo de una oferta para ser considerada.
    n: Número de ofertas a considerar.
    ofertas: Lista de ofertas, cada una es una tripleta (precio, min_acciones, max_acciones).
    """
    # Ordenar las ofertas por precio de manera descendente
    ofertas_ordenadas = sorted([(precio, min_acc, max_acc, i) 
                               for i, (precio, min_acc, max_acc) in enumerate(ofertas[:n])], 
                             reverse=True)
    
    mejor_asignacion = [0] * (n + 1)
    acciones_restantes = A
    valor_total = 0

    # Procesar cada oferta en orden de precio descendente
    for precio, min_acc, max_acc, indice_original in ofertas_ordenadas:
        if precio >= B:  # Solo considerar ofertas que cumplan el precio mínimo
            # Determinar cuántas acciones podemos asignar
            if acciones_restantes >= min_acc:
                acciones_asignar = min(max_acc, acciones_restantes)
                if acciones_asignar >= min_acc:
                    mejor_asignacion[indice_original] = acciones_asignar
                    valor_total += acciones_asignar * precio
                    acciones_restantes -= acciones_asignar

    return mejor_asignacion, valor_total
