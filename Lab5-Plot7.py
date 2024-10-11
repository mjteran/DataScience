# Lab 5 - Maria Jose Teran
import matplotlib.pyplot as plt

# Exercise 7: Pie Chart

categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

# Use the categories and values lists above.
# -Plot a pie chart using the data.
# -Add a title to the chart.
# -Add a legend.
plt.figure("Exercise 7: Pie Chart")
por = '%1.1f%%'                 # display percentage up to 1 decimal place
plt.pie(values, labels=categories,autopct=por)
plt.title("Pie Chart Plot")
plt.axis('equal')
plt.show()