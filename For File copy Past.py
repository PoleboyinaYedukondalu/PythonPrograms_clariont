#File handling concepts 
#written by Yedukondalu

# to copy and past the file one location to another location without removing orginal file location :
import os
import shutil

#Createing a new folder :
os.mkdir("d:\\FilecopyYD")

#Current Working Directory :
os.chdir("d:\\FilecopyYD")

#Storing Source Path in one variable
sourcePath= "C:\Users\poleb\Downloads\FILE SYSTEM.pdf"

#Storing destination Path in one variable
destPath = "\d:\\FilecopyYD\\File_System.pdf"

#copy the file into one directory into another directory(one destination to another destination) :
shutil.copy(sourcePath,destPath)