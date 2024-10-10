# string: a sequence of characters
# strings are immutable (not possible to change)
# "sequence" - order
from operator import length_hint

# index starts from 0: 0123456789012...
name = "Justin Bieber"

# 1. indexing a string
print(name[6])
print(name[0])
print(name[-1]) # go backwards. Last letter
print(name[-2]) # go backwards. Second last letter

# len(): returns the length of a string
print(len(name))
print(name[len(name)-3]) # third last letter

# 2. slice a string
# str[start:end]    start <= < end (last not included)
print(name[0:3])    # 0 1 2
print(name[7:13])   # 7 8 9 10 11 12
print(name[7:len(name)-2])    # 7 8 9 10
print(name[7:])   # till the last from 7
print(name[:4])    # till beginning to 3

# example
actor = "Ryan Reynolds"
# slice last name
print(actor[5:])

# 3. string methods
# multiply a string by an integer : repeat
print(actor * 3)
# + adding another string : concatenate (combine)
print(actor + " from Vancouver")

# more string methods
# 3.1 uppercase/lowercase/capitalize
address = "816 Granville ST, Vancouver, BC"
print(address.upper())
print(address.lower())
print(address.capitalize())

# 3.2 functions: find(), index()
print(address.find("vancouver"))    #throws an -1 if not found
print(address.index("Vancouver"))    #throws an error if not found

user_id = "19243a"
if user_id.isdigit():
    print("Valid User ID")
elif user_id.isalpha() or user_id.isalnum():
    print("Invalid User ID: use numbers only")

# 4. split, join by comma
# split - splits a string into a list of substrings
l= address.split(",")   # list of elements
print(l)
# strip() to remove blank spaces
street_address = l[0]
city = l[1].strip()
province = l[2].strip()
# create a full message
full_message = f"I live in {street_address}, {city}, {province}"  # use f if wants to use the variables from list
print(full_message)

# join() - joins a list of strings indo one big string. join is opposite of split
cities = ["Vancouver","Burnaby","Richmond","New Westminster","North Vancouver"]
print(" !! ".join(cities))
print(",".join(cities))