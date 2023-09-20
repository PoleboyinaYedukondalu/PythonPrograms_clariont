#File handling concepts 
#written by Yedukondalu

#to append new text to the existing file,if the file doesn't exist it will creat a new file : 
file1 = open("d:\\Handling\\new.txt","a")
print(file1.write("i am writing about FileHandling concept"))
#to read & append new text to the existing file if the file doesn't exist it will creat a new file :
file1 = open("d:\\Handling\\new2.txt","a+")
print(file1.write(" 'a'+ is read and append mode"))
print("the information in new.txt file is :-",file1.read())

file1.writelines()