#importando bibliotecas
from tkinter import *
from tkinter import ttk

#Definindo cores
gray = "#4b524d" #cinza

#Criando a janela
window = Tk()
window.title("Calculadora")
window.geometry("300x400")

#Criando o frame
window_frame = Frame(window, width=300, height=70, bg= gray)
window_frame.grid(row=0, column=0)

window.mainloop()
