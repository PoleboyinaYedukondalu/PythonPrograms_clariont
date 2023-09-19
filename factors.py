# write a programm to find out the common factors for 50 and 60 ?

#Defining A Function
def Factors(num1,num2):
    for i in range(1,num1 and num2):
        if num1%i==0 and num2%2==0:
            print("Common Factors For 50 & 60 Are:-",i)

#Calling The Function
Factors(50,60)
