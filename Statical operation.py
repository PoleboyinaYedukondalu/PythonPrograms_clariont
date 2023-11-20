import numpy as np 
# NumPy provides various statistical functions.

arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([1,2,3,4,5])
# Mean :
mean_value = np.mean(arr)
print(f"mean of {mean_value}  is :\n",mean_value)
# Sum :
sum_value = np.sum(arr)
print(f"sum of {arr} is : \n",sum_value)
# multiplicationm:
multiplication = np.multiply(arr,arr1)
print(f"multiplication of {arr} & {arr1} is :\n",multiplication)

division_arr = np.divide(arr,arr1)
print(f"division of {arr} & {arr1} is : \n",division_arr)
