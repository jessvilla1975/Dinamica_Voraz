import time  # Módulo para medir tiempos de ejecución
import numpy as np  # Biblioteca para cálculos numéricos
import matplotlib.pyplot as plt  # Biblioteca para generación de gráficos
from terminalInteligente.dinamica import calcular_solucion_optima  # Importar algoritmo de programación dinámica
from terminalInteligente.voraz import algoritmo_voraz  # Importar algoritmo voraz
from terminalInteligente.bruta import transformar_fuerza_bruta  # Importar algoritmo de fuerza bruta
from terminalInteligente.costos import calcular_costo  # Importar función de cálculo de costos

class TerminalInteligenteBenchmark:
    def __init__(self, num_iterations=50):
        # Inicializar el benchmark con número de iteraciones (por defecto 50)
        self.num_iterations = num_iterations
        self.results = {}  # Diccionario para almacenar resultados de benchmarking
        
        # Definir costos de operaciones para transformación de cadenas
        self.costos = {
            'advance': 1,  # Costo de avanzar (a)
            'delete': 2,   # Costo de borrar (b)
            'replace': 3,  # Costo de reemplazar (c)
            'insert': 2,   # Costo de insertar (d)
            'kill': 1      # Costo de finalizar (e)
        }
        
        # Definir casos de prueba con cadenas de origen y destino
        self.test_cases = [
            {
                'name': 'Caso 1: ingenioso -> ingeniero',  # Primer caso de prueba
                'origen': 'ingenioso',
                'destino': 'ingeniero'
            },
            {
                'name': 'Caso 2: algorithm -> altruistic',  # Segundo caso de prueba
                'origen': 'algorithm', 
                'destino': 'altruistic'
            }
        ]
        
        # Definir diccionario de algoritmos a benchmarking
        self.algorithms = {
            'Programación Dinámica': self.benchmark_dinamica,  # Método para programación dinámica
            'Algoritmo Voraz': self.benchmark_voraz,           # Método para algoritmo voraz
            'Fuerza Bruta': self.benchmark_fuerza_bruta        # Método para fuerza bruta
        }
    
    def benchmark_dinamica(self, origen, destino):
        # Método de benchmark para el algoritmo de programación dinámica
        costo, operaciones, m = calcular_solucion_optima(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        return costo, operaciones
    
    def benchmark_voraz(self, origen, destino):
        # Método de benchmark para el algoritmo voraz
        costo, operaciones = algoritmo_voraz(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert']
        )
        return costo, operaciones
    
    def benchmark_fuerza_bruta(self, origen, destino):
        # Método de benchmark para el algoritmo de fuerza bruta
        costo, operaciones = transformar_fuerza_bruta(
            origen, destino,
            self.costos['advance'],
            self.costos['delete'],
            self.costos['replace'],
            self.costos['insert'],
            self.costos['kill']
        )
        return costo, operaciones
    
    def run_benchmark(self):
        # Método principal para ejecutar el benchmarking
        for case in self.test_cases:
            # Iterar sobre cada caso de prueba
            self.results[case['name']] = {}
            print(f"\nBenchmarking {case['name']}:")
            
            for algo_name, algo_func in self.algorithms.items():
                # Iterar sobre cada algoritmo
                times = []  # Lista para almacenar tiempos de ejecución
                iteration_details = []  # Lista para detalles de iteraciones
                
                for i in range(self.num_iterations):
                    # Realizar múltiples iteraciones para cada algoritmo y caso
                    print(f"Corriendo iteración {i + 1} para {algo_name}")
                    start_time = time.time()
                    
                    # Ejecutar el algoritmo
                    try:
                        costo, operaciones = algo_func(case['origen'], case['destino'])
                        
                        # Verificar el costo calculado
                        costo_esperado = calcular_costo(
                            operaciones,
                            self.costos['advance'],
                            self.costos['delete'],
                            self.costos['replace'],
                            self.costos['insert'],
                            self.costos['kill']
                        )
                        
                        # Asegurar que el costo calculado coincida
                        assert costo == costo_esperado, 'El costo no es correcto.'
                    except Exception as e:
                        print(f"Error en iteración {i+1}: {e}")
                        continue
                    
                    end_time = time.time()
                    iteration_time = (end_time - start_time) * 1000  # Convertir a milisegundos
                    times.append(iteration_time)
                    
                    # Almacenar detalles de iteración
                    iteration_details.append({
                        'iteration': i + 1,
                        'time': iteration_time
                    })
                    
                    # Imprimir tiempo de cada iteración
                    print(f"Tiempo de iteración: {iteration_time:.4f} ms")
                
                # Calcular estadísticas de tiempo
                avg_time = np.mean(times)
                std_time = np.std(times)
                
                # Almacenar resultados
                self.results[case['name']][algo_name] = {
                    'mean': avg_time,
                    'std': std_time,
                    'times': times,
                    'iteration_details': iteration_details
                }
                
                # Imprimir resumen de resultados
                print(f"{algo_name:20} - Media: {avg_time:8.2f} ms, Desviación Std: {std_time:8.2f} ms")
    
    def plot_results(self):
        # Método para generar visualización de resultados
        plt.figure(figsize=(12, 6))  # Crear figura de gráfico
        
        # Obtener nombres de casos y algoritmos
        case_names = list(self.results.keys())
        algo_names = list(self.results[case_names[0]].keys())
        
        # Graficar tiempos medios
        for i, algo_name in enumerate(algo_names):
            # Obtener tiempos medios y desviaciones estándar
            means = [self.results[case][algo_name]['mean'] for case in case_names]
            stds = [self.results[case][algo_name]['std'] for case in case_names]
            
            # Graficar puntos y línea
            plt.plot(case_names, means, marker='o', label=algo_name)
            
            # Agregar barras de error
            plt.errorbar(case_names, means, yerr=stds, fmt='none', capsize=5, 
                         ecolor=plt.gca().lines[-1].get_color(), alpha=0.5)
        
        # Calcular y graficar líneas de tendencia
        for i, algo_name in enumerate(algo_names):
            means = [self.results[case][algo_name]['mean'] for case in case_names]
            
            # Usar valores numéricos para x
            x = range(len(means))
            
            # Intentar ajuste exponencial, con respaldo lineal
            try:
                # Ajuste exponencial usando logaritmo
                log_means = np.log(means)
                z = np.polyfit(x, log_means, 1)
                p = np.poly1d(z)
                
                # Línea de tendencia exponencial
                trend_line = np.exp(p(x))
            except:
                # Respaldo a ajuste lineal si exponencial falla
                z = np.polyfit(x, means, 1)
                p = np.poly1d(z)
                trend_line = p(x)
            
            # Graficar línea de tendencia
            plt.plot(case_names, trend_line, '--', 
                     color=plt.gca().lines[i*2].get_color(), 
                     alpha=0.5, 
                     label=f'{algo_name} Tendencia')
        
        # Configuración de etiquetas y título
        plt.xlabel('Casos de Prueba')
        plt.ylabel('Tiempo (ms)')
        plt.title('Comparación de Rendimiento de Algoritmos de Terminal Inteligente')
        plt.legend()
        plt.yscale('log')  # Escala logarítmica en eje y
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.tight_layout()
        plt.savefig('terminal_inteligente_benchmark_results.png')  # Guardar gráfico
        plt.show()  # Mostrar gráfico

# Ejecutar benchmark
benchmark = TerminalInteligenteBenchmark(num_iterations=50)  # Crear instancia con 50 iteraciones
benchmark.run_benchmark()  # Ejecutar benchmark
benchmark.plot_results() 