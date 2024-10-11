# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt

# Exercise 2: Customizing Plots
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# -Change the color and style of the line (e.g., use a dashed line and green
# color).
# -Add markers to the data points.
# -Add a grid to the plot.
plt.figure("Exercise 2: Customizing Plots")
plt.plot(x, y,color='violet',linestyle="--",marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.title("Simple Line Plot")
plt.show()