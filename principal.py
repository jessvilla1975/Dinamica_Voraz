import tkinter as tk
from tkinter import ttk
from interfaz_subasta import SubastaPublica
from interfaz_trancadena import TransformadorCadenas  # Supongamos que tienes esta clase
#from suma import main as suma_main


class Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        
        #configurar tamaño ventana
        self.root.geometry("800x600")
        
        
        # Configurar el estilo
        self.root.configure(bg='#2F4F4F')
        style = ttk.Style()
        style.configure('Custom.TFrame', background='white')
        
        # Crear el menú superior
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Menú "Opciones"
        opciones_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=opciones_menu)
        
        # Añadir opciones al menú
        opciones_menu.add_command(label="Abrir Subasta", command=self.abrir_subasta)
        opciones_menu.add_command(label="Abrir Inteligencia", command=self.abrir_inteligencia)
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Salir", command=self.root.quit)
        
    

    def abrir_subasta(self):
        # Cerrar la ventana principal y abrir la interfaz Subasta
        self.root.destroy()
        nueva_ventana = tk.Tk()
        SubastaPublica(nueva_ventana)

    def abrir_inteligencia(self):
        # Cerrar la ventana principal y abrir la interfaz Inteligencia
        self.root.destroy()
        nueva_ventana = tk.Tk()
        TransformadorCadenas(nueva_ventana)


def main():
    root = tk.Tk()
    app = Principal(root)
    


    root.mainloop()


if __name__ == "__main__":
    main()
