# Importamos las librerías necesarias
import time  # Para medir el tiempo de ejecución
import numpy as np  # Para manejar operaciones matemáticas y cálculos con arrays
import matplotlib.pyplot as plt  # Para generar gráficos
import os  # Para interactuar con el sistema de archivos (aunque no se usa en el código)
import json  # Para trabajar con datos en formato JSON (aunque no se usa en el código)
import math  # Para funciones matemáticas adicionales (aunque no se usa en el código)
from subasta.fuerza_bruta import subasta_fuerza_bruta  # Importamos el algoritmo de fuerza bruta
from subasta.voraz import subasta_voraz  # Importamos el algoritmo voraz
from subasta.dinamica import subasta_dinamica  # Importamos el algoritmo dinámico

# Definimos la clase para realizar el benchmarking de los algoritmos
class AuctionBenchmark:
    def __init__(self, num_iterations=50):
        self.num_iterations = num_iterations  # Número de iteraciones para las pruebas
        self.results = {}  # Diccionario para almacenar los resultados

    # Método para ejecutar el benchmark de los algoritmos
    def run_benchmark(self):
        # Casos de prueba con parámetros específicos
        test_cases = [
            {
                'name': 'Case n=1',
                'args': [100, 10, 2, [
                    [50, 10, 60],
                    [45, 40, 80],
                    [10, 0, 100]
                ]]
            },
            {
                'name': 'Case n=2',
                'args': [100, 10, 3, [
                    [50, 10, 60],
                    [45, 40, 80],
                    [30, 10, 30],
                    [10, 0, 100]
                ]]
            },
            {
                'name': 'Case n=3',
                'args': [100, 10, 4, [
                    [50, 40, 60],
                    [45, 10, 40],
                    [40, 10, 40],
                    [20, 5, 20],
                    [10, 0, 100]
                ]]
            }
        ]
        
        # Diccionario con los algoritmos que vamos a evaluar
        algorithms = {
            'Fuerza Bruta': subasta_fuerza_bruta,
            'Dinámico': subasta_dinamica,
            'Voraz': subasta_voraz
        }
        
        # Ejecutamos el benchmark para cada caso de prueba
        for case in test_cases:
            self.results[case['name']] = {}  # Inicializamos los resultados para cada caso
            print(f"\nBenchmarking {case['name']}:")  # Mostramos en pantalla el caso que estamos evaluando
            
            # Ejecutamos cada algoritmo para el caso de prueba
            for algo_name, algo_func in algorithms.items():
                times = []  # Lista para almacenar los tiempos de cada iteración
                iteration_details = []  # Lista para almacenar detalles de cada iteración
                for i in range(self.num_iterations):
                    start_time = time.time()  # Capturamos el tiempo al inicio de la ejecución
                    algo_func(*case['args'])  # Ejecutamos el algoritmo con los parámetros del caso
                    end_time = time.time()  # Capturamos el tiempo al final de la ejecución
                    iteration_time = (end_time - start_time) * 1000  # Convertimos el tiempo a milisegundos
                    times.append(iteration_time)  # Guardamos el tiempo de la iteración
                    
                    # Guardamos detalles de cada iteración
                    iteration_details.append({
                        'Iteración': i + 1,
                        'Tiempo de ejecución': iteration_time
                    })
                    
                    # Mostramos el tiempo de la iteración
                    print(f"  Iteración {i + 1}: {iteration_time:.4f} ms")
                
                # Calculamos el tiempo medio y la desviación estándar
                avg_time = np.mean(times)
                std_time = np.std(times)
                
                # Almacenamos los resultados
                self.results[case['name']][algo_name] = {
                    'mean': avg_time,
                    'std': std_time,
                    'times': times,
                    'iteration_details': iteration_details
                }
                
                # Mostramos los resultados finales para el algoritmo
                print(f"{algo_name:12} - Mean: {avg_time:8.2f} ms, Std: {std_time:8.2f} ms")
    
    # Método para generar y mostrar los gráficos con los resultados
    def plot_results(self):
        plt.figure(figsize=(12, 6))  # Definimos el tamaño de la figura
        
        # Obtenemos los nombres de los casos de prueba y algoritmos
        case_names = list(self.results.keys())
        algo_names = list(self.results[case_names[0]].keys())
        
        # Graficamos los resultados para cada algoritmo
        for i, algo_name in enumerate(algo_names):
            means = [self.results[case][algo_name]['mean'] for case in case_names]  # Promedio de tiempos
            stds = [self.results[case][algo_name]['std'] for case in case_names]  # Desviación estándar
            
            # Graficamos la media de los tiempos con puntos marcados
            plt.plot(case_names, means, marker='o', label=algo_name)
            
            # Agregamos barras de error (desviación estándar)
            plt.errorbar(case_names, means, yerr=stds, fmt='none', capsize=5, 
                         ecolor=plt.gca().lines[-1].get_color(), alpha=0.5)
        
        # Agregamos una línea de tendencia utilizando ajuste polinómico
        for i, algo_name in enumerate(algo_names):
            means = [self.results[case][algo_name]['mean'] for case in case_names]
            x = np.arange(len(means))  # Los índices de los casos de prueba
            z = np.polyfit(x, means, 1)  # Ajuste lineal (grado 1)
            p = np.poly1d(z)  # Función polinómica
            plt.plot(case_names, p(x), '--', 
                     color=plt.gca().lines[i*2].get_color(), 
                     alpha=0.5, 
                     label=f'{algo_name} Trend')
        
        # Añadimos etiquetas, título y leyenda al gráfico
        plt.xlabel('Casos de prueba')
        plt.ylabel('Tiempo (ms)')
        plt.title('Gráfico de Benchmarking')
        plt.legend()
        plt.yscale('log')  # Escala logarítmica para los tiempos
        plt.grid(True, which="both", ls="-", alpha=0.2)  # Rejilla para el gráfico
        plt.tight_layout()  # Ajustamos el diseño para evitar recortes
        plt.savefig('auction_benchmark_results.png')  # Guardamos el gráfico como imagen
        plt.show()  # Mostramos el gráfico en pantalla

# Ejecutamos el benchmark
benchmark = AuctionBenchmark(num_iterations=50)  # Creamos el objeto para el benchmark
benchmark.run_benchmark()  # Ejecutamos el benchmark
benchmark.plot_results()  # Ge