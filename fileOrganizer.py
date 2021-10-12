import os
import shutil

path= input("Enter name of the directory to be sorted: ")

listOfFiles = os.listdir(path)

for file in listOfFiles : 
    name, ext = os.path.splitext(file)

    ext = ext[1:] 
    if ext == "" :
        continue
    if os.path.exists(path + "/" + ext) :
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.mkdir(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
