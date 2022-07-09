from tkinter import * 

#
#   O tkinter funciona da seguinte forma:
#   1. Temos que definir um widget (butão, janela, barra, qualquer merda de interação com o user)
#   2. Depois, temos que inserir o widget criado no ecrã da maneira que quisermos 


def terminaExe():
    exit()

def adicionaRestrição():
    top = Toplevel()
    top.title("Bloqueador de programas") 
    aplicar = Button(top, text="Aplicar")
    aplicar.grid(row=10,column=10)
    cancelar = Button(top, text="Cancelar", command=top.destroy)
    cancelar.grid(row=10,column=11)
    top.mainloop()


def alteraRestrição():
    top = Toplevel()
    top.title("Bloqueador de programas") 
    e = Entry(top, width=50)
    e.insert(0, "Nome do programa a alterar: ")
    e.pack()
    aplicar = Button(top, text="Aplicar", command = e.get)
    cancelar = Button(top, text="Cancelar", command = top.destroy)
    aplicar.pack()
    cancelar.pack()
    top.mainloop()

root = Tk()
root.title("Bloqueador de Programas")

#Estamos a criar uma Label Widget   
myLabel1 = Label(root, text="Lista de restrições de acesso a programas:") #Isto é um Widget, ou seja, um elemento de interação da GUI
#Meter a Label criada anteriormente no ecrã
myLabel1.grid(row=0, column=0)

myButton1 = Button(root, text="Sair", command=terminaExe, padx=20, pady=10)  
myButton1.grid(row=10, column=10)

myButton2 = Button(root, text="Criar nova restrição a um novo programa", command=adicionaRestrição)
myButton2.grid(row=1,column=0)

myButton3 = Button(root, text="Alterar uma restrição de acesso a um programa já existente", command=alteraRestrição)
myButton3.grid(row=2, column=0)

root.mainloop()