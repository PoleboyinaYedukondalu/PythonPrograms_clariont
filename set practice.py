setA = {1,2,3,4,5}
setB = {4,5,6,7,8}

setA.add(7)
print(setA)

setA.discard(7)
print(setA)


# example for union :
print("The union of setA and setB :",setA.union(setB))

print("The size of unioun of setA and setB :",len(setA.union(setB)))




#multiple Set Oparations :-

setC=setA.union(setB)
setC.remove(5)
print(setC)

#intersection of setA and setB is :
print("The intersection of setA and SetB",setA.intersection(setB))

#differece of setA and SetB is :
print("The difference of setA and SetB",setA.difference(setB))

#difference of setB and setA is :
print("The difference of setB and SetA",setB.difference(setA))

#symatric Difference of setA and setB is :
print("The symetricDifference of setA and SetB",setA.symmetric_difference(setB))

#subset of setA and setB is :
print("the subset of setA and setB is :",setB.issubset(setA))

#subset of setA and setB is :
print("the superset of setA and setB is :",setA.issuperset(setB))
