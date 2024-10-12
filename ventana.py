import tkinter as tk
from tkinter import Button, ttk
from tkinter import messagebox
from terminalInteligente.test import ejecutar_ejemplos
from subasta.test2 import probar_enfoques, A, ofertas, ofertas2, oferta_gobierno



# Función para mostrar la siguiente ventana
def ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Terminal inteligente")
    nueva_ventana.geometry("400x400")
    



# Crear la ventana principal
root = tk.Tk()
root.title("Ventana principal")
root.geometry("800x600")  # Establecer tamaño más grande
root.resizable(False, False)



titulo_principal = tk.Label(root, text= "Proyecto ADA ll", font=("Arial", 24, "bold"))
titulo_principal.pack(pady=20)

# Frame izquierdo para las entradas
frame_izquierdo = tk.Frame(root)
frame_izquierdo.pack(side="left", padx=15, pady=15)


text_area = tk.Text(root, height=23, width=86)
text_area.place(x=50, y=170)
#text_area.config(state='disabled')
#text_area.pack(padx=40, pady=10)

# Crear una scrollbar
scrollbar = tk.Scrollbar(root, command=text_area.yview)
scrollbar.place(x=40, y=170, height=400)  # Ajusta la posición según el tamaño de tu text_area

# Configurar el text_area para que use la scrollbar
text_area.config(yscrollcommand=scrollbar.set)


label_estrategia = tk.Label(text="Problemas:")
label_estrategia.place(x=260, y=80)


estrategias = ["Terminal inteligente", "Subasta"]
combo_estrategia = ttk.Combobox(values=estrategias, state='readonly')
combo_estrategia.place(x=350, y=80)

combo_estrategia.current(0) 


limpiar = tk.Button(root, text="Limpiar")
limpiar.place(x=430, y=120)
#------------------------------------------------

# ----------------------- Eventos -----------------------

def ejecutar_accion():
    seleccion = combo_estrategia.get()
    if seleccion == "Terminal inteligente":
        contenido = ejecutar_ejemplos()
        if contenido:
            # Habilitar el text_area para editarlo
            text_area.config(state='normal')
            # Insertar el contenido en el text_area
            text_area.insert(tk.END, contenido)
            # Deshabilitar el text_area nuevamente
            text_area.config(state='disabled')
        else:
            messagebox.showerror("Error", "La función ejecutar_ejemplos() no retornó ningún contenido.")
    elif seleccion == "Subasta":
        contenidos = probar_enfoques(A, ofertas, oferta_gobierno)
        if contenidos:
            text_area.config(state='normal')
            text_area.insert(tk.END, contenidos)
            text_area.config(state='disabled')
        
    else:
        messagebox.showwarning("Selección no válida", "Por favor, selecciona una estrategia válida.")

# Función que se ejecuta al presionar el botón "Limpiar"
def limpiar_texto():
    # Habilitar el text_area para editarlo
    text_area.config(state='normal')
    # Borrar todo el contenido del text_area
    text_area.delete("1.0", tk.END)
    # Deshabilitar el text_area nuevamente
    text_area.config(state='disabled')




#---------------------------------------------------------------------
ejecutar = tk.Button(root, text="Ejecutar", command=ejecutar_accion)
ejecutar.place(x=340, y=120)
#-----------------------------------------------------------------------
limpiar = tk.Button(root, text="Limpiar", command=limpiar_texto)
limpiar.place(x=430, y=120)
#-----------------------------------------------------------------------
root.mainloop()



