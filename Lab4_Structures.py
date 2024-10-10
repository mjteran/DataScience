# Lab 4 - Maria Jose Teran

import numpy as np

# Exercise 1: Student Grades Analysis
print("\nEX 1: STUDENT GRADES ANALYSIS")
students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}

# ex1.1. Calculate and print the average score for each student.
print("- Task 1: The average score for each student is:")
av = 0
max_av = 0
max_st = ""
min_av = 0
min_st = ""
for k, v in students.items():                   # call items
    av = np.round(np.average(v),2)      # average for each student
    print(f"{k}: {av}")                         # print the average for each student
    if av > max_av:
        max_av = av
        max_st = k
    if av < min_av or min_av == 0:
        min_av = av
        min_st = k

# ex1.2. Find and print the name of the student with the highest average score.
print(f"\n- Task 2: The student with the highest average score is {max_st} with the score {max_av}.")

# ex1.3. Find and print the name of the student with the lowest average score.
print(f"\n- Task 3: The student with the lowest average score is {min_st} with the score {min_av}.")

# ex1.4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary
students["Frank"] = [80, 90, 85]
print("\n- Task 4: The updated dictionary after adding 'Frank' is:")
for k, v in students.items():                   # call items
    av = np.round(np.average(v),2)      # average for each student
    print(f"{k}: {av}")


# Exercise 2: Product Inventory Management
print("\nEX 2: PRODUCT INVENTORY MANAGEMENT")
inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}

# ex2.1. Print the current inventory in a user-friendly format.
print("- Task 1: Inventory from the store:")
for key, value in inventory.items():  # call items
    print('| Product: {:<6} | Quantity: {:<3} | Price: ${:<3} |'.format(key.capitalize(), value[0], value[1]))

# ex2.2. Calculate and print the total value of the inventory.
def print_inventory(repository):
    total = 0
    for k, v in repository.items():               # call items
        subtotal = v[0] * v[1]
        total += subtotal
        repository[k] = (v[0], v[1], subtotal)      # add total value as a third element
        print('| Product: {:<6} | Quantity: {:<3} | Price: ${:<3} | Subtotal: ${:<4} |'.format(k.capitalize(), v[0], v[1], subtotal))
    print(f"In the store, the total sum is ${total}.")
print("\n- Task 2: Print the total value of the inventory:")
print_inventory(inventory)

# ex2.3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
print("\n- Task 3: Add one product 'Mango' with 30 items priced at $0.6 each to the inventory:")
inventory["mango"] = [30, 0.6]
print_inventory(inventory)

# ex2.4. Update the quantity of "banana" to 120 and print the updated inventory.
print("\n- Task 4: Update the quantity of 'banana' to 120. The updated inventory:")
inventory["banana"] = (120, 0.2)
print_inventory(inventory)

# ex2.5. Remove "pear" from the inventory and print the updated inventory.
print("\n- Task 5: Remove 'pear' from the inventory:")
del inventory["pear"]
print_inventory(inventory)


# Exercise 3: EMPLOYEE RECORDS
print("\nEX 3: EMPLOYEE RECORDS")
employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]

# ex3.1. Print the names and departments of all employees.
np_employees = np.array(employees)                      # convert into a numpy array
np_employees_no_email = np.delete(np_employees, 2,1)    # remove email from array
print("- Task 1. Names and departments of all employees:")
for employee in np_employees_no_email:                  # print user friendly
    print(f"    Name: {employee[0]:<15} | Department: {employee[1]}")

# ex3.2. Print the email addresses of all employees in alphabetical order by their last names.
def sort_by_lastname(np_array):                         # function to sort by last name
    last_names = []
    for name_complete in np_array[:, 0]:                # range for names
        last = name_complete.split()[1]                 # extract the last name from name
        last_names.append(last)                         # append last names into array
    sorted_index = np.argsort(last_names)               # sort the index of lastnames
    array_sorted = np_array[sorted_index]               # array ordered by index sorted
    return array_sorted

employee_sorted = sort_by_lastname(np_employees)        # call function to sort by last name
employee_only_email = np.delete(employee_sorted, (0,1),1)   # delete rows except email
print(f"\n- Task 2. Email addresses of all employees in alphabetical order (by last names):\n{employee_only_email}")

