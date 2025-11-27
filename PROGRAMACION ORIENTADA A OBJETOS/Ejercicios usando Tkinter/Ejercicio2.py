#Crea una interfaz con un Entry y un Button. Al presionar el botón, muestra el texto escrito en el Entry en un Label.
import tkinter as tk
from tkinter import Label, Entry, Button, Tk, mainloop

def mostrar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)
    
ventana = Tk()
ventana.title("Entrada de Texto")
ventana.geometry("400x200")
entrada = Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)
boton = Button(ventana, text="Mostrar Texto", command=mostrar_texto, font=("Arial", 14))
boton.pack(pady=10)
etiqueta = Label(ventana, text="", font=("Arial", 14))
etiqueta.pack(pady=10)
mainloop()