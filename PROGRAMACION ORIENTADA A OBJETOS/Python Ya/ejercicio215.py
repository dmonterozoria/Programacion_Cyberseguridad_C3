# 57 - Interfaz gráfica de usuario : tkinter

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.ventana1.mainloop()


aplicacion1=Aplicacion()