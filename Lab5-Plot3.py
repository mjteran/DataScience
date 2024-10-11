# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt

# Exercise 3: Bar Plot
categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

# Plot a bar chart using the data.
# -Add labels for the x-axis and y-axis.
# -Add a title to the plot.
plt.figure("Exercise 3: Bar Plot")
plt.bar(categories,values,color="cyan", edgecolor="black")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()
