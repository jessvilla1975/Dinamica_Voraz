def subasta_dinamica(A, B, n, ofertas):
    """
    Implementa la solución de programación dinámica para la subasta pública.
    A: Número total de acciones.
    B: Precio mínimo de una oferta para ser considerada.
    n: Número de ofertas a considerar.
    ofertas: Lista de ofertas, cada una es una tripleta (precio, min_acciones, max_acciones).
    """
    dp = [[0] * (A + 1) for _ in range(n + 1)]
    asignaciones = [[[] for _ in range(A + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        precio, min_acciones, max_acciones = ofertas[i - 1]
        for acciones in range(A + 1):
            dp[i][acciones] = dp[i - 1][acciones]
            asignaciones[i][acciones] = asignaciones[i - 1][acciones][:]
            if precio >= B:
                for x in range(min_acciones, min(max_acciones, acciones) + 1):
                    valor = dp[i - 1][acciones - x] + x * precio
                    if valor > dp[i][acciones]:
                        dp[i][acciones] = valor
                        asignaciones[i][acciones] = asignaciones[i - 1][acciones - x][:]
                        asignaciones[i][acciones].append(x)

    mejor_asignacion = asignaciones[n][A]

    # Asegúrate de que la asignación tenga la longitud correcta
    # Si hay ofertas restantes, debemos añadir las acciones restantes (A - sum(mejor_asignacion))
    if len(mejor_asignacion) < n:
        mejor_asignacion.extend([0] * (n - len(mejor_asignacion)))  # Rellenar con ceros si faltan asignaciones

    # Calcular el valor total de la subasta
    valor_total = 0
    for i in range(n):
        precio, min_acciones, max_acciones = ofertas[i]
        valor_total += mejor_asignacion[i] * precio

    # Crear la lista de asignaciones en el formato deseado (agregar acciones restantes)
    resultado_asignacion = mejor_asignacion + [A - sum(mejor_asignacion)]

    return resultado_asignacion, valor_total
