# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 9: Box Plot
dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80
data = [dataset1, dataset2, dataset3]

# Plot a box plot for each dataset.
# -Add labels and a title.

fig, axis = plt.subplots(num="Exercise 9: Box Plot")
axis.boxplot(data)
plt.xlabel("Datasets")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()