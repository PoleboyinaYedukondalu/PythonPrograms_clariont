import numpy as np
# =>CREATING 1D & 2D ARRAYS :
# Creating a 1D array
arr1d = np.array([1, 2, 3])
# Creating a 2D array
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr1d)
print(arr2d[0][1])

# -----------------------------------------------------------------------
# =>RESHAPING :
# second example Reshape to 2x3 array
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)

# -----------------------------------------------------------------------
# =>DIMENTION CHECKING :
# checking the shape and dimension of an array.
print(arr1d.shape)  # (3,)
print(arr2d.shape)  # (2, 3)

print(arr1d.ndim)  # 1
print(arr2d.ndim)  # 2

# ------------------------------------------------------------------------
# =>ARRAY OPERATIONS :
# NumPy allows element-wise operations on arrays.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Addition
result = arr1 + arr2
print(result)  # [5, 7, 9]
# Element-wise multiplication
result = arr1 * arr2
print(result)  # [4, 10, 18]

# --------------------------------------------------------------------------
# =>STATICAL OPERATIONS :l
# NumPy provides various statistical functions.
arr = np.array([1, 2, 3, 4, 5])
# Mean :
mean_value = np.mean(arr)
print(mean_value)
# Sum :
sum_value = np.sum(arr)
print(sum_value)

# ----------------------------------------------------------------------------
# =>INDEXING AND SLICING :
# Accessing and manipulating specific elements in an array.
arr = np.array([0, 1, 2, 3, 4, 5])

# Accessing an element
print(arr[2])  # 2
# Slicing
print(arr[1:4])  # [1, 2, 3]

