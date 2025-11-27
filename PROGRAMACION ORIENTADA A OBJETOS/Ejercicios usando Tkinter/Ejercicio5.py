#Diseña una interfaz con un Canvas donde el usuario pueda dibujar líneas manteniendo presionado el botón del mouse.
import tkinter as tk
from tkinter import Tk, Canvas, mainloop

def iniciar_dibujo(event):
    global ultima_posicion
    ultima_posicion = (event.x, event.y)

def dibujar(event):
    global ultima_posicion
    x, y = event.x, event.y
    canvas.create_line(ultima_posicion[0], ultima_posicion[1], x, y, fill="black", width=2)
    ultima_posicion = (x, y)

ventana = Tk()
ventana.title("Dibujo en Canvas")
ventana.geometry("600x400")
canvas = Canvas(ventana, bg="white", width=600, height=400)
canvas.pack()
canvas.bind("<Button-1>", iniciar_dibujo)
canvas.bind("<B1-Motion>", dibujar)
mainloop()