# ex3.3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
new = np.array(["David Wilson", "Sales", "david.wilson@example.com"])   # add new employee
np_employees = np.vstack([np_employees,new])                            # add new row to employee array
employee_sorted = sort_by_lastname(np_employees)                        # call function to sort by last name
print("\n- Task 3. Add a new employee 'David Wilson' and print the updated list:")
for v in employee_sorted:  # call items
    print("    Name: {:<13} | Department: {:<10} | e-mail: {:<25}".format(*v))  # print employees

# ex3.4. Find and print the department of "Jane Smith".
employee = "Jane Smith"
print("\n- Task 4. Find and print the department of 'Jane Smith':")
dep_row = 0
for name in employee_sorted[:, 0]:                      # range for names
    if name == employee:
        print(employee_sorted[dep_row, 1])
    dep_row += 1


# Exercise 4: BOOK LIBRARY SYSTEM
print("\nEX 4: BOOK LIBRARY SYSTEM")
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

def print_books_library(repository,book):
    for isbn,info in repository.items():                  # loop for printing items
        if book == "" or book == "all" or isbn == book:  # Check for all or specific book
            print(f"ISBN: {isbn}")
            print(f"Title: {info['title']}")
            print(f"Author: {info['author']}")
            print(f"Year: {info['year']}\n")
            if isbn == book:  # Break after printing specific book
                break

# ex4.1. Print the details of all books in a user-friendly format.
print("- Task 1: Print the details of all books:")
print_books_library(library,"all")                           # call function to print all the books in library

# ex4.2. Find and print the details of the book with the ISBN "978-0-14-028329-7".
isbn_2 = "978-0-14-028329-7"
print(f"- Task 2: The book with the ISBN '{isbn_2}' has the following information:")
print_books_library(library,isbn_2)                             # call function to print one book in library

# ex4.3. Add a new book: ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", year 1925.
library["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
print(f"- Task 3: Add a new book ISBN '978-1-4028-9462-6' and print the updated library information:")
print_books_library(library,"all")                           # call function to print all the books in library

# ex4.4. Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.
library["978-0-7432-7356-5"]["year"] = 1961
print(f"- Task 4: Update the year of 'To Kill a Mockingbird' to 1961 and print the updated details:")
print_books_library(library,"978-0-7432-7356-5")           # call function to print one book in library

# ex4.5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
del library["978-0-452-28423-4"]
print(f"- Task 5: Remove the book with ISBN '978-0-452-28423-4' and print the updated library:")
print_books_library(library,"all")                           # call function to print all the books in library


# Exercise 5: CITY POPULATION DATA
print("EX 5: CITY POPULATION DATA")
cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}
def print_cities(repository,city):
    for c,p in repository.items():                  # loop for printing items
        if city == "" or city == "all" or c == city:  # Check for all or specific book
            print(f"The population of {c} is {p:,}.")
            if c == city:  # Break after printing specific book
                break

# ex5.1. Print the population of each city in a user-friendly format.
print(f"- Task 1: Print the population of each city:")
print_cities(cities,"all")

# ex5.2. Find and print the city with the highest population.
low_pop = 0
low_city = 0
big_pop = 0
big_city = 0
for city, pop in cities.items():  # loop for printing items
    if pop > big_pop:
        big_pop = pop
        big_city = city
    if pop < low_pop or low_pop == 0:
        low_pop = pop
        low_city = city
print(f"\n- Task 2: The city with bigger population is {big_city} with {big_pop:,}.")

# ex5.3. Find and print the city with the lowest population.
print(f"\n- Task 3: The city  with lowest population is {low_city} with {low_pop:,}.")

# ex5.4. Update the population of "Phoenix" to 1700000 and print the updated data.
cities["Phoenix"] = 1700000
print(f"\n- Task 4: Update the population of 'Phoenix' to 1700000 and print the updated data:")
print_cities(cities,"Phoenix")

# ex5.5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
print(f"\n- Task 5: Add a new city 'San Francisco' and print the updated data:")
cities["San Francisco"] = 884000
print_cities(cities,"all")


# Exercise 6: MOVIE DATABASE
print("\nEX 6: MOVIE DATABASE")

