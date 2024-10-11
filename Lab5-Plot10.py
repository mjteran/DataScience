# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 10: Line Plot with Annotations
x = range(0, 20)
y = [value ** 2 for value in x]

# to find max point
xmax = x[np.argmax(y)]     # maximum index x
ymax = np.max(y)           # maximum index y

# Create a line plot.
# -Annotate the highest and lowest points on the plot.
# -Add labels for the x-axis and y-axis, and a title.
plt.figure("Exercise 10: Line Plot with Annotations")
plt.plot(x, y,color='purple',marker='o')
plt.annotate("Highest Point", xy=(xmax, ymax), xytext=(xmax, ymax+2))   # annotate the highest point
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.title("Line Plot with Annotations")
plt.tight_layout()                  # adjust graph to screen
plt.show()