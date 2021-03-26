# !/usr/bin/python3

from zipfile import ZipFile
import os
from os.path import basename
import datetime
import sys


Current_Date = datetime.datetime.today().strftime ('%d_%b_%Y')

#path = "C:/Users/kinga/Desktop/studia/SEM2/PROGRAMOWANIE"
#my_path = "C:/Users/kinga/Desktop/studia/SEM2"
path = sys.argv[1]
my_path = sys.argv[2]
zip_path = f"{my_path}/{Current_Date}copy.zip"
with ZipFile(zip_path, "w") as zipObj:
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename == "{}copy.zip".format(Current_Date):
                continue
            filePath = os.path.join(folderName, filename)
            zipObj.write(filePath, basename(filePath))
