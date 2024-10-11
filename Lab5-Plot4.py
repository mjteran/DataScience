# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 4: Histogram
data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution

# Plot a histogram of the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 4: Histogram")
plt.hist(data,bins=20,color="gold",edgecolor="black")
plt.xlabel("Random data")
plt.ylabel("Values")
plt.title("Histogram Plot")
plt.show()