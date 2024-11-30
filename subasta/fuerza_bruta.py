def subasta_fuerza_bruta(A, B, n, ofertas):
    # Función para calcular el valor total de una asignación
    def calcular_valor(asignacion):
        valor_total = 0
        acciones_restantes = A
        for i in range(n):
            if ofertas[i][0] >= B:  # oferta[i][0] es el precio de la oferta
                valor_total += asignacion[i] * ofertas[i][0]  # asignación[i] * precio
                acciones_restantes -= asignacion[i]
        total = valor_total + ofertas[n][0] * acciones_restantes  # oferta[n][0] es el precio de la última oferta
        return total

    mejor_asignacion = None
    mejor_valor_total = 0

    # Función recursiva para explorar todas las combinaciones posibles de asignación
    def explorar_combinaciones(i, acciones_restantes, asignacion_actual):
        nonlocal mejor_asignacion, mejor_valor_total
        if i == n:  # Caso base, hemos asignado todas las ofertas
            asignacion_actual[i] = acciones_restantes
            valor_total = calcular_valor(asignacion_actual)
            if valor_total > mejor_valor_total:
                mejor_valor_total = valor_total
                mejor_asignacion = asignacion_actual[:]
            return

        # Si el precio de la oferta es menor que el umbral, no la consideramos
        if ofertas[i][0] < B:
            explorar_combinaciones(i + 1, acciones_restantes, asignacion_actual)
            return

        # Definir el rango de acciones que se pueden asignar a esta oferta
        min_acciones = ofertas[i][1]  # ofertas[i][1] es el valor mínimo de acciones
        max_acciones = min(ofertas[i][2], acciones_restantes)  # ofertas[i][2] es el valor máximo de acciones

        # Probar con todas las cantidades posibles de acciones para esta oferta
        for x in range(min_acciones, max_acciones + 1):
            asignacion_actual[i] = x
            explorar_combinaciones(i + 1, acciones_restantes - x, asignacion_actual)
        
        # También probar la opción de no asignar ninguna acción a esta oferta
        asignacion_actual[i] = 0
        explorar_combinaciones(i + 1, acciones_restantes, asignacion_actual)

    # Llamada inicial para comenzar la recursión
    explorar_combinaciones(0, A, [0] * (n + 1))

    if mejor_asignacion is None:
        mejor_asignacion = [0] * (n + 1)

    # Calcular el valor total de la mejor asignación encontrada
    valor_total = calcular_valor(mejor_asignacion)

    return mejor_asignacion, valor_total
