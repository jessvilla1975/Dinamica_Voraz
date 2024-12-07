import tkinter as tk
from tkinter import ttk
from subasta.dinamica import subasta_dinamica
from subasta.fuerza_bruta import subasta_fuerza_bruta
from subasta.voraz import subasta_voraz

class SubastaPublica:
    def __init__(self, root):
        self.root = root
        self.root.title("Subasta Pública")
        
        # Configurar el estilo
        self.root.configure(bg='#2F4F4F')
        style = ttk.Style()
        style.configure('Custom.TFrame', background='white')
        
        # Marco izquierdo para los controles
        left_frame = ttk.Frame(root, padding="10", style='Custom.TFrame')
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Sección de Datos
        ttk.Label(left_frame, text="Datos").grid(row=0, column=0, sticky=tk.W, pady=(0,10))
        
        datos_frame = ttk.Frame(left_frame)
        datos_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0,20))
        
        # Campos de datos
        ttk.Label(datos_frame, text="Acciones:").grid(row=0, column=0, padx=(5,5))
        self.acciones_entry = ttk.Entry(datos_frame, width=8)
        self.acciones_entry.grid(row=0, column=1, padx=(0,10), pady=2)
        self.acciones_entry.bind("<KeyRelease>", self.update_gobierno_offer)
        
        ttk.Label(datos_frame, text="Precio:").grid(row=0, column=2, padx=(5,5))
        self.precio_entry = ttk.Entry(datos_frame, width=8)
        self.precio_entry.grid(row=0, column=3, padx=(0,10), pady=2)
        self.precio_entry.bind("<KeyRelease>", self.update_gobierno_offer)
        
        ttk.Label(datos_frame, text="Número de ofertas:").grid(row=1, column=0, padx=(5,5))
        self.num_ofertas = ttk.Spinbox(datos_frame, from_=1, to=10, width=5, command=self.actualizar_ofertas)
        self.num_ofertas.grid(row=1, column=1, padx=(0,10), pady=2)
        
        # Sección de Ofertas
        ttk.Label(left_frame, text="Ofertas").grid(row=2, column=0, sticky=tk.W, pady=(0,10))
        
        self.ofertas_frame = ttk.Frame(left_frame)
        self.ofertas_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0,20))
        
        # Frame para las ofertas dinámicas
        self.ofertas_entries = []
        
        # Sección de Oferta del gobierno
        ttk.Label(left_frame, text="Oferta del gobierno").grid(row=4, column=0, sticky=tk.W, pady=(0,10))
        
        gobierno_frame = ttk.Frame(left_frame)
        gobierno_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0,20))
        
        ttk.Label(gobierno_frame, text="Gobierno:").grid(row=0, column=0, padx=(5,5))
        self.gobierno_entry = ttk.Entry(gobierno_frame, width=35)
        self.gobierno_entry.grid(row=0, column=1, padx=(0,10), pady=2)
        
        # Sección de Algoritmo
        ttk.Label(left_frame, text="Algoritmo").grid(row=6, column=0, sticky=tk.W, pady=(0,10))
        
        algorithm_frame = ttk.Frame(left_frame)
        algorithm_frame.grid(row=7, column=0, sticky=(tk.W, tk.E))
        
        self.algorithm_combo = ttk.Combobox(algorithm_frame, values=['Dinámica', 'Bruta', 'Voraz'], 
                                          state='readonly', width=20)
        self.algorithm_combo.set('Dinámica')
        self.algorithm_combo.grid(row=0, column=0, padx=(5,10))
        
        self.start_button = ttk.Button(algorithm_frame, text="Iniciar", command=self.iniciar_subasta)
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
        
        # Configurar el peso de las columnas y filas
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)
        
        # Inicializar con una oferta por defecto
        self.actualizar_ofertas()
        
    def subastaDinamica(self):
        try:
            # Obtener los valores de entrada
            A = int(self.acciones_entry.get())
            B = int(self.precio_entry.get())
            n = int(self.num_ofertas.get())
            ofertas = []

            # Recopilar las ofertas ingresadas
            for i in range(n):
                entry = self.ofertas_entries[i]
                oferta = entry.get()
                precio, minimo, maximo = map(int, oferta.split(','))
                ofertas.append((precio, minimo, maximo))

            # Llamar al método de programación dinámica (importado)
            asignaciones, valor_total = subasta_dinamica(A, B, n, ofertas)

            # Mostrar resultados en el cuadro de texto
            self.result_text.insert(tk.END, f"Resultados de Subasta Dinámica:\n")
            self.result_text.insert(tk.END, f"Asignaciones: {asignaciones}\n")
            self.result_text.insert(tk.END, f"Valor total: {valor_total}\n\n")
        except Exception as e:
            # Manejar errores y mostrar un mensaje
            self.result_text.insert(tk.END, f"Error: {str(e)}\n")
    
    def subastaBruta(self):
        try:
            # Obtener los valores de entrada
            A = int(self.acciones_entry.get())
            B = int(self.precio_entry.get())
            n = int(self.num_ofertas.get())
            ofertas = []
            
            # Recopilar las ofertas ingresadas
            for i in range(n):
                entry = self.ofertas_entries[i]
                oferta = entry.get()
                precio, minimo, maximo = map(int, oferta.split(','))
                ofertas.append((precio, minimo, maximo))
            
            # Llamar al método de fuerza bruta (importado)
            asignaciones, valor_total = subasta_fuerza_bruta(A, B, n, ofertas)
            
            # Mostrar resultados en el cuadro de texto
            self.result_text.insert(tk.END, f"Resultados de Subasta Bruta:\n")
            self.result_text.insert(tk.END, f"Asignaciones: {asignaciones}\n")
            self.result_text.insert(tk.END, f"Valor total: {valor_total}\n\n")
            print(asignaciones, valor_total)
        except ValueError:
            self.result_text.insert(tk.END, f"Error en la oferta {i+1}: Formato inválido.\n")
            return
    
    def subastaVoraz(self):
        try:
            # Obtener los valores de entrada
            A = int(self.acciones_entry.get())
            B = int(self.precio_entry.get())
            n = int(self.num_ofertas.get())
            ofertas = []

            # Recopilar las ofertas ingresadas
            for i in range(n):
                entry = self.ofertas_entries[i]
                oferta = entry.get()
                precio, minimo, maximo = map(int, oferta.split(','))
                ofertas.append((precio, minimo, maximo))

            # Llamar al método de programación dinámica (importado)
            asignaciones, valor_total = subasta_voraz(A, B, n, ofertas)

            # Mostrar resultados en el cuadro de texto
            self.result_text.insert(tk.END, f"Resultados de Subasta Voraz:\n")
            self.result_text.insert(tk.END, f"Asignaciones: {asignaciones}\n")
            self.result_text.insert(tk.END, f"Valor total: {valor_total}\n\n")
        except Exception as e:
            # Manejar errores y mostrar un mensaje
            self.result_text.insert(tk.END, f"Error: {str(e)}\n")     
        
    

        

 
    def regresar(self):
        """Cerrar esta ventana y volver al menú principal."""
        self.root.destroy()  # Cerrar la ventana actual
        
        # Importar Principal dentro del método para evitar el ciclo
        from principal import Principal
        
        nueva_ventana = tk.Tk()  # Crear una nueva ventana
        Principal(nueva_ventana)  # Abrir la ventana principal

        
    def actualizar_ofertas(self):
        # Limpiar ofertas existentes
        for entry in self.ofertas_entries:
            entry.destroy()
        self.ofertas_entries.clear()
        
        # Crear nuevas ofertas según el número seleccionado
        try:
            num = int(self.num_ofertas.get())
            for i in range(num):
                entry = tk.Entry(self.ofertas_frame, width=35)
                entry.grid(row=i, column=0, pady=2, padx=5)
                entry.insert(0, f"Oferta {i+1}: precio, min, max")
                entry.bind('<FocusIn>', self.on_entry_focus_in)
                entry.bind('<FocusOut>', self.on_entry_focus_out)
                self.ofertas_entries.append(entry)
        except ValueError:
            pass
    
    def on_entry_focus_in(self, event):
        # Borrar el texto de placeholder cuando se enfoca
        entry = event.widget
        if entry.get().startswith("Oferta"):
            entry.delete(0, tk.END)
    
    def on_entry_focus_out(self, event):
        # Restaurar placeholder si está vacío
        entry = event.widget
        if not entry.get().strip():
            index = self.ofertas_entries.index(entry)
            entry.insert(0, f"Oferta {index+1}: precio, min, max")
    
    def update_gobierno_offer(self, event=None):
        # Actualizar el campo de Oferta del gobierno
        acciones = self.acciones_entry.get()
        precio = self.precio_entry.get()
        self.gobierno_entry.delete(0, tk.END)
        self.gobierno_entry.insert(0, f"{precio}, {acciones}")
    
    def iniciar_subasta(self):
        # Obtener el valor seleccionado en el Combobox
        algoritmo_seleccionado = self.algorithm_combo.get()
        
        # Ejecutar la función correspondiente según el algoritmo seleccionado
        if algoritmo_seleccionado == "Dinámica":
            self.subastaDinamica()
        elif algoritmo_seleccionado == "Bruta":
            self.subastaBruta()
        elif algoritmo_seleccionado == "Voraz":
            self.subastaVoraz()
        else:
            # Si no hay un algoritmo seleccionado, mostrar un mensaje de error
            self.result_text.insert(tk.END, "Seleccione un algoritmo válido.\n")

    


def main():
    root = tk.Tk()
    app = SubastaPublica(root)
    # Establecer un tamaño mínimo para la ventana
    root.minsize(800, 600)
    root.mainloop()

if __name__ == "__main__":
    main()