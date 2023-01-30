# NumPy is a Python library.

# NumPy is used for working with arrays.

# NumPy is short for "Numerical Python".


import numpy as np

# print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

arr = np.array([[1, 2, 3], [4, 5, 6]])

""" arr = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ], 
    [
        [1, 2, 3], [4, 5, 6]
    ]
])
print(arr[0,0,0])
print(arr.ndim) """


arr = np.array([10, 15, 20, 25, 30, 35, 40])

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)

# print(arr[1:4:2])
# print(arr[1:6:1])
# print(arr[1:6:2])
# print(arr[::3])
# print(arr[2:5])
# print(type(arr))



arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])
# print(arr[::2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2]) # from both element, return index 2 value

# print(arr[0:2, 1:4]) #From 1st elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# print(arr[0:2, :4]) #From 1st elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# print(arr[0:2, 1:4]) #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:




# The main difference between a copy and a view of an array is that 
# the copy is a new array, and the view is just a view of the original array.
# The copy owns the data and any changes made to the copy will not affect original array, 
# and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, 
# and any changes made to the original array will affect the view.


arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
# print(x)
# print(arr)



arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
# print(arr)
# print(x)




arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 4)
newarr = arr.reshape(4, 3)

print(newarr)


























































