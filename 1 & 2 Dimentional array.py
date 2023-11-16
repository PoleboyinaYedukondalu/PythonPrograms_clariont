import numpy as np
# Creating a 1D array
arr1d = np.array([1, 2, 3])

# Creating a 2D array
arr2d = np.array([[1, 2, 3],[4, 5, 6],[5,8,9]])
print(type(arr2d))

print("1 dimentional array : ",arr1d)
print("2 dimentional array : ",arr2d)

# Checking the shape and dimension of an array.
print("Shap of array1 : ",arr1d.shape)  # (3,)
print("Shap of array2 : ",arr2d.shape)  # (2, 3)

print("Checking the dimention of array1 :",arr1d.ndim)  # 1
print("Checking the dimention of array2 :",arr2d.ndim)  # 2

print(arr1d.size)