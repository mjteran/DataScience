# tuple: a comma separated values

# how to create a tuple:
student1 = (1, "John", "Canada", "Canada")
student2 = (2, "Marta", "USA", "Colombia")
employee1 = (125, "Rose", "Balboa", "123-569-1478", "abc@gmail.com", 175)
employee2 = (586, "Fran", "Smith", "147-000-1478", "jfl@gmail.com", 180)
# student1[1] = "Justin"      # not allowed to re-assign a value

# store tuples in a list
employees = [employee1, employee2]
empl = employees[0]
print(empl[1]+ " " + empl[2])

# extract values from the tuple separate variable
_, name, country, _ = student1
print(name, country)

# access elements using [index]
print(student1[1])

# tuple methods (functions)
print(student1.index("Canada"))
print(student1.count("Canada"))

# for single element tuple
a = ("Hello",)      # add comma in the end
print(type(a))