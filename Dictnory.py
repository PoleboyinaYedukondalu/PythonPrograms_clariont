#Dictnory :
'''
   1)it is unodered
   2)it is key pair values,it accepts duplicate values but don't accept duplicate keys
   3)dict accept tuple as key another advanced datatypes don't accept like list,set,dict ect..
   4)we can create homogeneous, heterogeneous and nested dict also.
   5)it is mutabl
'''

emptyDict = dict()

myDict={'name':"nani",
        'working details':{'company':"clariont",'salary':15000,
                           'role':"python developer",'location':"madhapur,hydrabad",},
        (1,2):{'mango','apple'},
        2:['vizag','kerala','banglore'],
        3:['vizag','kerala','banglore']
        }
#to update the value  using keys :
myDict.update({3:[5,6,7,8,9]})
print("after updating the mydict using update method :",myDict)

#to get the total items in myDict :
print("the total items in mydict :",myDict.items())

#to get all keys in the myDict :
print("the total keys in myDict is :",myDict.keys())

#to get all the values in myDict is :
print("the total values inmyDict is :",myDict.values())

#to get the perticular value in myDict is :
print("to get the perticular value in myDict",myDict.get('name'))
print(myDict)
#to delete perticular ietem using keys with pop item method :
print("to delete perticular eliment in myDict is :",myDict.pop(3))
print(myDict)

#to print the perticular eliment in myDict is :
print("to get the perticular value in the myDict is :",myDict["name"])

#to know the size of the dict :
print("the size of the mydict is :",len(myDict))

#to know the type of the dict :
print("the size of the mydict is :",type(myDict))

print("the size of the mydict is :",type(myDict["working details"]))

print("the size of the mydict is :",type(myDict[(1,2)]))

print("the size of the mydict is :",type(myDict[2]))

#example of deepcopy(it store in different location that means u do changes in copy but it don't change in original dict) in mydict is :
urDict=myDict.copy()
print("the copy of mydict is :",urDict)
urDict.pop('name')
print("after doing delete in urdict :",urDict)
print("the orginal dict is :",myDict)

#example of ShallowCopy(it stores in same memory location if wu change in one copy it will also change orginal copy) is : 
Shallow_Copy=myDict
print("the orginal_copy all ietms are :",myDict)
print("the shallow_copy all items are :",Shallow_Copy)
Shallow_Copy.pop(2)
print("the orginal_copy all ietms are :",myDict)
print("the shallow_copy all items are :",Shallow_Copy)


#to clear all  the items in dict :
myDict.clear()
print("the items in dict is :",myDict)

#to delete the total dict with structure also :
del myDict
print("the items in  mydict is :",myDict)





