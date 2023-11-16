import numpy as np 

array1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
transposedarray = np.transpose(array1)
print("transposed array : \n",transposedarray)

print("dimention of array1 : ",array1.ndim)
print("shape of array1 : ",array1.shape)

array2 = np.zeros([3,3])
print(array2)

# Create an identity matrix
identity_matrix = np.eye(4)
print("\nIdentity Matrix:")
print(identity_matrix)

array3 = np.ones((3,3))
print(array3)

