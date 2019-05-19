import os
import sys
from shutil import copyfile

# Задача 1
folders = ("dir_1", "dir_2", "dir_3", "dir_4",
           "dir_5", "dir_6", "dir_7", "dir_8", "dir_9")

for folder in folders:
    os.mkdir(folder)
for folder in folders:
   os.rmdir(folder)

# Задача 2
for direct in os.listdir():
    if os.path.isdir(direct) == True:
        print(direct)

# Задача 3
    copyfile("easy5.py", "copy_easy5.py")
