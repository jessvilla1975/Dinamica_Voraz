import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Necesario para manejar imágenes
from interfaz_subasta import SubastaPublica
from interfaz_trancadena import TransformadorCadenas

class Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        
        # Configurar tamaño ventana
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

        # Crear un frame para contener la imagen
        self.frame_imagen = tk.Frame(self.root, bg='#2F4F4F')
        self.frame_imagen.place(relx=0.5, rely=0.5, anchor='center')
        
        # Cargar y mostrar la imagen
        try:
            # Reemplaza 'ruta_de_tu_imagen.png' con la ruta real de tu imagen
            imagen = Image.open('../Dinamica_Voraz/imagen/img.png')
            
            # Redimensionar la imagen si es necesario (ajusta los valores según necesites)
            imagen = imagen.resize((400, 300), Image.Resampling.LANCZOS)
            self.foto = ImageTk.PhotoImage(imagen)
            
            # Crear y posicionar el label con la imagen
            self.label_imagen = tk.Label(self.frame_imagen, image=self.foto, bg='#2F4F4F')
            self.label_imagen.pack()
            
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            # Crear un label con texto en caso de que la imagen no se pueda cargar
            self.label_imagen = tk.Label(
                self.frame_imagen,
                text="Imagen no disponible",
                font=('Arial', 14),
                bg='#2F4F4F',
                fg='white'
            )
            self.label_imagen.pack()

    def abrir_subasta(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        SubastaPublica(nueva_ventana)

    def abrir_inteligencia(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        TransformadorCadenas(nueva_ventana)

def main():
    root = tk.Tk()
    app = Principal(root)
    root.mainloop()

if __name__ == "__main__":
    main()