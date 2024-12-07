import tkinter as tk
from tkinter import ttk
from terminalInteligente.costos import calcular_costo
from terminalInteligente.dinamica import calcular_solucion_optima
from terminalInteligente.bruta import transformar_fuerza_bruta
from terminalInteligente.voraz import algoritmo_voraz

class TransformadorCadenas:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformar Cadenas")
        
        # Configurar el estilo
        self.root.configure(bg='#2F4F4F')
        style = ttk.Style()
        style.configure('Custom.TFrame', background='white')
        
        # Marco izquierdo para los controles
        left_frame = ttk.Frame(root, padding="10", style='Custom.TFrame')
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Sección de Costos
        ttk.Label(left_frame, text="Costos").grid(row=0, column=0, sticky=tk.W, pady=(0,10))
        
        cost_frame = ttk.Frame(left_frame)
        cost_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0,20))
        
        # Campos de costos
        cost_labels = ['Advance:', 'Insert:', 'Delete:', 'Replace:', 'Kill:']
        self.cost_entries = {}
        
        # Reorganizar los campos de costos en dos filas
        for i, label in enumerate(cost_labels):
            row = i // 3
            col = (i % 3) * 2
            ttk.Label(cost_frame, text=label).grid(row=row, column=col, padx=(5,5))
            self.cost_entries[label] = ttk.Entry(cost_frame, width=8)
            self.cost_entries[label].grid(row=row, column=col+1, padx=(0,10), pady=2)
            
        # Sección de Cadenas
        ttk.Label(left_frame, text="Cadenas").grid(row=2, column=0, sticky=tk.W, pady=(0,10))
        
        strings_frame = ttk.Frame(left_frame)
        strings_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0,20))
        
        # Reorganizar los campos de cadenas en dos filas
        ttk.Label(strings_frame, text="Actual:").grid(row=0, column=0, padx=(5,5))
        self.actual_entry = ttk.Entry(strings_frame, width=35)
        self.actual_entry.grid(row=0, column=1, padx=(0,10), pady=2)
        
        ttk.Label(strings_frame, text="Objetivo:").grid(row=1, column=0, padx=(5,5))
        self.objetivo_entry = ttk.Entry(strings_frame, width=35)
        self.objetivo_entry.grid(row=1, column=1, padx=(0,10), pady=2)
        
        # Sección de Algoritmo
        ttk.Label(left_frame, text="Algoritmo").grid(row=4, column=0, sticky=tk.W, pady=(0,10))
        
        algorithm_frame = ttk.Frame(left_frame)
        algorithm_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))
        
        self.algorithm_combo = ttk.Combobox(algorithm_frame, values=['Dinámica', 'Bruta', 'Voraz'], state='readonly', width=20)
        self.algorithm_combo.set('Dinámica')
        self.algorithm_combo.grid(row=0, column=0, padx=(5,10))
        
        self.start_button = ttk.Button(algorithm_frame, text="Iniciar", command=self.Iniciar)
        self.start_button.grid(row=0, column=1)
        
        # Botón Volver
        self.back_button = ttk.Button(root, text="Volver", command=self.regresar)
        self.back_button.grid(row=1, column=0, pady=20)
        
        # Panel derecho (cuadro grande)
        right_frame = ttk.Frame(root, padding="10", style='Custom.TFrame')
        right_frame.grid(row=0, column=1, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        
        # Texto grande a la derecha
        self.result_text = tk.Text(right_frame, width=70, height=30)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para el texto
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        # Configurar el peso de las columnas y filas para el redimensionamiento
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)
        
    def iniciar_transformacion(self):
        # Aquí iría la lógica de transformación
        pass
    
    def regresar(self):
        """Cerrar esta ventana y volver al menú principal."""
        self.root.destroy()  # Cerrar la ventana actual
        
        # Importar Principal dentro del método para evitar el ciclo
        from principal import Principal
        
        nueva_ventana = tk.Tk()  # Crear una nueva ventana
        Principal(nueva_ventana)  # Abrir la ventana principal
    
    # Función para calcular la solución óptima utilizando programación dinámica    
    def Dinamica(self):
        # Obtener las cadenas ingresadas por el usuario
        actual = self.actual_entry.get()
        objetivo = self.objetivo_entry.get()

        # Obtener los valores de los costos desde los campos de entrada
        try:
            a = int(self.cost_entries['Advance:'].get())
            b = int(self.cost_entries['Delete:'].get())
            c = int(self.cost_entries['Replace:'].get())
            d = int(self.cost_entries['Insert:'].get())
            e = int(self.cost_entries['Kill:'].get())
        except ValueError:
            # Si el valor no es un número, mostrar un error
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Por favor, ingrese valores válidos para los costos.")
            return

        # Llamar a la función de cálculo de la solución óptima con los costos personalizados
        costo, operaciones, matriz = calcular_solucion_optima(
            actual, objetivo, a, b, c, d, e
        )           

        # Mostrar los resultados en la interfaz
        self.result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto de resultados
        self.result_text.insert(tk.END, f'Costo total: {costo}\n')
        self.result_text.insert(tk.END, f"Mejor secuencia de operaciones:\n")
        self.result_text.insert(tk.END, f'Operaciones: {operaciones}\n')
        
        # Opcional: Imprimir la matriz si lo deseas mostrar
        self.result_text.insert(tk.END, "Matriz de costos:\n")
        for fila in matriz:
            self.result_text.insert(tk.END, f"{fila}\n")
            
    # Función para calcular la solución óptima utilizando Algotitmo voraz
    def Voraz(self):
        # Obtener las cadenas ingresadas por el usuario
        actual = self.actual_entry.get()
        objetivo = self.objetivo_entry.get()
        
        # Obtener los valores de los costos desde los campos de entrada
        try:
            a = int(self.cost_entries['Advance:'].get())
            b = int(self.cost_entries['Delete:'].get())
            c = int(self.cost_entries['Replace:'].get())
            d = int(self.cost_entries['Insert:'].get())
        except ValueError:
            # Si el valor no es un número, mostrar un error
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Por favor, ingrese valores válidos para los costos.")
            return
        
        
        # Llamar a la función de cálculo de la solución óptima con los costos personalizados
        costo, operaciones = algoritmo_voraz(actual, objetivo, a, b, c, d)
        
        
        # Mostrar los resultados en la interfaz
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f'Costo total: {costo}\n')
        self.result_text.insert(tk.END, f"Mejor secuencia de operaciones:\n")
        self.result_text.insert(tk.END, f'Operaciones: {operaciones}\n')
        
        """
        #opcional: Imprimir la matriz si lo deseas mostrar
        self.result_text.insert(tk.END, "Matriz de costos:\n")
        for fila in matriz:
            self.result_text.insert(tk.END, f"{fila}\n")
        
        """
    def Bruta(self):
        # Obtener las cadenas ingresadas por el usuario
        actual = self.actual_entry.get()
        objetivo = self.objetivo_entry.get()

        # Obtener los valores de los costos desde los campos de entrada
        try:
            a = int(self.cost_entries['Advance:'].get())
            b = int(self.cost_entries['Delete:'].get())
            c = int(self.cost_entries['Replace:'].get())
            d = int(self.cost_entries['Insert:'].get())
            e = int(self.cost_entries['Kill:'].get())
        except ValueError:
            # Si el valor no es un número, mostrar un error
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Por favor, ingrese valores válidos para los costos.")
            return

        # Llamar a la función de cálculo de la solución óptima con los costos personalizados
        costo, operaciones = transformar_fuerza_bruta(
            actual, objetivo, a, b, c, d, e
        )

        # Calcular el costo total
        resultado_final = calcular_costo(operaciones, a, b, c, d, e)

        # Mostrar los resultados en la interfaz
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Costo de la transformacion : {costo}\n")
        self.result_text.insert(tk.END, f"Mejor secuencia de operaciones:\n")
        self.result_text.insert(tk.END, f'Operaciones: {operaciones}\n')
        self.result_text.insert(tk.END, f"Costo total: {resultado_final}\n")
        
          
                    
    def Iniciar(self):
        # Obtener el valor seleccionado en el Combobox
        algoritmo_seleccionado = self.algorithm_combo.get()
        
        # Ejecutar la función correspondiente según el algoritmo seleccionado
        if algoritmo_seleccionado == "Dinámica":
            self.Dinamica()
        elif algoritmo_seleccionado == "Bruta":
            self.Bruta()
        elif algoritmo_seleccionado == "Voraz":
            self.Voraz()
        else:
            # Si no hay un algoritmo seleccionado, mostrar un mensaje de error
            self.result_text.insert(tk.END, "Seleccione un algoritmo válido.\n")


def main():
    root = tk.Tk()
    app = TransformadorCadenas(root)
    # Establecer un tamaño mínimo para la ventana
    root.minsize(800, 600)
    root.mainloop()

if __name__ == "__main__":
    main()