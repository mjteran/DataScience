# part 1 - Maria Jose

# How can I use mod (%) and integer division (/) to figure out the nth digit of an Integer?

# user inputs
num = int(input("Introduce the number: "))
dig = int(input("Introduce the nth digit: "))

# for finding divisors
div1 = 10
div2 = 1
ele = 0
for i in range(dig-1):                  # removing extra digits included in loop
        div1 *= 10
        div2 *= 10

ele = num % div1            # to remove extra digits on the left side
ele = ele // div2           # to remove extra digits on the right side
#ele = (num % div1) // div2      # % to remove extra digits on the left  and // on the right
print(f"The {dig}th element is '{ele}'.")

# sources
# source1: class explanation
# source2: https://www.learndatasci.com/solutions/python-double-slash-operator-floor-division/
