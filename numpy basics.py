import numpy as np

# python lists
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# creating numpy arrays
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height), type(np_weight))

# calculate bmi with numpy
np_bmi = np_weight / np_height ** 2
print(np_bmi)

# filter to verify values were height > 1.8
print(np_bmi[np_height>1.8])



