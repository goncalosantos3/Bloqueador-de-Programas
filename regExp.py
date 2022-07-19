import re
from datetime import datetime

string = "Discord bloqueado todos os dias das 00:00 ate as 10:00"
hora1 = re.split(" ate", string)
hora1 = re.split("das ", hora1[0])
hora1 = hora1[1]
hora2 = re.split(" as ", string)
hora2 = hora2[1].strip("\n")
print(hora1)
print(hora2)