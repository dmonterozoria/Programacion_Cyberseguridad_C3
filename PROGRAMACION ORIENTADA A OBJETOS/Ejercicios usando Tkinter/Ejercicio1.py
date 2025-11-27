#Crea una ventana básica con Tkinter que muestre un mensaje de bienvenida usando un Label.
import tkinter as tk
from tkinter import Label
from tkinter import Tk
from tkinter import mainloop

ventana = Tk()
ventana.title("Bienvenida")
ventana.geometry("300x200")
mensaje = Label(ventana, text="¡Bienvenido Dennis!", font=("Arial", 16))
mensaje.pack(pady=70)
mainloop()