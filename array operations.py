import numpy as np
# NumPy allows element-wise operations on arrays :
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
twodarray = np.array([[1,2,3,4],[5,6,7,8]])

# using dot operator :
result1 = np.dot(arr1,arr2);
print("using dot operator :",result1)

# Addition :
result = arr1 + arr2
print(f" addition of two arrays {result} ")  # [5, 7, 9]

# Element-wise multiplication :
result = arr1 * arr2
print(f" multiplication of two arrays {result} ") # [4, 10, 18]

# squaring the two different arrays :
result = arr1 ** arr2
print(f" square of two arrays {result} ")

# transpose the array, in this case rows will becomes columns coloumns will becomes : 
transposedarray = np.transpose(twodarray)
print("original array : ",twodarray)
print("transposed array : ",transposedarray)