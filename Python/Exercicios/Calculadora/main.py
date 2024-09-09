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
window.geometry("287x400");
window.configure(bg=gray);

#Criando o frame
window_frame = Frame(window, width=300, height=70, bg=gray);
window_frame.grid(row=0, column=0,);

#Segundo frame
window_frame2 = Frame(window, width=300, height=330,);
window_frame2.grid(row=1, column=0,);

#botões
but1 = Button(window_frame2, text="C", width=14, height=3, bg=white, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE);
but1.place(x=0, y=0);
but2 = Button(window_frame2, text="%", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but2.place(x=146, y=0);
but3 = Button(window_frame2, text="/", width=7, height=3, bg=orange, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but3.place(x=219, y=0);

but4 = Button(window_frame2, text="7", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but4.place(x=0, y=70);
but5 = Button(window_frame2, text="8", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but5.place(x=73, y=70);
but6 = Button(window_frame2, text="9", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but6.place(x=146, y=70);
but7 = Button(window_frame2, text="*", width=7, height=3, bg=orange, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but7.place(x=219, y=70);


window.mainloop()