movies = {
"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}
def print_movies(repository,movie):
    for name_movie,info in repository.items():                  # loop for printing items
        if movie == "" or movie == "all" or name_movie == movie:  # Check for all or specific book
            print(f"Movie: {name_movie}")
            print(f"Year: {info['year']}")
            print(f"Rating: {info['rating']}")
            print(f"Genre: {info['genre']}\n")
            if name_movie == movie:  # Break after printing specific book
                break

# ex6.1. Print the details of all movies in a user-friendly format.
print(f"- Task 1: Print the details of all movies:")
print_movies(movies,"all")

# ex6.2. Find and print the highest-rated movie.
rate = 0
hig_rate = ""
for name_m,info in movies.items():    # loop for printing items
    if info['rating'] > rate:
        rate = info['rating']
        hig_rate = name_m
print(f"- Task 2: The highest-rated movie is '{hig_rate}' with {rate}.")

# ex6.3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}
print(f"\n- Task 3: Add a movie to database and update the data:")
print_movies(movies,"all")

# ex6.4. Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"]["rating"] = 9.0
print(f"- Task 4: Update the rating of 'Inception' to 9.0 and update the data:")
print_movies(movies,"Inception")

# ex6.5. Remove "Pulp Fiction" from the database and print the updated list.
del movies["Pulp Fiction"]
print(f"- Task 5: Remove 'Pulp Fiction' from the database and update the data:")
print_movies(movies,"all")


# Exercise 7: COUNTRY CAPITALS
print("EX 7: COUNTRY CAPITALS")

countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}
def print_capitals(repository,c):
    for country,capital in repository.items():                  # loop for printing items
        if c == "" or c == "all" or c == country:  # Check for all or specific book
            print(f"The capital of '{country}' is '{capital}'.")
            if c == capital:  # Break after printing specific book
                break

# ex7.1. Print the names of all countries and their capitals.
print(f"- Task 1: Print the names of all countries and their capitals:")
print_capitals(countries,"all")

# ex7.2. Find and print the capital of Germany.
print(f"\n- Task 2: Find and print the capital of Germany:")
print_capitals(countries,"Germany")

# ex7.3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"
print(f"\n- Task 3: Add a new country 'Australia' and print the updated dictionary:")
print_capitals(countries,"all")

# ex7.4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"
print(f"\n- Task 4: Update the capital of 'USA' and print the updated dictionary:")
print_capitals(countries,"all")

# ex7.5. Remove "France" from the dictionary and print the updated dictionary.
del countries["France"]
print(f"\n- Task 5: Remove 'France' from the dictionary and print the updated dictionary:")
print_capitals(countries,"all")


# Exercise 8: SHOPPING CART
print("\nEX 8: SHOPPING CART")

cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]
# convert the list of dictionaries into list:
cart_list = []
for product in cart:
    cart_list.append([product['item'], product['quantity'], product['price_per_unit']])
# convert the list into numpy array, for making easy the number calculates:
cart_array = np.array(cart_list)               # convert the list into numpy array
# change type of daya in quantity and price
for i in range(cart_array.shape[0]):                        # in range of each row
    cart_array[i, 1] = int(cart_array[i, 1])                # update each quantity
    cart_array[i, 2] = float(cart_array[i, 2])              # update each price

# ex8.1. Print the details of all items in the cart.
print("- Task 1. Print the details of all items in the cart:")
for item in cart_array:  # call items
    print('| Item: {:<7} | Quantity: {:<2} | Price Per Unit: ${:<4} |'.format(item[0],item[1],item[2]))  # print employees

# ex8.2. Calculate and print the total cost of the cart.
quantities = cart_array[:,1].astype(int)                   # extract quantities into int
prices = cart_array[:,2].astype(float)                     # extract prices into float
total_values = np.round(quantities * prices,2)     # calculate total
cart_array = np.column_stack((cart_array,total_values))     # append the total to another column
def print_cart(array):                                # function to print the cart
    total_cart = 0
    for it in array:  # call items
        total_cart += it[3].astype(float)                   # calculate total of cart
        print('| Item: {:<7} | Quantity: {:<2} | Price/Unit: ${:<4} | Total Price: ${:<4} |'.format(*it))  # print items
    print(f"The total cost of the cart: is {total_cart}")

print("\n- Task 2. Calculate and print the total cost of the cart:")
print_cart(cart_array)                          # call function to print all the elements

# ex8.3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
new_item = np.array(["grape", 5, 0.6, 3.0])                 # create a numpy array, same column shape
cart_array = np.vstack((cart_array, new_item))              # add the new row to the cart array
print("\n- Task 3. Add a new item 'grape' with quantity 5 and print the updated cart:")
print_cart(cart_array)

