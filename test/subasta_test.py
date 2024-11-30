
# tests/test_subasta.py

import unittest
import time
from subasta.fuerza_bruta import subasta_fuerza_bruta
from subasta.voraz import subasta_voraz
from subasta.dinamica import subasta_dinamica

class TestSubasta(unittest.TestCase):

    def test_subasta_fuerza_bruta(self):
        print("\nProbando subasta fuerza_bruta...")
        A = 1000
        B = 100
        n = 2
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_fuerza_bruta(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 3
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [300, 100, 300],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_fuerza_bruta(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 3
        ofertas = [[500, 100, 200], 
                   [450, 400, 800],
                   [600, 100, 1000],
                   [100, 0, 1000]]
        asignacion_esperada = [0, 0, 1000, 0]
        vr_esperado = 600000
        inicio = time.time()
        asignacion, vr = subasta_fuerza_bruta(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

    def test_subasta_dinamica(self):
        print("\nProbando subasta dinámica...")
        A = 1000
        B = 100
        n = 2
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_dinamica(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 3
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [300, 100, 300],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_dinamica(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 4
        ofertas = [[500, 400, 600],
                   [450, 100, 400],
                   [400, 100, 400],
                   [200, 50, 200],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0, 0, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_dinamica(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

    def test_subasta_voraz(self):
        print("\nProbando subasta voraz...")
        A = 1000
        B = 100
        n = 2
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_voraz(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 1: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 3
        ofertas = [[500, 100, 600],
                   [450, 400, 800],
                   [300, 100, 300],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_voraz(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 2: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

        n = 4
        ofertas = [[500, 400, 600],
                   [450, 100, 400],
                   [400, 100, 400],
                   [200, 50, 200],
                   [100, 0, 1000]]
        asignacion_esperada = [600, 400, 0, 0, 0]
        vr_esperado = 480000
        inicio = time.time()
        asignacion, vr = subasta_voraz(A, B, n, ofertas)
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1000
        self.assertEqual(asignacion, asignacion_esperada, 'La asignación no es correcta.')
        self.assertEqual(vr, vr_esperado, 'El valor no es correcto.')
        print(f"Prueba 3: OK ☑ Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")

if __name__ == '__main__':
    unittest.main()
