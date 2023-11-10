mylist = [1,2,3,4,5,4]

mylist.append(6)
print(mylist)

print("index of 2 : ",mylist.index(3))

mylist.insert(1,100)
print(mylist)

mylist.pop()
print(mylist)

mylist.pop(1)
print(mylist)

print(mylist.count(4))

mylist.reverse()
print(mylist)

mylist[1]="nani"
print(mylist)

mylist.clear()
print()

del mylist