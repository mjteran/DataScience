# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt

# Exercise 8: Stacked Bar Plot
categories = ['Group 1', 'Group 2', 'Group 3']
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

# Create a stacked bar plot where each category has the three different values stacked.
# -Add labels for the x-axis and y-axis.
# -Add a legend to indicate the different parts of the stack.
plt.figure("Exercise 8: Stacked Bar Plot")
plt.bar(categories,value1,color="orange", edgecolor="black")
plt.bar(categories,value2, bottom=value1, color="yellow", edgecolor="black")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Bar Plot")
plt.show()