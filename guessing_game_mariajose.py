# GUESSING GAME - MARIA JOSE

# generate a random number
import random
random_n = random.randint(1, 1000)  # lower and maximum number

# initialize the range limits (max and min)
min_range = 1
max_range = 1000

# function to verify if the input is a valid number
def verify_numeric(u_str):
    while True:
        if u_str.isnumeric():
            if min_range <= int(u_str) <= max_range:
                break
            else:
                u_str = input(f"Error. Enter your guess from {min_range} to {max_range}: ")
            continue
        u_str = input(f"Error. The Game requires a valid number. Enter your guess from {min_range} to {max_range}: ")
    return int(u_str)           # convert the str to int

# user input the number
user_n = input(f"Enter your guess from {min_range} to {max_range}: ")
user_n = verify_numeric(user_n)

# loop to compare
count_guess = 0
while random_n != user_n:
    count_guess += 1            # increases the count of guesses
    print(f"Wrong! Guess count: {count_guess}")
    # nested loop to change the range
    if random_n > user_n:
        min_range = user_n + 1
    else:
        max_range = user_n - 1
    user_n = input(f"Enter your guess from {min_range} to {max_range}: ")
    user_n = verify_numeric(user_n)

# print from the right guess
if random_n == user_n:
    count_guess += 1            # increases the count of guesses
    print(f"You got it! The hidden number is {random_n}.")
    print(f"It took you {count_guess} guess(es).")