# ex8.4. Update the quantity of "banana" to 10 and print the updated cart.
for it in cart_array:  # call items
    if it[0] == "banana":
        it[1] = 10
        it[3] = 2.0
print("\n- Task 4. Update the quantity of 'banana' to 10 and print the updated cart:")
print_cart(cart_array)

# ex8.5. Remove "pear" from the cart and print the updated cart.
item_to_remove = "pear"
row_to_remove = 0
for i in range(cart_array.shape[0]):
    if cart_array[i, 0] == item_to_remove:
        row_to_remove = i
        break
cart_array = np.delete(cart_array, row_to_remove, axis=0)
print("\n- Task 5. Remove 'pear' from the cart and print the updated cart:")
print_cart(cart_array)


# Exercise 9: Weather Data
print("\nEX 9: WEATHER DATA")

weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}
def print_weather(repository,day):
    for weekday,info in repository.items():                  # loop for printing items
        if day == "" or day == "all" or weekday == day:  # Check for all or specific book
            print(f"Day: {weekday}")
            print(f"Temperature: {info['temperature']}")
            print(f"Humidity: {info['humidity']}\n")
            if weekday == day:  # Break after printing specific book
                break

# ex 9.1. Print the weather details for each day.
print(f"- Task 1: Print the weather details for each day:")
print_weather(weather,"all")

# ex 9.2. Find and print the day with the highest temperature.
low_hum = 0
low_day = ""
big_temp = 0
big_day = ""
for weekday, info in weather.items():  # loop for printing items
    if info['temperature'] > big_temp:
        big_temp = info['temperature']
        big_day = weekday
    if info['humidity'] < low_hum or low_hum == 0:
        low_hum = info['humidity']
        low_day = weekday
print(f"- Task 2: The day with highest temperature is {big_day} with {big_temp}.")

# ex 9.3. Find and print the day with the lowest humidity.
print(f"\n- Task 3: The day  with lowest humidity is {low_day} with {low_hum}.")

# ex 9.4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
weather["Wednesday"]["temperature"] = 25
print(f"\n- Task 4: Update the temperature of 'Wednesday' to 25 and print the updated data:")
print_weather(weather,"Wednesday")

# ex 9.5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated
# weather data.
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(f"- Task 5: Add weather data for 'Saturday' and print the updated data:")
print_weather(weather,"all")


# Exercise 10: LIBRARY MEMBERS
print("EX 10: LIBRARY MEMBERS")

members = [
{"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
{"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
{"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
{"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]
# convert list into dictionary
members_dict = {}
for member in members:
    members_dict[member['name']] = {'age': member['age'], 'books_borrowed': member['books_borrowed']}
def print_members(repository,names):
    for mem,inf in repository.items():                  # loop for printing items
        if names == "" or names == "all" or mem == names:  # Check for all or specific book
            print(f"Member's name: {mem}")
            print(f"    Age: {inf['age']}")
            print(f"    Books Borrowed: {", ".join(inf['books_borrowed'])}\n")
            if mem == names:  # Break after printing specific book
                break

# ex.10.1. Print the names and ages of all members.
print(f"- Task 1: Print the names and ages of all members:")
print_members(members_dict,"all")

# ex.10.2. Find and print the books borrowed by "Charlie".
print(f"- Task 2: Find and print the books borrowed by 'Charlie':")
for mem, inf in members_dict.items():           # loop for finding member
    if mem == "Charlie":                        # Check for Charlie specific books
        print(f"For, member's name: '{mem}', the books borrowed are: {", ".join(inf['books_borrowed'])}\n")

# ex.10.3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
members_dict["Eve"] = {"age": 28, "books_borrowed": ["Pride and Prejudice"]}
print(f"- Task 3: Add a new member 'Eve' and print the updated list:")
print_members(members_dict,"all")

# ex.10.4. Update the age of "Bob" to 31 and print the updated list.
members_dict['Bob']['age'] = 31
print(f"- Task 4: Update the age of 'Bob' to 31 and print the updated data:")
print_members(members_dict,"Bob")

# ex.10.5. Remove "David" from the list and print the updated list.
del members_dict["David"]
print(f"- Task 5: Remove 'David' from the list and print the updated list:")
print_members(members_dict,"all")