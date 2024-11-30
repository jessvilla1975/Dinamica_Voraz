# terminalinteligente_test.py
""" 
import unittest
import time
from terminalInteligente.dinamica import calcular_solucion_optima
from terminalInteligente.voraz import algoritmo_voraz
from terminalInteligente.bruta import transformar_fuerza_bruta
from terminalInteligente.costos import calcular_costo

class TestTerminalInteligente(unittest.TestCase):

    def test_calcular_solucion_optima(self):
        print("\nProbando calcular_solucion_optima...")

        # Caso de prueba
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos

        costo_esperado = calcular_costo(operaciones)  # Ajustar según los valores de COSTOS
        operaciones_esperadas = ['advance', 'advance', 'kill', 'insert t', 'advance', 'insert u', 'advance', 'insert s', 'advance', 'kill', 'insert i', 'insert c']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba calcular_solucion_optima: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

    def test_algoritmo_voraz(self):
        print("\nProbando algoritmo_voraz...")
        
        # Caso de prueba
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(origen, destino)
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio  # Tiempo en nanosegundos

        costo_esperado = calcular_costo(operaciones)  # Ajustar según los valores de COSTOS
        operaciones_esperadas = ['advance', 'advance', 'replace g with t', 'replace o with r', 'replace r with u', 'advance', 'replace t with s', 'replace h with t', 'replace m with i', 'insert c']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba algoritmo_voraz: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

    def test_transformar_fuerza_bruta(self):
        print("\nProbando transformar_fuerza_bruta...")

        # Caso de prueba
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos

        costo_esperado = calcular_costo(operaciones)  # Ajustar según los valores de COSTOS
        operaciones_esperadas = ['advance', 'advance', 'replace with t', 'delete', 'advance', 'insert u', 'advance', 'insert s', 'advance', 'insert i', 'insert c', 'kill']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba transformar_fuerza_bruta: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

if __name__ == '__main__':
    unittest.main()
 """
# terminalinteligente_test.py

import unittest
import time
from terminalInteligente.dinamica import calcular_solucion_optima
from terminalInteligente.voraz import algoritmo_voraz
from terminalInteligente.bruta import transformar_fuerza_bruta
from terminalInteligente.costos import calcular_costo

class TestTerminalInteligente(unittest.TestCase):

    def test_calcular_solucion_optima(self):
        print("\nProbando calcular_solucion_optima...")

        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'advance', 'advance', 'advance', 'advance', 'kill', 'insert e', 'insert r', 'advance']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba calcular_solucion_optima 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'kill', 'insert t', 'advance', 'insert u', 'advance', 'insert s', 'advance', 'kill', 'insert i', 'insert c']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba calcular_solucion_optima 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 3
        origen = 'francesa'
        destino = 'ancestro'
        inicio = time.time()
        costo, operaciones, m = calcular_solucion_optima(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        operaciones_esperadas = ['insert a', 'kill', 'advance', 'advance', 'advance', 'advance', 'insert t', 'insert r', 'replace with o']
        costo_esperado = calcular_costo(operaciones)
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba calcular_solucion_optima 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

    def test_algoritmo_voraz(self):
        print("\nProbando algoritmo_voraz...")
        
        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(origen, destino)
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio  # Tiempo en nanosegundos

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'advance', 'advance', 'advance', 'advance', 'replace o with e', 'replace s with r', 'advance']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba algoritmo_voraz 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(origen, destino)
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'replace g with t', 'replace o with r', 'replace r with u', 'advance', 'replace t with s', 'replace h with t', 'replace m with i', 'insert c']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba algoritmo_voraz 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

        # Caso de prueba 3
        origen = 'francesa'
        destino = 'ancestro'
        inicio = time.time_ns()
        costo, operaciones = algoritmo_voraz(origen, destino)
        fin = time.time_ns()
        tiempo_ejecucion = fin - inicio
        operaciones_esperadas = ['replace f with a', 'replace r with n', 'replace a with c', 'replace n with e', 'replace c with s', 'replace e with t', 'replace s with r', 'replace a with o']
        costo_esperado = calcular_costo(operaciones)
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba algoritmo_voraz 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion} ns")

    def test_transformar_fuerza_bruta(self):
        print("\nProbando transformar_fuerza_bruta...")

        # Caso de prueba 1
        origen = 'ingenioso'
        destino = 'ingeniero'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'advance', 'advance', 'advance', 'advance', 'replace with e', 'replace with r']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba transformar_fuerza_bruta 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 2
        origen = 'algorithm'
        destino = 'altruistic'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000

        costo_esperado = calcular_costo(operaciones)
        operaciones_esperadas = ['advance', 'advance', 'replace with t', 'delete', 'advance', 'insert u', 'advance', 'insert s', 'advance', 'insert i', 'insert c', 'kill']
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba transformar_fuerza_bruta 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        # Caso de prueba 3
        origen = 'francesa'
        destino = 'ancestro'
        inicio = time.time()
        costo, operaciones = transformar_fuerza_bruta(origen, destino)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        operaciones_esperadas = ['delete', 'delete', 'advance', 'advance', 'advance', 'advance', 'advance', 'insert t', 'insert r', 'replace with o']
        costo_esperado = calcular_costo(operaciones)
        self.assertEqual(costo, costo_esperado, 'El costo no es correcto.')
        self.assertEqual(operaciones, operaciones_esperadas, 'Las operaciones no son correctas.')
        print(f"Prueba transformar_fuerza_bruta 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

if __name__ == '__main__':
    unittest.main()
