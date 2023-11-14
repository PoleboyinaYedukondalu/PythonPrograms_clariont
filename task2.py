# importing a specific function in that module 

from My_Module import multiplication

value1 = float(input("enter value 1 :"))
value2 = float(input("enter value 2 :"))
multiplication_Value = multiplication(value1,value2)
print(f"multiplication of {value1} & {value2} is : {multiplication_Value}")

