#writelines method in files concept
#written by Yedukondalu

file1=open("d:\\Handling\\new.txt","w+")
file1.write("welcome to my file world :")

# file1=open("d:\\Handling\\new.txt","w+")
file1.write("trip")
list1=["friuts","veggies","s@i"]
for items in list1:
    file1.writelines(items)

file1.writelines(["items nani"])
file1.writelines("items nani")
