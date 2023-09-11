#TUPLE :
#TUPLE PROPERTIES :-
'''
   1)It is immutable
   2)it is odered
   3)it can accept the duplicate values
   4)we can do slicing in tuple
   5)we can create homogeneous , heterogeneous and nested tuple
'''
#Tuple  methods:
'''
   1)[:] :- foe slicing
   2)count()
   3)del tuple_name
'''

#fuunctions in Tuple :
'''
   1)type()
   2)len()

'''
mytuple=()
constractTuple=tuple()
homogeneousTuple=(1,3,4,5,2,3,43,23,3)
heterogeneousTuple=("books",10,"pens",12,"markers",3092.3,False,[1,2,3,4,5])
nestedTuple=(1,2,3,4,("books","school","students"),)

#exmple for slicing in tuple
print("to print 1 to 3 index valus",homogeneousTuple[1:3])


heterogeneousTuple.append(15)
print(heterogeneousTuple)
# OUTPUT :->> 'tuple' object has no attribute 'append'

heterogeneousTuple.insert(1,"nani")
print(heterogeneousTuple)
# OUTPUT :->>'tuple' object has no attribute 'insert'

heterogeneousTuple.pop()
print(heterogeneousTuple)
# OUTPUT :->> 'tuple' object has no attribute 'pop'

heterogeneousTuple.pop(1)
print(heterogeneousTuple)
# OUTPUT :->> 'tuple' object has no attribute 'pop'

heterogeneousTuple.remove(10)
print(heterogeneousTuple)
# OUTPUT :->> 'tuple' object has no attribute 'remove'

heterogeneousTuple.clear()
print(heterogeneousTuple)
# OUTPUT :->> 'tuple' object has no attribute 'clear'

# we can count the perticular elimet how many times it repete using count method :
print(heterogeneousTuple.count(10))
print("the size of the tuple",len(heterogeneousTuple))


# reverse the total tuple is posible :
heterogeneousTuple=heterogeneousTuple[::-1]
print(heterogeneousTuple)

# print the ietems in tuple one by one with giving numbers as index with using for loop :
counter=0
for items in heterogeneousTuple:
    counter+=1
    print("The item",counter,"is :",items)

# reverse a Tuple using for loop and slicing :
for items1 in heterogeneousTuple[::-1]:
    print(items1)

# delete the total tuple is polsible
del heterogeneousTuple
print(heterogeneousTuple)












