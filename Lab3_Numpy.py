# LAB 3 - Maria Jose Teran

import numpy as np

# TASK 1: Creating a 1D NumPy Array
# create an 1D python array
array_1d = []                       # create an empty py array
for i in range(30):                 # loop for 30 element py array
    array_1d.append(i + 1)

# create an 1D numpy array
np1d_array = np.array(array_1d)     # creating numpy arrays
print(f"\nTask 1:\n1D array: {np1d_array}")             # print the numpy array
print(f"1D array shape: {np.shape(np1d_array)}")        # print the shape of the numpy array
print(f"Indexing the 10th element: {np1d_array[10]}")   # access and print the element at index 10.


# TASK 2: Creating a 2D NumPy Array
# reshape the 1D array into a 2D array
np2d_array = np.reshape(np1d_array,(6,5))        # reshape into a 2D array (6, 5)
print(f"\nTask 2:\n2D array:\n{np2d_array}")            # print the 2D array

# access and array element and print
print(f"Indexing the (row = 3, column = 4) element: {np2d_array[3][4]}")    # access and print the element (3,4)


# TASK 3: Subsetting a 2D Array
# extract and print a row from 2D array
np2d_3 = np2d_array[3]
print(f"\nTask 3:\nFrom Task 2's 2D array, third row: {np2d_3}")      # print the 2D array (3rd row)

# extract and print the first two rows and the last three columns
print(f"From Task 2's 2D array, first two rows and last three columns:\n{np2d_array[0:2,2:5]}")   # (0-1 row,2-4 column)


# TASK 4: Generating Random Integer Array
# use the numpy.random module to generate a 1D array of 15 random integers
np1d_rd = np.random.randint(10,100,15)  # 1d array, 15 elements, numbers from 10 to 100
print(f"\nTask 4:\n1D array, 15 random numbers from 10 to 100:\n{np1d_rd}")     # print the array

# find its maximum and minimum values
np1d_rd_max = np.max(np1d_rd)                           # array maximum value
print(f"1D array, maximum value: {np1d_rd_max}")        # print the array maximum value
np1d_rd_min = np.min(np1d_rd)                           # array minimum value
print(f"1D array, minimum value: {np1d_rd_min}")        # print the array minimum value


# TASK 5: Generating a 2D Random Array
# generate a 2D array of shape (4, 4) with random integers between 0 and 50
np2d_rd = np.random.randint(0,50,(4,4))  # 2d array (4,4), numbers from 0 to 50
print(f"\nTask 5:\n2D array (4,4), random numbers from 0 to 50:\n{np2d_rd}")    # print the 2D array

# find the sum of all the elements in the array
np2d_rd_sum = np.sum(np2d_rd)
print(f"2D random array (4,4) total sum: {np2d_rd_sum}")    # sum of all the elements in the 2D array


# TASK 6: Manipulating Arrays
# create a 2D array of random integers (5, 5) between 1 and 20
np2d_rd2 = np.random.randint(1,20,(5,5))  # 2d array (5,5), numbers from 1 to 20
print(f"\nTask 6:\n2D array (5,5), random numbers from 1 to 20:\n{np2d_rd2}")   # print the 2D array

# set all values in the second row to 0
np2d_rd2[1] = 0
print(f"Set all values in the 2nd row [1] to 0:\n{np2d_rd2}")     # print the 2D array

# replace all values greater than 10 with the value 99
np2d_rd2[np2d_rd2 > 10] = 99
print(f"Replace all values > 10 with 99:\n{np2d_rd2}")           # print the 2D array


# TASK 7: Arithmetic Operations on Arrays
# create two 1D arrays of length 5 with random integers between 1 and 10.
np1d_rd1 = np.random.randint(1,10,5)        # 1d array, 5 elements, numbers from 1 to 10
np1d_rd2 = np.random.randint(1,10,5)        # 1d array, 5 elements, numbers from 1 to 10
print(f"\nTask 7:\n1st 1D array, 5 random numbers from 1 to 10: {np1d_rd1}")     # print the 1st array
print(f"2nd 1D array, 5 random numbers from 1 to 10: {np1d_rd2}")     # print the 1st array

# perform element-wise addition, subtraction, and multiplication on the two arrays
np1d_sum = np1d_rd1 + np1d_rd2                              # addition from arrays
np1d_sub = np1d_rd1 - np1d_rd2                              # subtraction from arrays
np1d_mp = np1d_rd1 * np1d_rd2                               # multiplication from arrays
print(f"Addition of arrays [1]+[2]: {np1d_sum}")            # print the addition
print(f"Subtraction of arrays [1]-[2]: {np1d_sub}")         # print the multiplication
print(f"Multiplication of arrays [1]*[2]: {np1d_mp}")       # print the multiplication


# TASK 8: Broadcasting in NumPy
# create a 1D array of length 4 with values [2, 4, 6, 8]
np1d = np.array([2, 4, 6, 8])
print(f"\nTask 8:\n1D array of length 4 with values (2, 4, 6, 8): {np1d}")     # print the 1D array

# create a 2D array of shape (3, 4) with random integers between 1 and 5
np2d = np.random.randint(1,5,(3,4))         # 2d array, (3,4), numbers 1 - 5
print(f"2D array (3,4), random numbers from 1 to 5:\n{np2d}")   # print the 2D array

# add the 1D array to each row of the 2D array using broadcasting
np_b = np2d+np1d                                            # add the array 1D to 2D
print(f"Broadcast array 2D + 1D array:\n{np_b}")            # print the broadcast array


# TASK 9: Filtering an Array
# generate a 1D array of 20 random integers between 1 and 100
np1d_rd3 = np.random.randint(1,100,20)        # 1d array, 20 elements, numbers from 1 to 100
print(f"\nTask 9:\n1D array, 20 random numbers from 1 to 100:\n{np1d_rd3}")     # print the array

# print all elements of the array that are greater than 50
print(f"1D array, with only elements > 50: {np1d_rd3[np1d_rd3>50]}")            # print the elements > 50

# replace all values less than 30 with -1 and print the modified array
np1d_rd3[np1d_rd3 < 30] = -1                                                    # modified array, elements < 30 = -1
print(f"1D array, when setting elements < 30 as -1 : {np1d_rd3}")                       # print the array


# TASK 10: Reshaping Arrays
# create a 1D array of 12 random integers between 1 and 50
np1d_rd4 = np.random.randint(1,50,12)           # 1d array, 12 elements, numbers from 1 to 50
print(f"\nTask 10:\n1D array, 12 random numbers from 1 to 50:\n{np1d_rd4}")     # print the array

# reshape the array into a 3x4 2D array
np2d_re = np.reshape(np1d_rd4, (3,4))                   # reshape the 1D array into 2D (3,4)
print(f"2D array 3x4, reshaped from 1D array:\n{np2d_re}")     # print the array

# transpose the array (swap rows and columns) and print the result
np2d_re2 = np.transpose(np2d_re)                                # transpose the array into (4,3)
print(f"2D transposed array 4x3:\n{np2d_re2}")                  # print the array
