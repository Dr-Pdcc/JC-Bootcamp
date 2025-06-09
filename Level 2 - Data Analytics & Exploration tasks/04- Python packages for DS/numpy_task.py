import numpy as np

'''
Question 1:
Why doesn't np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)
create a two-dimensional array? Write it the correct way.

Answer:

The line above does not work because np.array() expects a single 
iterable, such as a list or a tuple. This means that the arguments are passed
separately instead of being grouped into a single tuple or list. 

Also, the dtype argument is incorrectly placed inside one of the inner tuples. 
'''


# In x1 (correct approach) each inner tuple represents a row of the 2D array
# and dtype=float ensure that all elements in the array are of type float.
x1 = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print("_" * 70)
print(f"\n\033[1mAnswer Q1:\033[0m\n{x1}")


'''
Question 2:
What is the difference between a = np.array([0, 0, 0]) and a =
np.array([[0, 0, 0]])?

Answer:
a = np.array([0, 0, 0]) - 1D array (vector) with 3 elements.
Demonstrated in the code below as x2a

a = np.array([[0, 0, 0]]) - 2D array with 1 row and 3 columns.
Demonstrated in the code below as x2b
'''


x2a = np.array([0, 0, 0])
x2b = np.array([[0, 0, 0]])
print("_" * 70)
print("\n\033[1mAnswer Q2:\033[0m")
print(f"\nAnswer a:{x2a}, is a 1D array and contains 3 elements.")
print(f"\nAnswer b:{x2b}, is a 2D array with 1 row and 3 columns.")

'''
Question 3:
A 3 by 4 by 4 array is created with arr = np.linspace(1, 48,
48).reshape(3, 4, 4). Index or slice this array to obtain the following:
'''
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("_" * 70)
print("\n\033[1mQuestion 3 array:\033[0m")
print(arr)


# Q3.1 --> 20.0
# flatten() converts the 3D array into a 1D array. Then we use [19] to take
# the 20th element in the flattened array.
A1 = arr.flatten()[19]
print(f"\n\033[1mAnswer Q3.1:\033[0m {A1}")

# Q3.2 --> [ 9. 10. 11. 12.]
# We can simply use slicing to take the first block (0), third row(2)
# and all columns (:).
A2 = arr[0, 2, :]
print(f"\n\033[1mAnswer Q3.2:\033[0m {A2}")


# Q3.3 --> [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
# This is simply the third block reshaped into a 4 by 4 matrix.
A3 = arr[2].reshape(4, 4)
print(f"\n\033[1mAnswer Q3.3:\033[0m\n{A3}")

# Q3.4 --> [[5. 6.], [21. 22.] [37. 38.]]
# We take columns 1 and 2 of the second row of each block and combine them
# using np.stack()
A4 = np.stack([arr[0, 1, 1:3], arr[1, 1, 1:3], arr[2, 1, 1:3]])
print(f"\n\033[1mAnswer Q3.4:\033[0m\n{A4}")

# Q3.5 --> [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
# We use flip() to reverse the specified elements
# along the chosen axis ( axis = 1 for columns and axis = 0 for rows)
A5 = np.flip(arr[2, :, 2:4], axis=1)
print(f"\n\033[1mAnswer Q3.5:\033[0m\n{A5}")

# Q3.6 --> [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
# We take the first column for all rows on each block, stack them together
# and then we flip them to reverse the order.
A6 = np.flip(np.stack([arr[0, :, 0], arr[1, :, 0], arr[2, :, 0]]), axis=1)
print(f"\n\033[1mAnswer Q3.6:\033[0m\n{A6}")

# Q3.7 --> [[1. 4.] [45. 48.]]
# We can use take() to extract elements based on their flattened index
# https://numpy.org/doc/2.2/reference/generated/numpy.take.html
A7 = np.take(arr, [0, 3, 44, 47]).reshape(2, 2)
print(f"\n\033[1mAnswer Q3.7:\033[0m\n{A7}")

# Q3.8 --> [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
# We can use vstack() to combine rows from different blocks into a single array
A8 = np.vstack([arr[1, 2:, :], arr[2, :2, :]])
print(f"\n\033[1mAnswer Q3.8:\033[0m\n{A8}")
