def subasta_fuerza_bruta(A, B, n, ofertas):
    def calcular_valor(asignacion):
        valor_total = 0
        acciones_restantes = A
        
        # Calculamos el valor de las asignaciones actuales
        for i in range(len(ofertas)):
            if ofertas[i][0] >= B:  # Solo consideramos ofertas que cumplan el precio mínimo
                valor_total += asignacion[i] * ofertas[i][0]
                acciones_restantes -= asignacion[i]
        
        return valor_total  # Ya no agregamos valor por acciones restantes

    mejor_asignacion = None
    mejor_valor_total = 0

    def explorar_combinaciones(i, acciones_restantes, asignacion_actual):
        nonlocal mejor_asignacion, mejor_valor_total
        
        # Caso base: llegamos al final de las ofertas disponibles
        if i == n:
            valor_total = calcular_valor(asignacion_actual)
            if valor_total > mejor_valor_total:
                mejor_valor_total = valor_total
                mejor_asignacion = asignacion_actual[:]
            return

        # Si el precio de la oferta es menor que el umbral, saltamos a la siguiente
        if ofertas[i][0] < B:
            asignacion_actual[i] = 0
            explorar_combinaciones(i + 1, acciones_restantes, asignacion_actual)
            return

        # Probamos asignar diferentes cantidades de acciones
        min_acciones = ofertas[i][1]  # Mínimo requerido
        max_acciones = min(ofertas[i][2], acciones_restantes)  # Máximo posible

        # Primero probamos no asignar nada
        asignacion_actual[i] = 0
        explorar_combinaciones(i + 1, acciones_restantes, asignacion_actual)

        # Luego probamos las asignaciones válidas
        if max_acciones >= min_acciones:
            for x in range(min_acciones, max_acciones + 1):
                asignacion_actual[i] = x
                if acciones_restantes >= x:  # Verificamos que tengamos suficientes acciones
                    explorar_combinaciones(i + 1, acciones_restantes - x, asignacion_actual)
                asignacion_actual[i] = 0  # Restauramos el estado

    # Iniciamos la exploración
    explorar_combinaciones(0, A, [0] * (len(ofertas)))

    if mejor_asignacion is None:
        mejor_asignacion = [0] * (len(ofertas))

    return mejor_asignacion, mejor_valor_total
