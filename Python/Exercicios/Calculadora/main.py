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
window.geometry("287x420");
window.configure(bg=gray);

#Criando o frame
window_frame = Frame(window, width=300, height=70, bg=gray);
window_frame.grid(row=0, column=0,);

#Segundo frame
window_frame2 = Frame(window, width=300, height=420);
window_frame2.grid(row=1, column=0,);

#Criando label
text_val = StringVar();
label = Label(window_frame, textvariable = text_val, bg=gray, font=("ivy 20 bold"), width=16, height=2, padx=7, anchor=E, relief= FLAT, fg=white, justify=RIGHT);
label.place(x=0, y=0);
 

#botões
but1 = Button(window_frame2, command= lambda: clear(),text="C", width=14, height=3, bg=white, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE);
but1.place(x=0, y=0);
but2 = Button(window_frame2, command= lambda: input("%"), text="%", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but2.place(x=146, y=0);
but3 = Button(window_frame2, command= lambda: input("/"),text="/", width=7, height=3, bg=orange, font=("ivy 13 "),fg = white, relief=RAISED, overrelief=RIDGE);
but3.place(x=219, y=0);

but4 = Button(window_frame2, command= lambda: input("7"),text="7", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but4.place(x=0, y=70);
but5 = Button(window_frame2, command= lambda: input("8"),text="8", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but5.place(x=73, y=70);
but6 = Button(window_frame2, command= lambda: input("9"),text="9", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but6.place(x=146, y=70);
but7 = Button(window_frame2, command= lambda: input("*"),text="*", width=7, height=3, bg=orange, font=("ivy 13 "),fg = white, relief=RAISED, overrelief=RIDGE);
but7.place(x=219, y=70);

but8 = Button(window_frame2, command= lambda: input("4"),text="4", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but8.place(x=0, y=140);
but9 = Button(window_frame2, command= lambda: input("5"),text="5", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but9.place(x=73, y=140);
but10 = Button(window_frame2, command= lambda: input("6"),text="6", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but10.place(x=146, y=140);
but11 = Button(window_frame2, command= lambda: input("-"),text="-", width=7, height=3, bg=orange, font=("ivy 13 "),fg = white, relief=RAISED, overrelief=RIDGE);
but11.place(x=219, y=140);

but12 = Button(window_frame2, command= lambda: input("1"),text="1", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but12.place(x=0, y=210);
but13 = Button(window_frame2, command= lambda: input("2"),text="2", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but13.place(x=73, y=210);
but14 = Button(window_frame2, command= lambda: input("3"),text="3", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but14.place(x=146, y=210);
but15 = Button(window_frame2, command= lambda: input("+"),text="+", width=7, height=3, bg=orange, font=("ivy 13 "),fg = white, relief=RAISED, overrelief=RIDGE);
but15.place(x=219, y=210);

but16 = Button(window_frame2, command= lambda: input("0"),text="0", width=16, height=3, bg=white, font=("ivy 13"), relief=RAISED, overrelief=RIDGE);
but16.place(x=0, y=280);
but17 = Button(window_frame2, command= lambda: input("."),text=".", width=7, height=3, bg=white, font=("ivy 13 "), relief=RAISED, overrelief=RIDGE);
but17.place(x=146, y=280);
but18 = Button(window_frame2, command= lambda: calc(),text="=", width=7, height=3, bg=orange, font=("ivy 13 "),fg = white, relief=RAISED, overrelief=RIDGE);
but18.place(x=219, y=280);

#logica

#criando variavel all_values que recebe os valores digitados pelo usuario
all_values = "";


#criando função input, que recebe o evento e adiciona o valor ao all_values e seta o valor no label 
def input(event):
    
    global all_values
    
    all_values = all_values + str(event);
    text_val.set(all_values);
    
#definindo fuçnção calcular que calcula a expressão matematica
    
def calc():
    global all_values;
    
    answer = eval(all_values);
    print(answer);
    
#definindo função clear que limpa a tela

def clear():
    
    global all_values;
    
    all_values = "";
    text_val.set("");
     
window.mainloop()
