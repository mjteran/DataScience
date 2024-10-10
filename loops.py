# loops
# - for loop
# for "loop_var" in "collection"

# collection (iterable): range(start, end, steps), string, list
# loop_var: to assign each value in a collection

# always last index not included

for i in range(5):      # (0, 1, 2, 3, 4)
    print(f"{i}: Hello")

for i in range(2, 7):   # (2, 3, 4, 5, 6)
    print(f"{i}: Hi")

for i in range(1, 10, 2):   # str[1:5:2] = (1, 3, 5, 7, 9)
    print(f"{i}: 2 steps each")

for i in range(10, 1, -1):  # (10, 8, 6, 4, 2)
    print(f"{i}: negative step")

# iterating a string
city = "Vancouver"

for ch in city:
    print(ch)

# count the number of vowels?
vowel_count = 0
for ch in city:
    # logic (if ch is vowel: count)
    if ch in "AEIOUaeiou":      # same as if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"
        vowel_count += 1        # same as adding 1 to vowel_count
print(f"{city} has {vowel_count} vowels.")

# iterating a list
nums = [1, 40, 20, 14, 35, 31, 7, 11]

# e.g.1 count the number of even numbers in the list
even_count = 0
for num in nums:                # num iterate each element of the list
    # logic is verify if num is even
    if num % 2 == 0:            # % checks the reminder after divide by
        even_count +=1
print(f"{nums} list has {even_count} even numbers.")

# while loop
x = 0
while x <5:
    print("Hello")
    x += 1

# count the number of vowels
city = "Vancouver"
# I need to be able to access each character
# index!
i = 0
vowels = 0
while i < len(city):
    if city[i] in "AEIOUaeiou":     # check if a character is vowel
        vowels += 1
    i += 1
print(f"{city} has {vowels} vowels.")

# count the number of even numbers with a list
list1 = [1, 40, 20, 14, 35, 31, 7, 11]
j = 0
even = 0
while j < len(list1):
    if list1[j] % 2 == 0:
        even += 1
    j += 1
print(even)
print(f"{list1} has {even} even numbers.")

# infinite loop with break and continue
while True:                         # infinite loop
    command = input("Enter 'q' to quit: ")
    if command == "q":
        print("Bye!")
        break                       # stop the loop
    elif command == "s":
        continue                    # skip the rest
    print("Try again!")