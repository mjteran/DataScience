# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt

# Exercise 1: Basic Line Plot
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# Plot x vs y:
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 1: Basic Line Plot")
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()