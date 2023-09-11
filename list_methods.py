""" program describing
    written on 06-09-23
    written by Nani
"""
# LIST :- TO STROE ACOOLECTION OF ITEMS IN A SINGLE VARIABLE
# LIST ATTRIBUTES :-
'''
    # 1)List is mutable
    # 2)it is ordered
    # 3)it has forword and reverse index
    # 4)we can do slicing in list
    # 5)we can creat homogeneous, heterogeneous and nested list
    # 6)
'''
#LIST ALL METHODS :-
'''
    1)append(item)
    2)insert(index,item)
    3)pop()
    4)pop(index)
    5)extand(item)
    5)del list_name
    6)del list_name[index]
    7)clear()
    8)remove(item)
    9)copy()
    10)short()
    11)shorted()
'''

#list Functions :-
'''
   1)type()
   2)len()
'''

#EXAMPLES OF LIST METHODS AND FUNCTIONS

list1 =["nani p","sai","surya",10,11,12,11,"nani",["chanikya","pawan"],13,14,"dhurga",15,"sowjanya",16,11]
print("total list :",list1)
list2=[1,2,3,4,5,6,7]

# example of append method in list :
list1.append(25)
print("after appending 25 value :",list1)

#example of insert method in list :
list1.insert(-5,["vijaya"])
print("after inserting names list :",list1)

list1[-6].insert(1,"sishva")
print("after inserting names list :",list1)

#example of pop() method in list :
list1.pop()
print("after inserting names list :",list1)

#example of pop index method in list :
list1.pop(4)
print("delete the perticular eliment using pop index method :",list1)

#example of extand method in list  :
list1.extend(list2)
print("after extand method the list1 is :",list1)
#example of count method in list :
print(list1.count(11))

#example of remove method in list :
list1.remove(11)
print("after deleting the perticular item in a list using romove method :")


#example of clear method in list :
list1.clear()
print("after clearing all eliment in list using clear method :",list1)

list1.remove(11)
print("after deleting the perticular item in a list using romove method :")

counter=0
for items in list1:
    counter+=1
    print("The item",counter,"is :",items)




















