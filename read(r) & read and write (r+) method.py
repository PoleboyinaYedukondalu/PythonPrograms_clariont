#File handling concepts 
#written by Yedukondalu

#to read alredy existing file :
file1 =open("d:\\Handling\\new.txt","r")
print("the information in new.txt file is :-",file1.read())
#to read and write mode, but it did't create a new file if the file is doesn't exist :
file1 =open("d:\\Handling\\new.txt","r+")
#to read the file :
print("the information in new.txt file is :-",file1.read())
#to write the file :
print("the information in new.txt file is :-",file1.write("this is"))