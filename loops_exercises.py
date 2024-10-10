#   STRING EXERCISES

# 1 print each character
str1 = "Python"

for ch in str1:
    print(ch)

# 2 count the number of vowels
str2 = "data science"
count1 = 0

for ch in str2:
    if ch in "AEIOUaeiuo":
        count1 += 1

print(f"The string '{str2}' has {count1} vowels.")

# 3 reverse the string
str3 = "hello world"
str_rev = ""

for ch in str3:
    str_rev = ch + str_rev      # append in reverse
print(str_rev)

# 3 another
reversed_str3 = ""
for i in range(len(str3) - 1, -1, -1):
    reversed_str3 += str3[i]

# 4 ASCII value of each character
str4 = "coding"

for ch in str4:
    print(f"ASCII code from {ch} is {ord(ch)}.")

# 5 count repetition from character "e"
str5 = "experience"
count2 = 0

for ch in str5:
    if ch in "eE":
        count2 += 1

print(f"The string '{str5}' has {count2} 'e' characters.")

# 6 replace each vowel in the string
str6 = "education"
str_rep = ""
new_ch = "*"

for ch in str6:
    if ch in "aeiouAEIOU":
        ch = new_ch
    str_rep += ch

print(f"When replacing vowels to * from '{str6}' = '{str_rep}'")

# 7 print every second character
str7 = "looping"
srt_2c = ""

for i in range(1,len(str7),2):
    srt_2c += str7[i]

print(f"If printing only the 2nd character from '{str7}' = '{srt_2c}'")

# 8 find the first repeating character
str8 = "swiss"

for i in range(len(str8)):
    if str8[i] == str8[i+1]:
        print(f"The first repeating character from '{str8}' appears on position '{i+1}' (starting from 1)")
        break

# 9 capitalize each word
str9 = "machine learning is fun"
str_cap = ""

for i in range(len(str9)):
    str_cap += str9[i].upper()

print(f"The string capitalized by character is '{str_cap}'")

# 10 check if is same forwards and backwards
str10 = "racecar"
str10_rev = ""

for ch in str10:
    str10_rev = ch + str10_rev      # append in reverse
if str10_rev == str10:
    print(f"The string {str10} is Palindrome")
else:
    print(f"The string {str10} is not Palindrome")

#   LIST EXERCISES

# 1 print each element
l1 = [10, 20, 30, 40, 50]

for element in l1:
    print(element)

# 2 sum of all elements
l2 = [1, 2, 3, 4, 5]
s = 0

for el in l2:
    s += el

print(f"The sum from the list elements is {sum}")

# 3 find the largest number
l3 = [3, 7, 2, 9, 9]

largest = l3[0]
j = 0
while j < len(l3):
    if l3[j] > largest:
        largest = l3[j]
    j += 1

print(f"The largest element from the list is {largest}")

# 4 count times that appears the number 4
l4 = [1, 4, 4, 2, 4, 3]

count3 = 0
j = 0
while j <= len(l3):
    if l4[j] == 4:
        count3 += 1
    j += 1

print(f"The number 4 appears {count3} times in the list")

# 5 create a new list that contains the squares of each number
l5 = [1, 2, 3, 4, 5]
l5_sqr = []

for ele in l5:
    l5_sqr.append(ele ** 2)

print(f"Initial list: {l5}, Squared list: {l5_sqr}")

# 6 concatenate all the words
l6 = ["Python", "is", "awesome"]
l6_str = ""

for ele in l6:
    l6_str += ele + " "

print(f"Concatenated string: {l6_str}")

# 7 create a list that contains only the even numbers
l7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l7_even = []

for ele in l7:
    if ele % 2 == 0:
        l7_even.append(ele)

print(f"Initial list: {l7}, Even numbers list: {l7_even}")

# 8 multiply each number by 2
l8 = [2, 4, 6, 8]
l8_2 = []

for ele in l8:
    l8_2.append(ele * 2)

print(f"Initial list: {l8}, List * 2: {l8_2}")

# 9 remove the occurrences of the number 3
l9 = [1, 3, 3, 4, 3, 5, 3]
l9_new = []

for ele in l9:
    if ele != 3:                # could use the == 3, using .pop
        l9_new.append(ele)

print(f"Initial list: {l9}, List without 3: {l9_new}")

# 10 find the index of the 1st occurrence of 7
l10 = [5, 7, 8, 7, 10]

for i in range(len(l10)):
    if l10[i] == 7:
        print(f"For the list: {l10}, the index of the 1st 7 is: {i+1} (1st list element starts as 1)")
        break
