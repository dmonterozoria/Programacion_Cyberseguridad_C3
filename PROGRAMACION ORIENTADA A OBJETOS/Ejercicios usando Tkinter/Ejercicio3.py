#Crea una calculadora sencilla que pueda sumar dos números usando Labels, Entries y Buttons.
import tkinter as tk
from tkinter import Label, Entry, Button, Tk, mainloop

def sumar_numeros():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa números válidos.")   
        
ventana = Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("400x250")
entrada1 = Entry(ventana, font=("Arial", 14))
entrada1.pack(pady=10)
entrada2 = Entry(ventana, font=("Arial", 14))
entrada2.pack(pady=10)
boton_sumar = Button(ventana, text="Sumar", command=sumar_numeros, font=("Arial", 14))
boton_sumar.pack(pady=10)
etiqueta_resultado = Label(ventana, text="Resultado: ", font=("Arial", 14))
etiqueta_resultado.pack(pady=10)
mainloop()