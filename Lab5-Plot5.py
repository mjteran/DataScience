# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 5: Scatter Plot
x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1

# Plot a scatter plot using the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
plt.figure("Exercise 5: Scatter Plot")
plt.scatter(x,y,color="blueviolet",marker="*",alpha=0.7)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()