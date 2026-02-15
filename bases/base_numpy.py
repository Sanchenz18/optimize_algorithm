import numpy as np

# native python list
py_list = [1, 2, 3, 4, 5]
print(py_list * 2)  # opration: double the list

# numpy array
np_array = np.array([1, 2, 3, 4, 5])
print(np_array * 2)  # computation: double each element in the array

# scalar * array
result = 0.618 * np_array
print(result)
