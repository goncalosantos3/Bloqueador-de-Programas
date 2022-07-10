from tabnanny import check
from tkinter import *
from turtle import width 
from PIL import ImageTk, Image
from pyparsing import col

#
#   O tkinter funciona da seguinte forma:
#   1. Temos que definir um widget (butão, janela, barra, qualquer merda de interação com o user)
#   2. Depois, temos que inserir o widget criado no ecrã da maneira que quisermos 

def adicionaRestrição():
    top = Toplevel()
    top.title("Bloqueador de programas") 
    top.iconbitmap('C:/Users/smgon/Phyton/Bloqueador-de-Programas/Sawyer_Pilar.ico')
    top.geometry("500x500")

    var1 = IntVar() 
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    c1 = Checkbutton(top, text="Todos os dias", variable= var1)
    c2 = Checkbutton(top, text="Segunda-feira", variable= var2)
    c3 = Checkbutton(top, text="Terça-feira", variable= var3)
    c4 = Checkbutton(top, text="Quarta-feira", variable= var4)  
    c5 = Checkbutton(top, text="Quinta-feira", variable= var5) 
    c6 = Checkbutton(top, text="Sexta-feira", variable= var6)
    c7 = Checkbutton(top, text="Sábado", variable= var7)
    c8 = Checkbutton(top, text="Domingo", variable= var8)
    c1.grid(row=1,column=0)
    c2.grid(row=2,column=0)
    c3.grid(row=3,column=0)
    c4.grid(row=4,column=0)
    c5.grid(row=5,column=0)
    c6.grid(row=6,column=0)
    c7.grid(row=7,column=0)
    c8.grid(row=8,column=0)

    i = 0
    while i < 8:       
        lab1 = Label(top, text="Das")
        lab2 = Label(top, text=":")
        lab3 = Label(top, text="Até") 
        lab1.grid(row=i+1, column=1)
        lab2.grid(row=i+1, column=3)
        lab3.grid(row=i+1, column=5)

        options1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        options2 = [0, 30]

        clicked1 = StringVar()
        clicked1.set(options1[0])

        clicked2 = StringVar()
        clicked2.set(options2[0])

        drop1 = OptionMenu(top, clicked1, *options1)
        drop1.grid(row=i+1,column=2)

        drop2 = OptionMenu(top, clicked2, *options2)
        drop2.grid(row=i+1, column=4)
        i = i+1

    aplicar = Button(top, text="Aplicar")
    aplicar.grid(row=10,column=10)
    cancelar = Button(top, text="Cancelar", command=top.destroy)
    cancelar.grid(row=10,column=11)

    top.mainloop()


def alteraRestrição():
    top = Toplevel()
    top.title("Bloqueador de programas")
    top.iconbitmap('C:/Users/smgon/Phyton/Bloqueador-de-Programas/Sawyer_Pilar.ico')

    my_label = Label(top, text = "Alterar restrição ao programa " + myListBox.get(ANCHOR) + " :")
    my_label.pack()
    #Configurações e alterações possiveis (desenvolver mais tarde)
    aplicar = Button(top, text="Aplicar")
    cancelar = Button(top, text="Cancelar", command = top.destroy)
    aplicar.pack()
    cancelar.pack()
    top.mainloop()

def delete():
    myListBox.delete(ANCHOR)
    #Aqui tem que se eliminar a restrição e não apenas da list box!!!

root = Tk()
root.title("Bloqueador de Programas")
root.iconbitmap('C:/Users/smgon/Phyton/Bloqueador-de-Programas/Sawyer_Pilar.ico')
root.geometry("500x350")
#Ícone do canto superior esquerdo
#root.iconbitmap('@/home/goncalo/Desktop/Python/Bloqueador-de-Programas/Sawyer_Pilar.xbm')

#Estamos a criar uma Label Widget   
myLabel1 = Label(root, text="Lista de restrições de acesso a programas:") #Isto é um Widget, ou seja, um elemento de interação da GUI
#Meter a Label criada anteriormente no ecrã
myLabel1.grid(row=1, column=0)

myButton1 = Button(root, text="Sair", command=root.quit, padx=20, pady=10)  
myButton1.grid(row=10, column=10)

myButton2 = Button(root, text="Eliminar restrição.", command=delete)
myButton2.grid(row=3,column=0)

myButton4 = Button(root, text="Alterar uma restrição de acesso a um programa já existente", command=alteraRestrição)
myButton4.grid(row=4, column=0)

myButton3 = Button(root, text="Criar nova restrição a um novo programa", command=adicionaRestrição)
myButton3.grid(row=5,column=0)

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

#global myListBox
myListBox = Listbox(my_frame, yscrollcommand=my_scrollbar.set, width=30)

my_scrollbar.config(command=myListBox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.grid(row=2, column=0)
myListBox.pack()

restricoes = ["A tua mãe", "Aquela gorda", "A tua prima aquela obesa", "A tua avó parece um camião",
    "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for item in restricoes:
    myListBox.insert(END, item)

root.mainloop()