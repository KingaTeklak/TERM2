
import time
import datetime
import sys
import os

#path = sys.argv[1]

#path = "C:/Users/kinga/Desktop/studia/SEM2"

def last_modification(path = sys.argv[1]):

    calender = {"01":0, "02":0, "03":0, "04":0,"05":0, "06":0, "07":0, "08":0,"09":0, "10":0, "11":0, "12":0}
    for x in os.listdir(path):
        temporary_path = str(path)+"/"+str(x)
        modificationTime = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(temporary_path)))
        print("Last Modified Time : ", modificationTime )
        year = modificationTime[6:]
        month = modificationTime[3:5]

        if year == "2021":
            calender[month] += 1
    return calender

print(last_modification())
