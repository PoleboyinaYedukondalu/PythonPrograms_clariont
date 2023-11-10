mystring="hii this is nani"
# mystring[0]='H' #string is immutable we can't change charecters in a string we can change entire string
print(mystring[::-5]) #it can print leaving 4 charecter in the reverse orderd

print(mystring.capitalize()) #it can convert the string first letter in capital like title()

print(mystring.count("i")) #it can give the duplicate count of given charecter

print("index of i : ",mystring.find('i')) #give the t index in the string
print("index of i : ",mystring.index("i")) #give the t index in the string
print(mystring)

print(mystring.isupper())
print(mystring.islower())
print(mystring.isalnum())
print(mystring.isalpha())
print(mystring.isnumeric())

# setA = {1,2,3,4,5}
# setB = {4,5,6,7,8}
# setA.difference_update(setB)
# print(setA)
# print(setB)


