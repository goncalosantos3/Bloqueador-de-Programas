import re
from datetime import datetime

string = "Discord bloqueado todos os dias das 00:00 até às 10:00"
hora1 = re.split(" até", string)
hora1 = re.split("das ", hora1[0])
hora1 = hora1[1]
hora2 = re.split("às ", string)
hora2 = hora2[1].strip("\n")
print(hora1)
print(hora2)