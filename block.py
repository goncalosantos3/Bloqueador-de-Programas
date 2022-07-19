#Objetivo: Bloquear o lol entre as 8 e as 20
import time
import datetime
import winreg as reg
import os            
import re
 
def AddToRegistry():
 
    # in python __file__ is the instant of
    # file path where it was executed
    # so if it was executed from desktop,
    # then __file__ will be
    # c:\users\current_user\desktop
    pth = os.path.dirname(os.path.realpath(__file__))
     
    # name of the python file with extension
    s_name = "mYscript.py"    
     
    # joins the file name to end of path address
    address = os.path.join(pth,s_name)
     
    # key we want to change is HKEY_CURRENT_USER
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
     
    # open the key to make changes to
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
     
    # modify the opened key
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)
     
    # now close the opened key
    reg.CloseKey(open)
 
def verificaRestrições():

    listaRestrições = []
    restrições = open('restrições.txt', 'r')
    lines = restrições.readlines()
    now = datetime.datetime.now().time()
    diaDaSemana = datetime.datetime.now()

    for line in lines:

        list = re.split("bloqueado", line)
        programa = list[0].strip(" ")

        if re.search("todos os dias", line) != None:#A restrição é aplicada todos os dias
            hora1 = re.split(" ate", line)
            hora1 = re.split("das ", hora1[0])
            hora1 = hora1[1]
            hora2 = re.split(" as ", line)
            hora2 = hora2[1].strip("\n")
            hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
            hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
            if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                listaRestrições.append(programa)
        else:
            if re.search("Segunda-feira", line) != None and diaDaSemana == 0:#A restrição é aplicada na Segunda-feira
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Terca-feira", line) != None and diaDaSemana == 1:#A restrição é aplicada na Terça-feira
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Quarta-feira", line) != None and diaDaSemana == 2:#A restrição é aplicada na Quarta-feira
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Quinta-feira", line) != None and diaDaSemana == 3:#A restrição é aplicada na Quinta-feira
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")   
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Sexta-feira", line) != None and diaDaSemana == 4:#A restrição é aplicada na Sexta-feira
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")     
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Sabado", line) != None and diaDaSemana == 5:#A restrição é aplicada no Sábado
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
            if re.search("Domingo", line) != None and diaDaSemana == 6:#A restrição é aplicada no Domingo
                hora1 = re.split(" ate", line)
                hora1 = re.split("das ", hora1[0])
                hora1 = hora1[1]
                hora2 = re.split(" as ", line)
                hora2 = hora2[1].strip("\n")
                hora1 = datetime.datetime.strptime(hora1, '%H:%M').time()
                hora2 = datetime.datetime.strptime(hora2, '%H:%M').time()
                if hora1 < now and now < hora2:#Estamos dentro do horário da restrição
                    listaRestrições.append(programa)
    
    restrições.close()
    return listaRestrições

def main():
    
    AddToRegistry()
    while 1:

       restrições = verificaRestrições()
       now = datetime.datetime.now().time()

       for programa in restrições:
            os.system("TASKKILL /F /IM " + programa + ".exe") # select process by its names
            time.sleep(30)

# Driver Code
if __name__ == "__main__":
    main()

#elif now < ini: 
#    tdelta = ini - now
#    time.sleep(tdelta.total_seconds())
#elif now > fim:
#    tdelta = meia_noite - now
#    tdelta += ini -meia_noite
#    time.sleep(tdelta.total_seconds())