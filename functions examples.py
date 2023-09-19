#using concadination
def my_function(First_name,Last_name):
    print(First_name + " "+Last_name)
my_function("rakeskh","ramu ") 

# to find youngest child in kids 
def my_function(*kids):
    print("the youngest child is " + kids[1])

my_function("ramu","somu","pavan")

#example using ==
def my_function(child1,child2,child3):
    print("the youngest child is " +child2)
my_function(child1="pavan",child2="prashanth",child3="kumar")

#find kid last name
def my_function(**kid):
    print("his last name is " +kid["lname"])
my_function(fname="kumar",lname="somu")

#exmple of country
def my_function(country=""):
    print("i am from "+country)
my_function("usa")
my_function("london")
my_function("uk")

#using for loop 
def my_function(food):  
    for x in food:
        y=x.upper()
        return y
list1=("apple","banana","mango")
my_function(list1)