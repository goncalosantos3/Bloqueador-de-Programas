#Objetivo: Bloquear o lol entre as 8 e as 20
import time
import datetime
import winreg as reg
import os            
 
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
 
def main():
    AddToRegistry()
    ini = datetime.time(8,0)

    fim = datetime.time(20,0)

    meia_noite = datetime.time(0,0)

    while 1:
        now = datetime.datetime.now().time()
        if now > ini and now < fim:
            os.system("TASKKILL /F /IM LeagueClient.exe") # select process by its names
            time.sleep(30)
        else:
            exit()

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