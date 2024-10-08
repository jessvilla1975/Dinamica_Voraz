# Este archivo implementa una solución con programación dinámica para el problema de la subasta pública.
# El objetivo es maximizar el valor total (vr) de la subasta considerando todas las combinaciones posibles,
# utilizando programación dinámica para evitar la evaluación redundante de subproblemas.

def subasta_dinamica(A, ofertas, oferta_gobierno):
    """
    Implementa la solución con programación dinámica para la subasta.
    A: Número total de acciones.
    ofertas: Lista de ofertas, cada una es una tripleta (p_i, m_i, M_i).
    oferta_gobierno: Oferta del gobierno, tripleta (B, 0, A).
    """
    n = len(ofertas)
    # Crear una matriz dp donde dp[i][j] representa el valor máximo posible con las primeras i ofertas y j acciones
    dp = [[float('-inf')] * (A + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base del caso inicial: con 0 ofertas y 0 acciones, el valor es 0

    # Llenar la tabla dp
    for i in range(1, n + 1):
        p_i, m_i, M_i = ofertas[i - 1]
        for j in range(A + 1):
            # No asignar acciones de la oferta actual
            dp[i][j] = dp[i - 1][j]
            # Asignar acciones de la oferta actual, desde m_i hasta min(M_i, j)
            for x in range(m_i, min(M_i, j) + 1):
                if dp[i - 1][j - x] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + x * p_i)

    # Obtener el valor máximo posible
    mejor_vr = float('-inf')
    mejor_asignacion = None
    for j in range(A + 1):
        if dp[n][j] != float('-inf'):
            acciones_restantes = A - j
            vr_total = dp[n][j] + acciones_restantes * oferta_gobierno[0]
            if vr_total > mejor_vr:
                mejor_vr = vr_total
                mejor_asignacion = j

    # Reconstruir la asignación óptima
    asignaciones = [0] * n
    acciones_restantes = mejor_asignacion
    for i in range(n, 0, -1):
        p_i, m_i, M_i = ofertas[i - 1]
        for x in range(m_i, min(M_i, acciones_restantes) + 1):
            if acciones_restantes - x >= 0 and dp[i - 1][acciones_restantes - x] + x * p_i == dp[i][acciones_restantes]:
                asignaciones[i - 1] = x
                acciones_restantes -= x
                break

    # Añadir la asignación del gobierno
    asignaciones.append(A - sum(asignaciones))

    return asignaciones, mejor_vr

#Pruebas
""" # Datos de entrada
A = 1000  # Total de acciones
ofertas = [
    (500, 100, 600),
    (450, 100, 400),
    (400, 100, 400),
    (200, 50, 200)
]
oferta_gobierno = (100, 0, A)  # Oferta del gobierno

# Llamada a la función con las ofertas
 """

# Mostrar los resultados detallados
""" print("Asignaciones óptimas:")
for idx, (asignacion, oferta) in enumerate(zip(asignaciones_optimas[:-1], ofertas)):
    print(f"  Oferente {idx+1} (Precio: {oferta[0]}, Mín: {oferta[1]}, Máx: {oferta[2]}): {asignacion} acciones")
print(f"  Gobierno (Precio: {oferta_gobierno[0]}): {asignaciones_optimas[-1]} acciones")
print(f"Valor máximo (vr): {valor_maximo}") """
#asignaciones_optimas, valor_maximo = subasta_dinamica(A, ofertas, oferta_gobierno)