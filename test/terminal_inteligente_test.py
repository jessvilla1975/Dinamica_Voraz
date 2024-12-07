# terminalinteligente_test.py
import unittest
import time
from terminalInteligente.dinamica import calcular_solucion_optima
from terminalInteligente.voraz import algoritmo_voraz
from terminalInteligente.bruta import transformar_fuerza_bruta
from terminalInteligente.costos import calcular_costo

class TestTerminalInteligente(unittest.TestCase):

    def setUp(self):
        # Definir los costos que se usarán en todas las pruebas
        self.costos = {
            'advance': 1,  # a
            'delete': 2,   # b
            'replace': 3,  # c
            'insert': 2,   # d
            'kill': 1      # e
        }

    def test_calcular_solucion_optima(self):
        print("\nProbando TerminalInteligente calcular_solucion_optima...")

        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente calcular_solucion_optima 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente calcular_solucion_optima 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

    def test_algoritmo_voraz(self):
        print("\nProbando TerminalInteligente algoritmo_voraz...")
        
        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert']
        )
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente algoritmo_voraz 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert']
        )
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente algoritmo_voraz 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

    def test_transformar_fuerza_bruta(self):
        print("\nProbando transformar_fuerza_bruta...")

        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente transformar_fuerza_bruta 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(
            operaciones,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        print(f"Prueba TerminalInteligente transformar_fuerza_bruta 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

if __name__ == '__main__':
    unittest.main()
