# LIST EXERCISES
# 1 List Creation and Access
from audioop import reverse
from operator import index

list = [1, 2, 3, 4, 5]
print(list[2])  # print element

# 2 List Manipulation

list.append(6)  # append
print(list)     # print list updated
list.pop(1)     # remove second element
print(list)     # print list updated

# 3 List Slicing

list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list2[:4])
print(list2[len(list2)-3:])
print(list2[1])

# 4 List Operations
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sum from elements
# sum from elements way 1
sum1 = 0
for x in list3:
    sum1 += x
print(sum1)
# sum from elements way 2
sum2 = 0
for x in range(len(list3)):
    sum2 = sum2 + list3[x]
print(sum2)

# maximum
maximum = max(list3)
print(maximum)
# minimum
minimum = min(list3)
print(minimum)

# 5 List Comprehension

list4 = []
for x in range(10):
    list4.append(x+1)
print(list4)

# 6 Nested Lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested[1][1])

# STRING EXERCISES
# 1 String Creation and Access

s1 = "Hello, World!"
print(s1[0])
print(s1[-1])

# 2 String Slicing

s2 = "Python Programming"
print(s2[:6])
print(s2[7:])

# 3 String Methods

s3 = "hello, world!"            # lowercase
s3 = s3.upper()
print(s3)

print(s1[:7] + "Phyton!")       # replace way 1

s4 = s1.split(",")
s4[1] = ", Phyton!"
print(s4[0] + s4[1])            # replace way 2

print(s1.replace("World","Phyton")) # replace way 3 (CORRECT)

# 4 String Concatenation

s5 = "Hello"
s6 = "World"
print(s5 + " " + s6)    # concatenated strings

# 5 String Splitting

s7 = "apple,banana,cherry"
l = s7.split(",")
print(l)

# 6 String Formatting

name = "Rubi"
age = 5
m = f"My name is {name} and I am {age} years old"
print(m)

# 7 String Reversal

s8 = input("Enter a string to be reversed: ")
r1 = s8[::-1]   # string[start:stop:step] > step -1 means reverse
print(r1)

# BONUS EXERCISES
# 1 Palindrome Check

def palindrome (z):                     # way 1 long
    y = 0
    for i in range (len(z)):
       if  z[i] == z[len(z)-i-1]:
           y = 1
       else:
           y = -1
    if y == 1:
        print("palindrome")
    elif y == -1:
        print("not palindrome")

def palindrome2 (z):                    # way 2 (CORRECT)
    if z == z[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

pali = input("Enter the text to verify if it is a palindrome: ")
palindrome(pali)
palindrome2(pali)

# 2 List to String Conversion
list5 = ["P", "y", "t", "h", "o", "n"]
s9 = "".join(list5)
print(s9)