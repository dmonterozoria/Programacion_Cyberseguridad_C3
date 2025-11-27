#Crea una ventana con un Listbox que muestre una lista de elementos. Agrega un botón para añadir nuevos elementos a la lista.
import tkinter as tk
from tkinter import Label, Entry, Button, Listbox, Tk, mainloop, END

def agregar_elemento():
    nuevo_elemento = entrada.get()
    if nuevo_elemento:
        lista_elementos.insert(END, nuevo_elemento)
        entrada.delete(0, END)
        
ventana = Tk()
ventana.title("Lista de Elementos")
ventana.geometry("400x300")
entrada = Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)
boton_agregar = Button(ventana, text="Agregar Elemento", command=agregar_elemento, font=("Arial", 14))
boton_agregar.pack(pady=10)
lista_elementos = Listbox(ventana, font=("Arial", 14))
lista_elementos.pack(pady=10, fill=tk.BOTH, expand=True)
mainloop()