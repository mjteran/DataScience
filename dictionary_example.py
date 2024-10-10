contacts_name = ["John", "Marta", "Juan"]
contacts_number = ["778-253-4343", "236-234-8596", "604-152-9874"]

# dictionary definition: a set of key-value pairs, no order, no duplicate keys
# using dictionary:

contacts = {"John": "778-253-4343", "Marta": "236-234-8596", "Juan": "604-152-9874"}

# how to access the value using the key
print(contacts["John"])

# how to add a new key value pair
contacts["Susy"] = "123-526-7896"
print(contacts)

# how to delete a key-value pair
del contacts["John"]
print(contacts)

# how to update the value in dictionary
if "Juan" in contacts:
    contacts["Juan"] = "667-415-0000"       # update just passing the same key with a different value
print(contacts)

# how to get the sum of the total population
world_pop = {"Canada": 40, "USA": 300, "Brazil":220, "Mexico": 127, "Japan": 125, "Colombia": 51, "South Korea": 51,
             "Ecuador": 18, "Iran": 89}

# loop for iterating key and value as a pair
total = 0
for k, v in world_pop.items():              # call items
    total += v
    print(f"{k}: {v}")
print(total)

# use _ when you don't use the loop variable
total1 = 0
for _, v in world_pop.items():              # call items. _for not using that variable
    total1 += v
print(total1)

# loop for only using values
for v in world_pop.values():
    print(v)

# loop for only using keys
for k in world_pop.keys():
    print(k)

# check the type
print(type(world_pop.keys()))

# convert dictionary to list
print(list(world_pop.keys()))       # convert dictionary into list
print(list(world_pop.values()))     # convert dictionary into list