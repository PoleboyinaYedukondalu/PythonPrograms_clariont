import numpy as np

arr1d = np.array([1, 2, 3])
arr2d = np.array([[[1, 2, 3],[4, 5, 6],[8,9,10]]])
print(arr2d[::-1])
# print(sum(arr1d))


# Simple example Reshape to 2x3 array
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)