import tkinter as tk

ventana =tk.Tk()
ventana.title("mi ventana")
ventana.geometry("400x300")

etiqueta= tk.Label(ventana, text="Hola mundo")
etiqueta.pack()

ventana.mainloop()