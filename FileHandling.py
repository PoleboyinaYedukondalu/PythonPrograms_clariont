#File handling concepts 
#written by Yedukondalu

#importing os packages :
import os 

#to create a new director :
os.mkdir("d:\\Handling")

#to remove existing directory
os.removedirs("d://Handling")

#to know the which files are there in given directory
print("the current directory is :",os.listdir("d:\\Handling"))

#to remove peticular files in existing directory :
os.remove("d:\\files\\pawan.txt")
print("the current directory is :",os.listdir("d:\\files"))


#to write content in existing file this metho re write the total matter in that file, is the file dosen't exist
# it can creat a new file : 
file1 = open("d:\\Handling\\new.txt","w")
print(file1.write("hii this is nani"))
# to write multiple lines in existing file :
file2=open("d:\\Handling\\new.txt","w")
print(file2.write('''
Hii this is nani ,
i am writing file handling concept,
Thank you..'''))
#to read & write new text to the existing file if the file doesn't exist it will creat a new file, if the file doesn't exist it will creat a new file :
file1 = open("d:\\Handling\\new2.txt","w+")
print(file1.write(" 'a'+ is read and append mode"))
print("the information in new.txt file is :-",file1.read())



#to append new text to the existing file :
file1 = open("d:\\Handling\\new.txt","a")
print(file1.write("i am writing about FileHandling concept"))
#to read & append new text to the existing file if the file doesn't exist it will creat a new file :
file1 = open("d:\\Handling\\new2.txt","a+")
print(file1.write(" 'a'+ is read and append mode"))
print("the information in new.txt file is :-",file1.read())


#to read alredy existing file :
file1 =open("d:\\Handling\\new.txt","r")
print("the information in new.txt file is :-",file1.read())
#to read and write mode, but it did't create a new file if the file is doesn't exist :
file1 =open("d:\\Handling\\new.txt","r+")
#to read the file :
print("the information in new.txt file is :-",file1.read())
#to write the file :
print("the information in new.txt file is :-",file1.write("this is"))

#to create a new file in existing directory 
file1=open("d:\\Handling\\new.txt","x")


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



# to cut and past the file into one location to another location with the name changing of that file : 
import os
import shutil

#Createing a new folder :
os.mkdir("d:\\FilecopyYD")

#Current Working Directory :
os.chdir("d:\\FilecopyYD")

srcPath = "d:\\\FileConcept1.pdf"
destpath= "d:\\FilecopyYD\\FileHandling.pdf"
os.rename(srcPath,destpath)


