# Starry - Maria Jose

n = int(input("Introduce the number of columns for drawing patterns: "))

# first pattern
print("\n#1:\n")

for i in range(0, n):               # range to print pattern increasingly
    for j in range(n - i - 1):      # n-i to print spaces decreasingly and -1 for pattern's position on the left
        print(" ", end="")
    for j in range(2 * i + 1):      # 2*i+1 for printing odd stars increasingly
        print("*", end="")
    print()

# second pattern
print("\n#2:\n")

for i in range(n, 0, -1):           # stars printed in decrease order
    for j in range(i):
        print("*", end="")
    print()

# third pattern
print("\n#3: (If n is even then it prints n lines, where n is the closest odd number.)\n")

m = n / 2                           # m: total number of lines for mirror patterns loops
m = int(round(m + 0.5))             # convert m into an integer

for i in range(m):                  # print stars increasingly
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(m, 1, -1):           # print stars decreasingly (mirror)
    for j in range(i - 1):
        print("*", end="")
    print()

# fourth pattern
print("\n#4: (If n is even then it prints n lines, where n is the closest odd number.)\n")

for i in range(m, 0, -1):           # range to print pattern decreasingly
    for j in range(m - i):          # print spaces increasingly
        print(" ", end="")
    for j in range(2 * i - 1):      # 2*i-1 for printing odd stars decreasingly
        print("*", end="")
    print()
for i in range(1, m):               # range to print pattern increasingly (mirror)
    for j in range(m - i - 1):      # print spaces decreasingly
        print(" ", end="")
    for j in range(2 * i + 1):      # 2*i+1 for printing odd stars increasingly
        print("*", end="")
    print()

# fifth pattern
print("\n#5: (If n is even then it prints n lines, where n is the closest odd number.)\n")
for i in range(0, m - 1):           # range to print pattern increasingly
    for j in range(m - i - 1):      # print spaces decreasingly
        print(" ", end="")
    for j in range(2 * i + 1):      # 2*i+1 for printing odd stars increasingly
        print("*", end="")
    print()
for i in range(m, 0, -1):           # range to print pattern decreasingly (mirror)
    for j in range(m - i):          # print spaces increasingly
        print(" ", end="")
    for j in range(2 * i - 1):      # 2*i-1 for printing odd stars decreasingly
        print("*", end="")
    print()