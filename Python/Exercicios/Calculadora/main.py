#importando bibliotecas
from tkinter import *
from tkinter import ttk

#Definindo cores
gray = "#4b524d"; #cinza
white = "#ffffff"; #branco
black = "#000000";#preto
orange = "#ff8c00"; #laranja
blue = "#102ac2"; #azul

#Criando a janela
window = Tk();
window.title("Calculadora");
window.geometry("300x400");
window.configure(bg=gray);

#Criando o frame
window_frame = Frame(window, width=300, height=70, bg=gray);
window_frame.grid(row=0, column=0,);

#Segundo frame
window_frame2 = Frame(window, width=300, height=330,);
window_frame2.grid(row=1, column=0,);

#botões
but1 = Button(window_frame2, text="C", width=10, height=3, bg=white);
but1.place(x=0, y=0);

window.mainloop()
