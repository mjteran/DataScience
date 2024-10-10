# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt
import numpy as np

# Exercise 1: Basic Line Plot
# ex.1. Objective: Create a simple line plot.

# ex.1. Instructions:
# Create two lists x and y with values:
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Plot x vs y:
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 1: Basic Line Plot")
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
#plt.show()


# Exercise 2: Customizing Plots
# ex.2. Objective: Customize the appearance of a plot.

# ex.2. Instructions:
# -Use the same data as in Exercise 1.
# -Matplotlib Exercises - 1 2
# -Change the color and style of the line.
# -Add markers to the data points.
# -Add a grid to the plot.
plt.figure("Exercise 2: Customizing Plots")
plt.plot(x, y,color='limegreen',linestyle="--",marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.title("Simple Line Plot")
#plt.show()


# Exercise 3: Bar Plot
# ex.3. Objective: Create a bar plot.

# ex.3. Instructions:
# Create two lists categories and values .
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Plot a bar chart using the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 3: Bar Plot")
plt.bar(categories,values,color="cyan", edgecolor="black")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
#plt.show()


# Exercise 4: Histogram
# ex.4. Objective: Create a histogram.

# ex.4. Instructions:
# Generate a random dataset using NumPy.
hist = np.random.randn(1000)                # random float data set with Gaussian distribution

# Plot a histogram of the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 4: Histogram")
plt.hist(hist,bins=10,color="gold",edgecolor="black")
plt.xlabel("Random numbers")
plt.ylabel("Values")
plt.title("Histogram Plot")
#plt.show()


# Exercise 5: Scatter Plot
# ex.5. Objective: Create a scatter plot.

# ex.5. Instructions:
# Create two lists x and y with random values.
x5 = np.random.randn(1000)                # random float data set with Gaussian distribution
y5 = np.random.randn(1000)                # random float data set with Gaussian distribution

# Plot a scatter plot using the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
# -Show the plot.
plt.figure("Exercise 5: Scatter Plot")
plt.scatter(x5,y5,color="blueviolet",marker="*",alpha=0.6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
#plt.show()


# Exercise 6: Subplots
# ex.6. Objective: Create multiple plots in a single figure using subplots.
# data 1
x6 = np.arange(-20,21,1)      # int from -20 to 20
y6 = (0.15 * x6 ) ** 3
# data 2
cat = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ,'J']
val = np.random.randint(1,10,10)
# data 3
hist_sub = np.random.randn(500)                # random float data set with Gaussian distribution
# data 4
x_sub = np.random.randn(200)                # random float data set with Gaussian distribution
y_sub = np.random.randn(200)                # random float data set with Gaussian distribution

# ex.6. Instructions:
# Create a figure with 2x2 subplots.
# Plot different types of plots in each subplot (e.g., line plot, bar plot,
# histogram, scatter plot).
# Add titles to each subplot.
# Show the figure.
fig,axes = plt.subplots(2, 2,num="Exercise 6. Subplots")
fig.suptitle("Multiple plots in a single figure")

axes[0,0].plot(x6,y6,color="lime")
axes[0,0].set_title("Line Plot")

axes[0,1].bar(cat,val,color="gray",edgecolor="black")
axes[0,1].set_title("Bar Plot")

axes[1,0].hist(hist_sub,bins=15,color="blue",edgecolor="black")
axes[1,0].set_title("Histogram Plot")

axes[1,1].scatter(x_sub,y_sub,color="orangered",marker="x",alpha=0.6)
axes[1,1].set_title("Scatter Plot")

plt.tight_layout()      # adjust the space in the subplots
plt.show()