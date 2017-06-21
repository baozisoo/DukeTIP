import numpy as np

# 5 x 4 array with all ones
array1 = np.ones((5,4))
print array1

# 5 x 1 array of [1, 0, 0, 0, 0]
array2 = np.zeros((5, 1))
array2[0]= 1
print array2

# Multiply 5 x 4 and 5 x 1
print array1 * array2

#Change 3rd item in row 2 to 10
array1[2,1] = 10
print array1

#5 x 4 array times 2
print array1 * 2

#5 x 4 array sum of everything
print (array1.sum())

#5 x 4 array sum of rows
print (array1.sum(axis = 1))

#5 x 4 array sum of columns
print (array1.sum(axis = 0))