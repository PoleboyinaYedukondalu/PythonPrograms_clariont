#File handling concepts 
#written by Yedukondalu

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


#example of write line method :
file1.writelines(["items nani"])
file1.writelines("items nani")