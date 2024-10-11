# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 6: Subplots

# Line Plot dataset:
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# Bar Plot dataset:
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
# Histogram dataset:
data = np.random.randn(1000)
# Scatter Plot dataset:
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Create a figure with 2x2 subplots.
# Plot different types of plots in each subplot
# Add titles to each subplot.
fig,axes = plt.subplots(2, 2,num="Exercise 6. Subplots")
fig.suptitle("Multiple plots in a single figure")

axes[0,0].plot(x,y,color="lime")
axes[0,0].set_title("Line Plot")

axes[0,1].bar(categories,values,color="gray",edgecolor="black")
axes[0,1].set_title("Bar Plot")

axes[1,0].hist(data,bins=15,color="blue",edgecolor="black")
axes[1,0].set_title("Histogram Plot")

axes[1,1].scatter(x_scatter,y_scatter,color="orangered",marker="x",alpha=0.6)
axes[1,1].set_title("Scatter Plot")

plt.tight_layout()      # adjust the space in the subplots
plt.show()