from ast import Lambda
from tabnanny import check
from tkinter import *
from turtle import width 
from PIL import ImageTk, Image
from pyparsing import col
from tkinter import messagebox

#
#   O tkinter funciona da seguinte forma:
#   1. Temos que definir um widget (butão, janela, barra, qualquer merda de interação com o user)
#   2. Depois, temos que inserir o widget criado no ecrã da maneira que quisermos 

def verificaArgumentos(clicked0):#Esta função verifica se os parâmetros da nova restrição estão todos satisfeitos

    if clicked0.get() == "Selecione o programa!":#Não foi inserido o programa
        messagebox.showinfo("Erro ao criar nova restrição!", "O nome do programa que quer restringir tem de ser inserido.")
        return 0
    
    return 1

def aplicaNovaRestrição(clicks, variables, top, myListBox, clicked0, fRestriçoes):
    
    value = verificaArgumentos(clicked0)

    #Variables-> Dias da semana em que a restrição se aplica
    #Clicks-> As horas de cada dia em que a restrição se aplica
    #top-> janela secundária a fechar no final
    #myListBox-> uma lista que mostra todas as restrições ativas
    #clicked0-> nome do programa ao qual a nova restrição se aplica

    if (variables[0].get() == 1) and value == 1:#Todos os dias
        horas = []
        horas.append(clicks[0].get() + ":" + clicks[1].get())
        horas.append(clicks[2].get() + ":" + clicks[3].get())
        myListBox.insert(END, clicked0.get() + " bloqueado todos os dias das " + horas[0] + " ate as " + horas[1])
        fRestriçoes.write(clicked0.get() + " bloqueado todos os dias das " + horas[0] + " ate as " + horas[1] + "\n")
        fRestriçoes.flush()
    else:
        if (variables[1].get() == 1):#Segunda-feira
            horas = []
            horas.append(clicks[4].get() + ":" + clicks[5].get())
            horas.append(clicks[6].get() + ":" + clicks[7].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Segunda-feira das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Segunda-feira das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[2].get() == 1):#Terça-feira
            horas = []
            horas.append(clicks[8].get() + ":" + clicks[9].get())
            horas.append(clicks[10].get() + ":" + clicks[11].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Terca-feira das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Terca-feira das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[3].get() == 1):#Quarta-feira
            horas = []
            horas.append(clicks[12].get() + ":" + clicks[13].get())
            horas.append(clicks[14].get() + ":" + clicks[15].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Quarta-feira das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Quarta-feira das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[4].get() == 1):#Quinta-feira
            horas = []
            horas.append(clicks[16].get() + ":" + clicks[17].get())
            horas.append(clicks[18].get() + ":" + clicks[19].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Quinta-feira das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Quinta-feira das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[5].get() == 1):#Sexta-feira
            horas = []
            horas.append(clicks[20].get() + ":" + clicks[21].get())
            horas.append(clicks[22].get() + ":" + clicks[23].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Sexta-feira das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Sexta-feira das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[6].get() == 1):#Sábado
            horas = []
            horas.append(clicks[24].get() + ":" + clicks[25].get())
            horas.append(clicks[26].get() + ":" + clicks[27].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Sabado das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Sabado das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush()
        if (variables[7].get() == 1):#Domingo
            horas = []
            horas.append(clicks[28].get() + ":" + clicks[29].get())
            horas.append(clicks[30].get() + ":" + clicks[31].get())
            myListBox.insert(END, clicked0.get() + " bloqueado na Domingo das " + horas[0] + " ate as " + horas[1])
            fRestriçoes.write(clicked0.get() + " bloqueado na Domingo das " + horas[0] + " ate as " + horas[1] + "\n")
            fRestriçoes.flush() 
    top.destroy()

def ativarOptionMenu(optionMenus, number, var1):
    
    i=0
    while(i<4):
        optionMenus[number+i].configure(state = NORMAL)
        i=i+1

def adicionaRestrição(myListBox, fRestriçoes):
    top = Toplevel()
    top.title("Bloqueador de programas") 
    #top.iconbitmap('C:/Users/smgon/Phyton/Bloqueador-de-Programas/Sawyer_Pilar.ico')
    top.geometry("900x500")

    lab0 = Label(top, text="Programa a restringir:")
    lab0.grid(row=0, column=0)

    #Melhor isto, arranjar uma maneira de fazer aparecer a lista de programas instalados e possíveis de bloquear
    programas = ["League of Legends", "Discord", "Opera Internet Browser"]

    clicked0 = StringVar()
    clicked0.set("Selecione o programa!")
    drop0 = OptionMenu(top, clicked0, *programas)
    drop0.grid(row=0, column=1)

    i = 0
    optionMenus = []
    clicks = []
    while i < 8:       
        lab1 = Label(top, text="Bloquear das")
        lab2 = Label(top, text=":")
        lab3 = Label(top, text="até às") 
        lab1.grid(row=i+1, column=1)
        lab2.grid(row=i+1, column=3)
        lab3.grid(row=i+1, column=5)

        options1 = ["00",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        options2 = ["00", 30]

        clicked1 = StringVar()
        clicked1.set(options1[0])

        clicked2 = StringVar()
        clicked2.set(options2[0])

        clicked3 = StringVar()
        clicked3.set(options1[0])

        clicked4 = StringVar()
        clicked4.set(options2[0])

        drop1 = OptionMenu(top, clicked1, *options1)
        drop1.grid(row=i+1,column=2)
        drop1.configure(state=DISABLED)

        drop2 = OptionMenu(top, clicked2, *options2)
        drop2.grid(row=i+1, column=4)
        drop2.configure(state=DISABLED)

        drop3 = OptionMenu(top, clicked3, *options1)
        drop3.grid(row=i+1,column=6)
        drop3.configure(state=DISABLED)

        drop4 = OptionMenu(top, clicked4, *options2)
        drop4.grid(row=i+1, column=8)
        drop4.configure(state=DISABLED)

        optionMenus.append(drop1)
        optionMenus.append(drop2)
        optionMenus.append(drop3)
        optionMenus.append(drop4)

        clicks.append(clicked1)
        clicks.append(clicked2)
        clicks.append(clicked3)
        clicks.append(clicked4)

        i = i+1

    var1 = IntVar() 
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    c1 = Checkbutton(top, text="Todos os dias", variable= var1, command=lambda: ativarOptionMenu(optionMenus, 0, var1))
    c2 = Checkbutton(top, text="Segunda-feira", variable= var2, command=lambda: ativarOptionMenu(optionMenus, 4, var1))
    c3 = Checkbutton(top, text="Terça-feira", variable= var3, command=lambda: ativarOptionMenu(optionMenus, 8, var1))
    c4 = Checkbutton(top, text="Quarta-feira", variable= var4, command=lambda: ativarOptionMenu(optionMenus, 12, var1))  
    c5 = Checkbutton(top, text="Quinta-feira", variable= var5, command=lambda: ativarOptionMenu(optionMenus, 16, var1)) 
    c6 = Checkbutton(top, text="Sexta-feira", variable= var6, command=lambda: ativarOptionMenu(optionMenus, 20, var1))
    c7 = Checkbutton(top, text="Sábado", variable= var7, command=lambda: ativarOptionMenu(optionMenus, 24, var1))
    c8 = Checkbutton(top, text="Domingo", variable= var8, command=lambda: ativarOptionMenu(optionMenus, 28, var1))
    c1.grid(row=1,column=0)
    c2.grid(row=2,column=0)
    c3.grid(row=3,column=0)
    c4.grid(row=4,column=0)
    c5.grid(row=5,column=0)
    c6.grid(row=6,column=0)
    c7.grid(row=7,column=0)
    c8.grid(row=8,column=0)
    
    variables = [var1,var2,var3,var4,var5,var6,var7,var8]

    aplicar = Button(top, text="Aplicar", command=lambda: aplicaNovaRestrição(clicks, variables, top, myListBox, clicked0, fRestriçoes))
    aplicar.grid(row=10,column=10)
    cancelar = Button(top, text="Cancelar", command=top.destroy)
    cancelar.grid(row=10,column=11)

    top.mainloop()

def delete(myListBox):
    programa = myListBox.get(ANCHOR)
    myListBox.delete(ANCHOR)
    fRead = open('restrições.txt', 'r')
    lines = fRead.readlines()
    fRead.close()
    fWrite = open('restrições.txt', 'w')
    for line in lines:
        if line.strip("\n") != programa:
            fWrite.write(line)
    fWrite.flush()
    fWrite.close()

##################################################################################################################################################################################

fRestriçoes = open('restrições.txt', 'r+')# r+ -> read and write the file

root = Tk()
root.title("Bloqueador de Programas")
#root.iconbitmap('C:/Users/smgon/Phyton/Bloqueador-de-Programas/Sawyer_Pilar.ico')
root.geometry("650x350")
#Ícone do canto superior esquerdo
#root.iconbitmap('@/home/goncalo/Desktop/Python/Bloqueador-de-Programas/Sawyer_Pilar.xbm')

#Estamos a criar uma Label Widget   
myLabel1 = Label(root, text="Lista de restrições de acesso a programas:") #Isto é um Widget, ou seja, um elemento de interação da GUI
#Meter a Label criada anteriormente no ecrã
myLabel1.grid(row=1, column=0)


my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

myListBox = Listbox(my_frame, yscrollcommand=my_scrollbar.set, width=70)
lines = fRestriçoes.readlines()
for line in lines:
    myListBox.insert(END, line)

my_scrollbar.config(command=myListBox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.grid(row=2, column=0)
myListBox.pack()

myButton1 = Button(root, text="Sair", command=root.quit, padx=20, pady=10)  
myButton1.grid(row=10, column=10)

myButton2 = Button(root, text="Eliminar restrição a restrição selecionada.", command=lambda: delete(myListBox))
myButton2.grid(row=3,column=0)

#myButton4 = Button(root, text="Alterar a restrição selecionada.", command = lambda: alteraRestrição(myListBox, fRestriçoes))
#myButton4.grid(row=4, column=0)

myButton3 = Button(root, text="Criar nova restrição a um novo programa.", command=lambda: adicionaRestrição(myListBox, fRestriçoes))
myButton3.grid(row=5,column=0)

root.mainloop()

fRestriçoes.close()