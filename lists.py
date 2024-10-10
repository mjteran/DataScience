# list: a sequence of elements of any data type
from operator import index
from queue import PriorityQueue


countries = ["Brazil", "Canada", "Colombia", "Ecuador", "Japan", "Iran", "Mexico",
             "Nepal", "South Korea", "Taiwan", "USA", "France"]

# indexing a list (index starts from 0)
print(countries[0])         # first element of the list
print(countries[-1])        # last element of the list
print(len(countries[0]))    # number of elements in the list

# slicing a list
# list[start:end]
print(countries[:3])
print(countries[3:])

# assign a new element
countries[11] = "ABC"
print(countries)

# swap elements
first = countries[0]        # assign first, before assigning it later
countries[0] = countries[1]
countries[1] = first
print(countries)

# list methods (functions)
languages = ["C", "C++", "Phyton", "Java", "Javascript"]
# append() - adding a new element at the end of the list
languages.append("SQL")
print(languages)

# insert(): add a new element at the given index
languages.insert(0,"Swift")
print(languages)

# remove elements: pop(index) or remove(element)
languages.pop(0)
print(languages)
languages.remove("Javascript")
print(languages)

# find an element
# index(element)
print(languages.index("Phyton"))

# +: concatenate (combine)
# *: repeat
num1 = [1, 2, 3]
num2 = [4, 5, 6]
print(num1 + num2)
print(num1 * 3)

# "nested" lists
students = [[1, "John", "Canada"], [2, "Max", "USA"], [3, "Peter", "UK"]]
print(students[2][1])   # way 1
inner = students[2]
print(inner[1])         # way 2 (with an extra variable)

# list comprehension -> "google"
